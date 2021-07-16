import json
import secrets
import requests
def post(url, data=None):
    data = json.dumps(data, ensure_ascii=False)
    data = data.encode(encoding="utf-8")
    r = requests.post(url=url, data=data)
    print("post: ", "url: ", url, " data: ", data)
    r = json.loads(r.text)
    return r

conversation_id = secrets.token_urlsafe(16)  # 随机生成会话id
messages_url = "http://host.docker.internal:5005/conversations/{}/messages".format(conversation_id)  # 发送消息
predict_url = "http://host.docker.internal:5005/conversations/{}/predict".format(conversation_id)  # 预测下一步动作
execute_url = "http://host.docker.internal:5005/conversations/{}/execute".format(conversation_id)  # 执行动作

if __name__ == "__main__":
    action = "action_listen"  # 动作初始化为等待输入
    while True:
        print("action=", action)
        if action in ["action_listen", "action_default_fallback", "action_restart"]:
            # 等待输入
            text = input("Your input ->  ")
            post(messages_url, data={"text": text, "sender": "user"})  # 发送消息

        response = post(predict_url)  # 预测下一步动作
        action = response["scores"][0]["action"]  # 取出置信度最高的下一步动作
        #print(response)

        response = post(execute_url, data={"name": action})  # 执行动作
        messages = response["messages"]  # 取出对话信息
        if messages:
            print(messages)

# from: https://blog.csdn.net/lly1122334/article/details/106072969
