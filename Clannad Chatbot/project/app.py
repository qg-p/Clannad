from conversation import *
import json

from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = "static"

@app.route("/")
def home():
    return render_template("index.html")

# 装饰器。设置函数成员变量
def static_vars(**kwargs):
    def decorated(func):
        for _ in kwargs:
            setattr(func, _, kwargs[_])
        return func
    return decorated

@static_vars(msgque=[])
# msgque：应答消息的队列
def popmsg():
    # 当队列非空，返回其第一个元素并弹出
    if len(popmsg.msgque):
        _ = popmsg.msgque[0]
        popmsg.msgque.pop(0)
        print("pop: "+_)
        return _
    return None

def pushmsg(Type, msg):
    popmsg.msgque.append([Type, msg])
    print("output:"+Type+":"+msg)

def msgempty():
    if len(popmsg.msgque):
        return True
    return False

def clearmsg():
    popmsg.msgque = []

def popmsg_all():
    print("pop_all: ", popmsg.msgque)
    msg = json.dumps(popmsg.msgque)
    clearmsg()
    print(msg)
    return msg

def send_text(text:str):
    msg = json.dumps([["text", text]])
    return msg
def send_image(imgsrc:str):
    msg = json.dumps([["image", imgsrc]])
    return msg

global action
action = "action_listen"
# action: 状态机状态
@app.route("/get")
def get_response():
    global action
    print("action:"+action)
    # 等待输入
    userText = request.args.get("msg")
    print("input: "+userText)
    post(messages_url, data = {"text": userText, "sender": "user"})

    print("mark #1");
    def trypushmsg(key, _):
        if key in _:
            pushmsg(key, _[key])
    while True:
        print("Interactive with rasa...")
        response = post(predict_url)
        action = response["scores"][0]["action"] # most possible action
        print("action:"+action)
        response = post(execute_url, data = {"name": action})
        if action in ["action_listen", "action_default_fallback", "action_restart"]:
            print("break")
            break
        messages = response["messages"]
        print(messages)
        if (messages):
            for _ in messages:
                trypushmsg("text", _)
                trypushmsg("image", _)

    #pushmsg("image", "static/zodiacs/Aries.svg")
    msg = popmsg_all()
    if msg == "[]":
        msg = send_text("Sorry, I don't understand.") # default response "Speak English, please."
    print("send: ", msg)
    return msg

if __name__ == "__main__":
    #print(action)
    action = "action_listen"
    clearmsg()
    app.run(host="0.0.0.0", port=5000)
