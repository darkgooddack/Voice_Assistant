import os, webbrowser, sys, requests, subprocess, pyautogui, vosk, g4f, queue, voice
import sounddevice as sd
import pyttsx3
from telegram import Bot
import openai
import speech_recognition as sr
import pyttsx3
import telebot
import json
from datetime import datetime

engine = pyttsx3.init()
engine.setProperty('rate', 160)
bot = telebot.TeleBot('6873601461:AAFb89VE2_-hAXUarsQWJ5apSCdTk1DkMoY')

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
    project_path = "D:\\мой 3 курс\\Python\\the_applicant's_assistant"
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

def picture():
    pass

def create_project():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    project_name = f"{timestamp}"
    print("work")
    project_path = f"D:\\PythonProjects\\{project_name}"
    try:
        os.makedirs(project_path, exist_ok=True)
        print("work2")
        subprocess.run(["pycharm", project_path])
        speaker(f"Проект {project_name} создан в PyCharm")
        os.startfile(project_path)
        print("work3")
    except Exception as e:
        print(f"Failed to create project: {e}")
        speaker("Не удалось создать проект")

def get_chat_id(contact_name):
    try:
        user = bot.get_chat(contact_name)
        return user.id
    except Exception as e:
        print(f"Failed to get chat ID: {e}")
        return None

def telegramto():
    speaker("Кому вы хотите отправить сообщение?")
    contact_name = input("Введите имя контакта: ")
    speaker("Диктуйте сообщение")
    message = input("Введите сообщение: ")
    speaker(f"Вы хотите отправить следующее сообщение контакту {contact_name}: {message}? Скажите 'отправляй' для подтверждения.")
    confirmation = input("Подтверждение (отправляй/нет): ")
    if confirmation.lower() == 'отправляй':
        chat_id = get_chat_id(contact_name)  # Implement this function to get the chat ID by contact name
        if chat_id:
            speak_and_send_message(chat_id, message)
        else:
            speaker(f"Контакт {contact_name} не найден")
    else:
        speaker("Сообщение не отправлено")

# Function to send a message to a chat
def send_message(chat_id, message):
    bot.send_message(chat_id, message)

# Function to synthesize speech and send a message to a chat
def speak_and_send_message(chat_id, text):
    engine.say(text)
    engine.runAndWait()
    send_message(chat_id, text)