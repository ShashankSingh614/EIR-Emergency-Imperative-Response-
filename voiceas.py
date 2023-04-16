# impoerting all the required modules
import pyttsx3
import speech_recognition as sr
import os

#running the voice 
engi = pyttsx3.init()
voi = engi.getProperty("voices")
engi.setProperty("voice", voi[1].id)

#defining all the required function

def filwrite(txt):
    fil1= open("dat.txt",'a')
    fil1.write(txt+'\n')

def speak(audio):
    engi.say(audio)
    print(audio)
    engi.runAndWait()


def talk():
    rec = sr.Recognizer()

    with sr.Microphone() as source:
        rec.adjust_for_ambient_noise(source)
        print("Listening...")
        rec.pause_threshold = 1
        audio = rec.listen(source)

    try:
        print("Recognizing...")
        query = rec.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as err:
        print(err)
        print("Unable to Recognize your voice.")
        return "None"

    return query


def readinput(prompt):
    return prompt.split()

def googlesearch(query):
    try:
        import requests
        from bs4 import BeautifulSoup
        url = 'https://www.google.com/search?q=' + query
        print ('your query is :',query)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        search_result = soup.find("div", class_="kCrYT")
        paragraph_text = search_result.find("div", class_="BNeawe s3v9rd AP7Wnd").text
        return (paragraph_text)
    except:
        query= 'how to'+query
        import requests
        from bs4 import BeautifulSoup
        url = 'https://www.google.com/search?q=' + query
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        search_result = soup.find("div", class_="kCrYT")
        paragraph_text = search_result.find("div", class_="BNeawe s3v9rd AP7Wnd").text
        return (paragraph_text)


def strttalk(val):
    if val == 1:
        speak("hello there, Eir at your service, what's the emergency")
    elif val == 2:
        speak("is the victim conscious and breathing")
    elif val == 3:
        speak("is the victim in need of cpr if not check for laceration and bleeding")
    elif val == 4:
        speak("check for laceration and bleeding")
    elif val == 5:
        speak("where is the bulk of injury located")
    elif val == 6:
        speak("is there any fracture or swelling")
    elif val == 7:
        speak(
            "now may i suggest to either put the person in recovery position or move it"
        )
    elif val == 8:
        speak("now would you like to put the patient in recovery position")
    elif val == 9:
        speak("would you like to search anything else , to close just say exit")

def clear():
    return os.system("cls")
while True:
    val = 1
    while True:
        strttalk(val)

        prompt = talk().lower()
        filwrite(prompt)

        if any(map(lambda w: w in prompt, ("accident", "crash", "injury"))):
            filel = open(r"accidentbase.txt", "r")
            speakingLines = filel.read()
            speak(speakingLines)
            val = 2

        elif "exit" in prompt :
            speak("Thanks for giving me your time")
            exit()

        elif any(
            map(lambda w: w in prompt, ("breath", "not breathing", "trouble breathing"))
        ):
            filel = open(r"breadth.txt", "r")
            speakingLines = filel.read()
            speak(speakingLines)
            val = 3

        elif any(
            map(
                lambda w: w in prompt,
                ("cpr", "chest compression", "Cardiopulmonary", "resuscitation"),
            )
        ):
            filel = open(r"cpr.txt", "r")
            speakingLines = filel.read()
            speak(speakingLines)
            val = 4
        elif any(
            map(
                lambda w: w in prompt,
                ("lacerations", "wounds", "bleeding", "avulsions"),
            )
        ):
            filel = open(r"cpr.txt", "r")
            speakingLines = filel.read()
            speak(speakingLines)
            val = 5
        elif any(map(lambda w: w in prompt, ("injury", "injured"))):
            if any(map(lambda w: w in prompt, ("head", "top", "mouth", "face"))):
                filel = open(r"head.txt", "r")
                speakingLines = filel.read()
                speak(speakingLines)
                val = 6

            elif any(
                map(
                    lambda w: w in prompt,
                    ("chest", "mid", "stomach", "front", "torso", "body"),
                )
            ):
                filel = open(r"chest.txt", "r")
                speakingLines = filel.read()
                speak(speakingLines)
                val = 6

            elif any(
                map(lambda w: w in prompt, ("back", "spine", "spinal", "shoulder"))
            ):
                filel = open(r"spine.txt", "r")
                speakingLines = filel.read()
                speak(speakingLines)
                val = 6

        elif any(
            map(lambda w: w in prompt, ("fracture", "broke", "break", "swelling"))
        ):
            filel = open(r"fracture.txt", "r")
            speakingLines = filel.read()
            speak(speakingLines)
            val = 7

        elif any(
            map(
                lambda w: w in prompt,
                ("carry", "change position", "displace", "moving"),
            )
        ):
            filel = open(r"moving.txt", "r")
            speakingLines = filel.read()
            speak(speakingLines)
            val = 8

        elif any(
            map(
                lambda w: w in prompt,
                ("recovery position", "position", "sitting", "resting"),
            )
        ):
            filel = open(r"rp.txt", "r")
            speakingLines = filel.read()
            speak(speakingLines)
            val = 9
        elif any(
            map(
                lambda w: w in prompt,
                ("google search"),
            )
        ):
            speak("what do you want to search")
            qury = talk()
            outcome = googlesearch(qury)
            speak(outcome)
        
        elif val == 10 and 'yes' in prompt:
            speak("what do you want to search")
            qury = talk()
            outcome = googlesearch(qury)
            speak(outcome)
        else:
            speak("sorry we did'nt quite understant what to do. whould you like to search for it in google")
            val = 10