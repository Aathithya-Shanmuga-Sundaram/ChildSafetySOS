import random
import requests
from transformers import pipeline

classifier=pipeline("text-classification", model="unitary/toxic-bert")

#Telegram Bot Setup
Bot_token = "8413444861:AAHMqX1NTO5bGsBs0uXFzwhyLxjgYuDb0hI"
Parent_token = "5061583546"

def SOS(message,label,score,sender):
    text=f"SOS ALERT \n From {sender}\n Message:{message}\nType:{label}\nRisk:{score:.2f}"
    url=f"https://api.telegram.org/bot{Bot_token}/sendMessage"
    requests.post(url,data={"chat_id":Parent_token,"text":text})

def sentimenal_analysis(message,sender):
    result=classifier(message)[0]
    label=result["label"]
    score=result["score"]

    flagged=label in ["toxic","obscene","threat","sexual_explicit"] and score >=0.8

    if flagged:
        print(f"{sender}: {message}")
        print("Alert:{sender} sent/received a flagged message!")
        SOS(message,label,score,sender)
    else:
        print(f"{sender}: {message}")

bot_replies=["Hi, How are You!","You are Dumb", "I will kill you", "I hate you"]

app_run=True
while app_run:
    child_msg=input("")
    if child_msg == "exit":
        app_run=False
        break
    else:
        sentimenal_analysis(child_msg,sender="Child")

    reply=random.choice(bot_replies)
    sentimenal_analysis(reply,sender="Bot/Friend")
