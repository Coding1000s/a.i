import pyttsx3
import speech_recognition as sr
import datetime
import random
import os
import openai
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer , QTime , QDate , Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from ui import Ui_MainWindow 
import sys

'''def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=38096a5969bd4ed58277dc95b0230ba3'

    main_page = requests.get(main_url).join()
    articles = main_page["articles"]
    head = []
    day=["first","second"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        say(f"today's {day[i]} news is: {head[i]}")'''





chatStr = ""
def chat(query):
    global chatStr
    print(chatStr)
    #apikey = "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"
    #openai.api_key_path = ('C:/Users/RIHAN/Desktop/A.I/config.py')
    #openai.api_kay = apikey
    
    chatStr += f"user: {query}\n A.I: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]
    if not os.path.exists("ai"):
        os.mkdir("ai")

   #with open(f"ai/prompt- {random.randint(1, 9999999999999999999999)}", "w") as f:
    with open(f"ai/prompt/{''.join(prompt.split('intelligence')[1:]).strip }.txt", "w") as f:
        f.write(text)






#set openai_api_key=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

#openai.api_key = os.getenv("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")
#apikey = "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"
openai.api_key = "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"
#openai.api_key_path = ('C:/Users/RIHAN/Desktop/A.I/config.py')

def ai(prompt):
    #apikey = "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"
    #openai.api_key_path = ('C:/Users/RIHAN/Desktop/A.I/config.py')
    #openai.api_kay = apikey
    text = f"ai response for Prompt: {prompt} \n***********************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("ai"):
        os.mkdir("ai")

   #with open(f"ai/prompt- {random.randint(1, 9999999999999999999999)}", "w") as f:
    with open(f"ai/prompt/{''.join(prompt.split('intelligence')[1:]).strip }.txt", "w") as f:
        f.write(text)
    


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def say(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def commend():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        say("Say that again please...")
    return query

    #return None

'''def chat(query):'''


def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        say("good morning")

    elif hour>12 and hour<18:
        say("good afternoon")

    else:
        say("good evening")
    say("i am a i made by rihhaan")



if __name__ == "__main__":
    wish()
    while True:


        query = commend().lower()


        '''if "hello" in query:
            say('hello')'''
        
        if "using artificial intelligence".lower() in query.lower():
            ai(prompt=query)


        elif "exit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""


        else:
            print("chating...")
            chat(query)

        



