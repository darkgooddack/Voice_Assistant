import os, webbrowser, sys, requests, subprocess, pyautogui, vosk, g4f, queue, voice
import sounddevice as sd
import pyttsx3
from telegram import Bot
import openai
import speech_recognition as sr
import pyttsx3
import telebot
import json

engine = pyttsx3.init()
engine.setProperty('rate', 160)

def music():
    webbrowser.open('https://www.youtube.com/watch?v=e_Ms6YXnQsc&ab_channel=kizaru-Topic', new=2)

def speaker(text):
    engine.say(text)
    engine.runAndWait()

def browser():
    webbrowser.open('https://www.google.com/webhp?hl=ru&sa=X&ved=0ahUKEwj7n-KqqeGDAxW_-AIHHY8hADkQPAgJ', new=2)

def home():
    pyautogui.hotkey('win', 'd')

def game():
    print('игра запущена')

def offpc():
    #os.system('shutdown /s')
    print('пк выключен')

def offBot():
    sys.exit()

def passive():
    pass

def proect():
    project_path = "D:\\myapp"
    os.startfile(project_path)

def search_movie():
    webbrowser.open('https://kinogo.biz/', new=2)

def search_movie_history():
    webbrowser.open('https://kinogo.biz/istoricheskie/', new=2)


def openAI():
    question = ''
    q = queue.Queue()
    model = vosk.Model('model_small')

    device = sd.default.device = 0, 4
    samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])

    def callback(indata, frames, time, status):
        q.put(bytes(indata))

    with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0], dtype='int16', channels=1,
                           callback=callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        while question == '':
            data = q.get()
            if rec.AcceptWaveform(data):
                question = rec.Result()

    out = ''
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}],
        stream=True,
    )

    for message in response:
        out += message
    out = out.replace("*", '')
    out = out.replace('#', '')
    print(out)

    voice.speaker(out)




def telegram2():
    # Замените 'YOUR_BOT_TOKEN' на токен вашего бота
    bot = telebot.TeleBot('6873601461:AAFb89VE2_-hAXUarsQWJ5apSCdTk1DkMoY')

    # Функция для отправки сообщения в чат
    def send_message(chat_id, message):
        bot.send_message(chat_id, message)

    # Функция для синтеза речи и отправки сообщения в чат
    def speak_and_send_message(chat_id, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        send_message(chat_id, text)

    # Пример использования
    chat_id = '1741279318'  # Замените на ваш chat_id
    message = "Привет! Это сообщение отправлено из Python!"
    speak_and_send_message(chat_id, message)