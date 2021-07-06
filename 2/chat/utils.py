from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

import os

db = 'database.sqlite3'
is_new_chatbot = 0
if os.path.exists(db) == 0:# ''' validation required '''
    is_new_chatbot = 1
def chattingbot(name:str, similarity:float):
    bot = ChatBot(
        name,
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
            'chatterbot.logic.MathematicalEvaluation',
            'chatterbot.logic.TimeLogicAdapter',
            'chatterbot.logic.BestMatch',
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'I am sorry, but I do not understand. I am still learning.',
                'maximum_similarity_threshold': similarity
            }
        ],
        database_uri='sqlite:///'+db
    )
    return bot

def train(chatbot, dire):
    training_data_quesans = open('training_data/ques_ans.txt').read().splitlines()
    training_data_personal = open('training_data/personal_ques.txt').read().splitlines()

    training_data = training_data_quesans + training_data_personal

    additional_training_data = []
    for file in os.listdir(dire):
        file = dire+'\\'+file
        #print(file)
        file = open(file, 'r', encoding='utf-8')
        data = file.read()
        data = data.splitlines()
        additional_training_data.append(data)
    
    for additional in additional_training_data:
        training_data = training_data + additional

    trainer = ListTrainer(chatbot)
    trainer.train(training_data)

def trainEng(chatbot):
    # Training with English Corpus Data
    trainer_corpus = ChatterBotCorpusTrainer(chatbot)
    trainer_corpus.train(
        'chatterbot.corpus.english'
    )
#  # Training with Personal Ques & Ans
# conversation = [
#     "Hello",
#     "Hi there!",
#     "How are you doing?",
#     "I'm doing great.",
#     "That is good to hear",
#     "Thank you.",
#     "You're welcome."
# ]
# 
# trainer = ListTrainer(chatbot)
# trainer.train(conversation)
