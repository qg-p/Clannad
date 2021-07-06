from utils import chattingbot, train, trainEng, db, is_new_chatbot
def response(i):
    flag = 0
    o=""
    if i == "exit" or i == "quit":
        flag = 2 # exit
    elif i == ".train" or i == ".update":
        print("updating...")
        train(chatbot, "training_data")
    elif i == ".learn Engilish" or i == ".upgrade":
        print("Training with English Corpus Data...")
        trainEng(chatbot)
    else:
        o = str(chatbot.get_response(i))
        flag = 1 # response from chatbot
    return flag, o

if __name__ == "__main__":
    print("Loading")
    chatbot = chattingbot("CoronaBot", 0.90)
    if is_new_chatbot:
        response(".update")
        response(".upgrade")
    while 1:
        i = input("Input: ")
        f, o = response(i)
        if (f == 1):
            print(o)
        elif (f == 2):
            print("bye")
            break
        else:
            continue