from tkinter import *
import random
import requests
import json
import wikipedia
import webbrowser
import pyttsx3
import speech_recognition as sr
import pyaudio
import os
import time
import sys


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        r.adjust_for_ambient_noise(source)
        b.set("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        bot_screen.update()
    try:
        b.set("Recognising.....")
        query = r.recognize_google(audio, language="en-in")
        b.set(f"user said:{query}\n")
        bot_screen.update()

    except:
        b.set("say again")
        bot_screen.update()
        return None
    return query

class Windows:
    def BMI(self):
        os.system("start \"\" https://www.calculator.net/bmi-calculator.html")

    def Game(self):
        os.system("start \"\" https://www.crazygames.com/t/first-person-shooter")

    def Currency_Converter(self):
        os.system("start \"\" https://www.xe.com/currencyconverter/")


    def Weather_Condition(self):
        api_key = r"fc1e42af75daae80a0b4c0ff9e9e6378"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        complete_url = base_url + "appid=" + api_key + "&q=" + "jaipur"
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            return " Temperature (in kelvin unit) = " + str(current_temperature) + "\n atmospheric pressure (in hPa unit) = " +str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " + str(weather_description)

        else:
            return " City Not Found "


class Non_Windows:

    def Text_To_Speech(self, audio):
        engine = pyttsx3.init('sapi5')
        voice = engine.getProperty('voices')
        engine.setProperty("voice", voice[1].id)
        engine.say(audio)
        engine.runAndWait()

    def Google_Search(self, q):
        webbrowser.open(f"https://www.google.com/search?q={q.replace(' ', '+')}")

    def Calculation(self, q):
        return eval(q)

    def Wikipedia(self, q):
        q = q.replace("wikipedia", "")
        results = wikipedia.summary(q, sentences=2)
        return results

    def Password_Generator(self):
        values = [i for i in "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"]
        a = []
        for i in range(10):
            a.append(random.choice(values))
        final = "".join(a)
        return final

    # def Covid_Visualizer(self):
    #     corona = []
    #     url = r"https://api.covid19india.org/data.json"
    #     page = requests.get(url)
    #     data = json.loads(page.text)
    #     return "Total Active Cases are - " + str(data["statewise"][0]["active"]) + " " + "Total Active Confirmed are - " + str(data["statewise"][0]["confirmed"])

    def Flip_A_Coin(self):
        coin = ["HEAD", "TAIL"]
        return random.choice(coin)

    def Roll_Dice(self):
        dice = [1, 2, 3, 4, 5, 6]
        return random.choice(dice)

# MAIN GUI


text = StringVar


root = Tk()
root.geometry("940x360")
root.title("Chat-Bot")

win = Windows()
non_win = Non_Windows()


def voice_button_function():

    a.set(takecommand())
    user_screen.update()
    Button_function()


def Button_function():

    user_said = user_screen.get()
    x = user_said.lower()
    jokes = ['My wife told me to stop impersonating a flamingo. I had to put my foot down.',
             'I went to buy some camo pants but couldn’t find any',
             'I failed math so many times at school, I can’t even count.',
             'I used to have a handle on life, but then it broke.',
             'I was wondering why the frisbee kept getting bigger and bigger, but then it hit me']

    if "joke" in x:
        b.set(random.choice(jokes))
        bot_screen.update()

    elif "hello" in x:
        b.set("Hello")
        bot_screen.update()

    elif "hey" in x:
        b.set("Hello")
        bot_screen.update()

    elif "name" in x:
        b.set("I am Frizzy")
        bot_screen.update()

    elif "age" in x:
        b.set("an infinite years of age")
        bot_screen.update()

    elif "bye" in x:
        b.set("BYE Take Care")
        bot_screen.update()
        time.sleep(3)
        sys.exit()

    elif "tata" in x:
        b.set("BYE Take Care")
        bot_screen.update()
        time.sleep(3)
        sys.exit()

    elif "bmi" in x:
        win.BMI()

    elif "health" in x:
        win.BMI()

    elif "game" in x:
        win.Game()

    elif "play" in x:
        win.Game()

    elif "fun" in x:
        win.Game()

    elif "weather" in x:
        x = win.Weather_Condition()
        b.set(x)
        bot_screen.update()

    elif "search" in x:
        x = x.replace("search", "")
        non_win.Google_Search(x)

    elif "speak" in x:
        x = x.replace("speak", "")
        non_win.Text_To_Speech(x)

    elif "search for" in x:
        x = x.replace("search for", "")
        non_win.Google_Search(x)

    elif "password" in x:
        b.set(non_win.Password_Generator())
        bot_screen.update()

    elif "wikipedia" in x:
        b.set(non_win.Wikipedia(x))
        bot_screen.update()

    elif "corona" in x:
        b.set(non_win.Covid_Visualizer())
        bot_screen.update()

    elif "coin" in x:
        b.set(non_win.Flip_A_Coin())
        bot_screen.update()

    elif "dice" in x:
        b.set(non_win.Roll_Dice())
        bot_screen.update()

    elif not x.replace(" ", "").isalpha():
        b.set(non_win.Calculation(x))
        bot_screen.update()

    else:
        b.set("I can't understand")
        bot_screen.update()

    non_win.Text_To_Speech(bot_screen.get())
    b.set("")
    bot_screen.update()


f1 = Frame(root, bg="white")
f1.grid()

instruction_img = PhotoImage(file=r"D:\all subject notes\project\chatbot icon.png")
instruction_img_main = instruction_img.subsample(1, 1)

instruction_label = Label(f1, image=instruction_img_main)
instruction_label.grid(row=1, column=0)

img_human_bot = PhotoImage(file=r"D:\all subject notes\project\human bot.png")
img_human_main = img_human_bot.subsample(4, 4)

instruction_label1 = Label(f1, image=img_human_main)
instruction_label1.grid(row=1, column=1)

img_robot_bot = PhotoImage(file=r"D:\all subject notes\project\robot.png")
img_robot_main = img_robot_bot.subsample(2, 2)

instruction_label2 = Label(f1, image=img_robot_main)
instruction_label2.grid(row=2, column=1)

a = StringVar()
a.set("  ")

user_screen = Entry(f1, textvariable=a, bg="#02dee1", font=("Times Bold", 22))
user_screen.grid(row=1, column=2, ipady=50, padx=10)

b = StringVar()
b.set("Hello,I am FRIZZY!")

bot_screen = Entry(f1, textvariable=b, bg="#02dee1", font=("Times Bold", 22))
bot_screen.grid(row=2, column=2, ipady=50)

img_speech = PhotoImage(file=r"D:\all subject notes\project\mic.png")
img_speech_main = img_speech.subsample(12, 12)

b2 = Button(f1, image=img_speech_main, command=voice_button_function)
b2.grid(row=1, column=4)

img_click = PhotoImage(file=r"D:\all subject notes\project\click.png")
img_click_main = img_click.subsample(8, 8)

b2 = Button(f1, image=img_click_main, bg="white", command=Button_function)
b2.grid(row=1, column=5, padx=10)

root.mainloop()