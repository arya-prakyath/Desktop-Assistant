# Imports
import pyttsx3
import speech_recognition as sr
import time
import datetime
import os
import random
import wikipedia
import webbrowser
from selenium import webdriver
from tkinter import *
from PIL import Image, ImageTk
import pyautogui

# Initializing chrome browser
chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webBro = webbrowser.get('chrome')

# Create speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
voiceList = [0, 1, 2]
assistant = random.choice(voiceList)
engine.setProperty('voice', voices[assistant].id)

# Initialize the recognizer
r = sr.Recognizer()

# List of speech's
meRefList = ['arya', 'prakkyath', 'boss', 'big boss', 'master', 'sir']
aiInitList = ['How may I help you', 'what do you want me to do', 'whats up', 'shoot your command']
aiInit = random.choice(aiInitList)

# Function to make assistant speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Function to play music video
def play_music_vid(song):
    # Using selenium
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    rootyt = webdriver.Chrome('chromedriver.exe', options=options)
    song = song.split(' ')
    rootyt.get(f"https://www.youtube.com/results?search_query={'+'.join(song)}")
    time.sleep(3)
    # Click on 1st video
    first_vid = rootyt.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]')
    first_vid.click()
    rootyt.maximize_window()
    time.sleep(0.5)
    pyautogui.press('f')
    return None


# Function to play music
def play_music(song):
    # Using selenium,
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    rootgn = webdriver.Chrome('chromedriver.exe')
    rootgn.get(f"https://gaana.com/search/{song}")
    time.sleep(3)
    rootgn.minimize_window()
    # Click on 1st song
    first_song = rootgn.find_element_by_xpath('//*[@id="new-release-album"]/li[1]')
    first_song.click()
    return None


# Function to make assistant wish the user
def wish_me(a=1):
    if a == 1:
        wishing_choice_list = ['a', 'b', 'c']
        wishing_choice = random.choice(wishing_choice_list)

        if wishing_choice == 'a':
            hour = int(datetime.datetime.now().hour)
            if 0 <= hour < 12:
                speak("Good Morning {0}".format(random.choice(meRefList)))
            elif 12 <= hour < 15:
                speak("Good Afternoon {0}".format(random.choice(meRefList)))
            else:
                speak("Good Evening {0}".format(random.choice(meRefList)))

        elif wishing_choice == 'b':
            speak("Hey {0}".format(random.choice(meRefList)))

        else:
            speak("Hello {0}".format(random.choice(meRefList)))

    else:
        speak("{0} {1}".format(aiInit, random.choice(meRefList)))

    return None


# Function to take microphone input from the user and returns string output
error_count = 0
def take_command():
    global error_count
    # Intialize the microphone
    with sr.Microphone() as source:
        strings.insert(END, "Listening.......\n")
        root.update_idletasks()

        try:
            # r.adjust_for_ambient_noise(source)
            # r.pause_threshold = 1.00
            audio = r.listen(source)
            strings.insert(END, "Recognizing.....\n")
            root.update_idletasks()
            query = r.recognize_google(audio)
            strings.insert(END, f"THE_ARYA: {query}\n\n")
            root.update_idletasks()

        except Exception:
            error_count += 1
            if error_count < 3:
                speak("I'm sorry. say that again please")
                strings.insert(END, "Say that again please......\n")
                root.update_idletasks()
                return take_command()
            else:
                error_count = 0
                return 'error'

    return query


# End and exit the application
def exit_assistant():
    strings.delete(1.0, END)
    exit_list = ['bye bye', 'good bye', 'have a good day', 'my pleasure', 'see you later', 'bye']
    speak('{0} {1}'.format(random.choice(exit_list), random.choice(meRefList)))
    strings.insert(END, '\n\nCAll ME AGAIN WHENEVER NEEDED!!!\n\n')
    root.update_idletasks()
    strings.insert(END, "*" * 35 + "\n\n\n")
    root.update_idletasks()
    strings.insert(END, 'THE_ARYA AND Co.\n')
    root.update_idletasks()
    root.after(3000, root.quit())


# Main function to control assistant
def assistant_function():
    # Take commands
    query = take_command().lower()
    if query[0:4] == "exit" or query[0:4] == "mute":
        return

    # Logic for executing tasks based on query i.e "_the voice converted to text_"
    if ('the time' in query) or ('time is it' in query):
        t = time.asctime(time.localtime(time.time()))
        time_list = t.split(' ')
        speak(f"Sir, the time is {time_list[3].split(':')[0]} {time_list[3].split(':')[1]}")

    elif 'roll a die' in query:
        speak('dib dib. dib dib')
        time.sleep(0.5)
        speak(f'Its a {random.choice([1, 2, 3, 4, 5, 6])}')

    elif 'coin' in query:
        speak('on it sir. The coin has been tossed high')
        time.sleep(0.5)
        speak('and what you got is.')
        speak(random.choice(['heads', 'tails']))

    elif 'open youtube' in query:
        speak('do you want me to search for something')
        yt_search = take_command().lower()
        if yt_search[0:4] == "exit" or yt_search[0:4] == "mute":
            return
        if 'no' in yt_search:
            speak("Opening youtube {0}".format(random.choice(meRefList)))
            webBro.open("youtube.com")
        else:
            speak('What do you want me to search?')
            yt_search_query = take_command().lower()
            yt_search_query = yt_search_query.split(' ')
            speak("Opening youtube {0}".format(random.choice(meRefList)))
            webBro.open(f"https://www.youtube.com/results?search_query={'+'.join(yt_search_query)}")
        minimize()

    elif 'open google' in query:
        speak('opening google for you boss')
        webBro.open("")
        minimize()

    elif 'search' in query:
        query_list = query.split(' ')
        root.update_idletasks()
        webBro.open(f"https://www.google.com/search?q={'+'.join(query_list)}")
        speak("here's the result for your search query")
        minimize()

    elif 'open stack overflow' in query:
        speak('Opening stack overflow')
        webBro.open("stackoverflow.com")
        minimize()

    elif ('book gas' in query) or ('book the gas' in query):
        speak('Booking gas NOw. This may take a while')
        os.system(r'python "C:\Users\aryap\Documents\Python Scripts\py_Gas Booking\bookGas.py"')
        speak('my job of booking gas here is done, boss. hope you paid the money and confirmed the booking sir')
        minimize()

    elif ('covid app' in query)  or ('corona app' in query):
        speak('opening covid app')
        os.system("cd 'C:\\Users\\aryap\\Documents\\Python Scripts\\py_covidAid'")
        os.system("covidAid.exe")
        speak('covid app was successfully opened')
        minimize()

    elif ('play music' in query) or ('music for me' in query) or ('play song' in query) or ('song for me' in query):
        speak('choose the song')
        song = take_command().lower()
        speak('do you want video too?')
        isvid = take_command().lower()
        if isvid[0:4] == "exit" or isvid[0:4] == "mute":
            return
        if ('yes' in isvid) or ('s' in isvid) or ('yeah' in isvid):
            speak("Playing the song for you via youtube")
            try:
                play_music_vid(song)
                strings.insert(END, 'Enjoy the song.....\n')
                root.update_idletasks()
            except:
                speak("There is some problem. Try updating chrome driver.")
                strings.insert(END, 'There is some problem. Try updating chrome driver.\n')
                root.update_idletasks()
        else:
            speak("Playing the song for you")
            try:
                play_music(song)
                strings.insert(END, 'Enjoy the song.....\n')
                root.update_idletasks()
            except:
                speak("There is some problem. Try updating chrome driver.")
                strings.insert(END, 'There is some problem. Try updating chrome driver.\n')
                root.update_idletasks()
        time.sleep(0.5)
        minimize()

    elif ('wikipedia' in query) or ('what' in query) or ('who' in query) or ('whom' in query) or (
            'whose' in query) or ('where' in query) or (
            'when' in query) or ('why' in query) or ('which' in query) or ('how' in query) or ('tell me about' in query):
        speak('just a minute {0}'.format(random.choice(meRefList)))
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak(random.choice(["as far as i know", "what i know is that", "what i found is"]))
        strings.insert(END, results + "\n")
        root.update_idletasks()
        speak(results)
        speak('do you want more')
        more = take_command().lower()
        if ('yes' in more) or ('yesh' in more) or ('ya' in more) or ('yeah' in more):
            query_list = query.split(' ')
            speak('here you go sir')
            webBro.open(f"https://www.google.com/search?q={'+'.join(query_list)}")
        minimize()

    elif ('bye' in query) or ('goodbye' in query) or ('bhai' in query) or ('good night' in query) or (
            'sleep' in query) or (
            'rest' in query) or ('close' in query) or ('die' in query) or ('quit' in query) or (
            'exit' in query) or (
            'f*** off' in query):
        exit_assistant()

    else:
        strings.insert(END, 'Sorry Did not Catch that. Try again.\n')
        root.update_idletasks()
        speak('Sorry I Did not Catch that')


def call():
    exit['state'] = 'disabled'
    command['state'] = 'disabled'
    root.update_idletasks()
    wish_me(0)
    strings.delete(1.0, END)
    assistant_function()
    # strings.insert(END, '\n *** AI is Active. Press command. ***\n\n')
    exit['state'] = 'normal'
    command['state'] = 'normal'


def minimize():
    root.overrideredirect(False)
    root.update_idletasks()
    root.state('iconic')


def maximize(event):
    root.overrideredirect(True)
    root.update_idletasks()
    root.state('normal')


if __name__ == "__main__":
    root = Tk()
    root.overrideredirect(True)
    root.title("\tTHE_ARYA | JARVIS")
    root.geometry("1070x600+220+100")
    icon = PhotoImage(file="icon.png")
    root.iconphoto(False, icon)
    root.resizable(False, False)
    root["bg"] = "#00004d"
    root.bind("<Alt_L>", lambda e: minimize())
    root.wm_attributes("-topmost", 1)

    titleBar = Label(root, text="\tTHE_ARYA | AI", anchor=W, relief=SOLID,  height=2, bg="#00004d", fg="WHITE")
    titleBar.pack(side=TOP, fill=X, expand=True, pady=(0, 0))
    titleBar.bind("<Map>", maximize)
    minimizeButton = Button(titleBar, text='---', font=("", 15), bg="#00004d", fg="WHITE", anchor=CENTER, relief=SOLID, cursor="hand2", command=minimize)
    minimizeButton.pack(side=RIGHT, padx=(0, 15), pady=(0, 0))

    img = Image.open("background.jpg")
    bg = ImageTk.PhotoImage(img)
    main = Label(root, image=bg, cursor="tcross", relief=SOLID)
    main.pack(side=TOP, fill=BOTH, expand=True, pady=(0, 0))

    command = Button(main, text="COMMAND", width=38, height=2, relief=SOLID, bg="#00004d",
                   fg="WHITE", font=("consolas",), activebackground="#1f1f2e", activeforeground="WHITE",
                   cursor="hand2", command=call)
    command.pack(padx=(650, 0), pady=(50, 0))

    strings = Text(main, width=38, height=18, relief=SOLID, bg="#00004d",
                   fg="WHITE", font=("consolas",), state="normal", cursor="tcross")
    strings.pack(padx=(650, 0), pady=(10, 0))

    exit = Button(main, text="EXIT", width=38, height=2, relief=SOLID, bg="#00004d", fg="WHITE", font=("consolas",), activebackground="#1f1f2e", activeforeground="WHITE",
                  cursor="hand2", command=exit_assistant)
    exit.pack(padx=(650, 0), pady=(10, 10))

    strings.insert(END, '\n *** AI is Active. Press command. ***\n\n')
    root.update_idletasks()
    if assistant == 0:
        root.after(500, wish_me(), speak("I'm Jarvis"))
        titleBar['text'] = "\tTHE_ARYA | JARVIS"
    elif assistant == 1:
        root.after(500, wish_me(), speak("I'm Friday"))
        titleBar['text'] = "\tTHE_ARYA | FRIDAY"
    else:
        root.after(500, wish_me(), speak("I'm Edith"))
        titleBar['text'] = "\tTHE_ARYA | EDITH"
    root.mainloop()
