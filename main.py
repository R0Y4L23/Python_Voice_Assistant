import time
import pyttsx3
import speech_recognition as sr
from selenium import webdriver

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold=4000
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"
    return query

def search_web(search_q):
    driver = webdriver.Chrome(executable_path=r"C:\Users\Subham Roy\Documents\Drivers\chromedriver.exe")
    driver.get("https://www.google.com/")
    driver.maximize_window()
    print(driver.title)
    searchBar = driver.find_element_by_class_name("gLFyf").send_keys(search_q)
    driver.implicitly_wait(2)
    searchBut = driver.find_element_by_class_name("gNO89b")
    searchBut.click()
    driver.implicitly_wait(2)
    firstLink = driver.find_element_by_class_name("LC20lb")
    firstLink.click()

def search_yt(search_q):
    driver = webdriver.Chrome(executable_path=r"C:\Users\Subham Roy\Documents\Drivers\chromedriver.exe")
    driver.get("https://www.youtube.com/")
    driver.maximize_window()
    driver.find_element_by_name("search_query").send_keys(search_q)
    driver.implicitly_wait(2)
    driver.find_element_by_id("search-icon-legacy").click()
    driver.implicitly_wait(2)
    links = driver.find_elements_by_id("video-title")
    links[0].click()

def search_wiki(search_q):
    driver = webdriver.Chrome(executable_path=r"C:\Users\Subham Roy\Documents\Drivers\chromedriver.exe")
    driver.get("https://en.wikipedia.org/wiki/Main_Page")
    driver.maximize_window()
    driver.find_element_by_name("search").send_keys(search_q)
    driver.implicitly_wait(2)
    driver.find_element_by_name("go").click()
    driver.implicitly_wait(2)
    links = driver.find_elements_by_tag_name("p")
    for link in links:
        if link.text != "":
            print(link.text)
            speak(link.text)
            break

if __name__ == '__main__':
    name_of_assistant = "Athena"
    owner = "Subham"
    speak("Now starting your personal voice assistant!")
    speak("Hey "+owner+", this is "+name_of_assistant+" , your personal Voice assistant. How may I assist you today?")
    while True:
        speak("listening now....")
        q = takeCommand().lower()
        if "hello" in q:
            t = "Hello,I am "+name_of_assistant+". How may I help you?"
            speak(t)
        elif "how are you" in q:
            speak("I am doing fine Sir.")
        elif "What is your name" in q:
            speak("hello "+owner+", I am "+name_of_assistant+", your voice assistant")
        elif "thank" in q:
            speak("welcome "+owner)
        elif "what are you doing" in q:
            speak("Hey "+owner+" , I am listening to your commands and trying to help you as much as I can")
        elif "search on web" in q:
            q=q.replace("search on web","")
            speak("Now opening your browser and search is being done")
            search_web(q)
        elif "search on youtube" in q:
            q=q.replace("search on youtube","")
            speak("Now opening your browser and search is being done on youtube")
            search_yt(q)
        elif "search on wikipedia" in q:
            q=q.replace("search on wikipedia","")
            speak("Now opening your browser and search is being done on wikipedia")
            search_wiki(q)
        elif "wait" in q:
            speak("how long do you want to wait?")
            q=takeCommand().lower()
            print(q)
            for i in range(1,int(q)+1):
                speak(i)
        elif 'stop' in q:
            speak("ok , quitting the program")
            break
        else:
            speak("you said "+q+" which is not in my command list. So I am sorry that I cannot help you.")
