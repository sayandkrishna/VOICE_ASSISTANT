import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import sys
import datetime

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    microphone = sr.Microphone()
    with microphone as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source)
            query = r.recognize_google(audio, language="eng-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            print(e)
            return "SOME ERROR OCCURRED. SORRY FROM JARVIS"

if __name__ == '__main__':
    print('PyCharm')
    say("HALLO I AM SHAMINA HOW MAY I HELP YOU ")
    print("Listening...")
    while True:
        query = takeCommand()
        sites = [
            ["YouTube", "https://www.youtube.com"],
            ["Google", "https://www.google.com"],
            ["Mail", "https://www.gmail.com"],
            ["BBC News", "https://www.bbc.com/news"],
            ["CNN", "https://www.cnn.com"],
            ["The New York Times", "https://www.nytimes.com"],
            ["ESPN", "https://www.espn.com"],
            ["BBC Sport", "https://www.bbc.com/sport"],
            ["Coursera", "https://www.coursera.org"],
            ["Khan Academy", "https://www.khanacademy.org"],
            ["Wikipedia", "https://www.wikipedia.org"],
            ["Jio Cinema", "https://www.jiocinema.com/"],
            ["Reddit", "https://www.reddit.com"],
            ["Facebook", "https://www.facebook.com"],
            ["Twitter", "https://www.twitter.com"],
            ["Instagram", "https://www.instagram.com"],
            ["LinkedIn", "https://www.linkedin.com"],
            ["Amazon", "https://www.amazon.com"],
            ["eBay", "https://www.ebay.com"],
            ["Netflix", "https://www.netflix.com"],
            ["Spotify", "https://www.spotify.com"]
        ]
        deviceapps = [
            ["settings", "start ms-settings:"],
            ["calculator", "calc"],
            ["notepad", "notepad"],
            ["command prompt", "cmd"],
            ["task manager", "taskmgr"],
            ["control panel", "control"],
            ["file explorer", "explorer"],
            ["powershell", "powershell"],
            ["snipping tool", "snippingtool"],
            ["system information", "msinfo32"],
            ["disk management", "diskmgmt.msc"],
            ["device manager", "devmgmt.msc"],
            ["event viewer", "eventvwr"],
            ["services", "services.msc"],
            ["registry editor", "regedit"],
            ["performance monitor", "perfmon"]
        ]

        if query:
            if "stop" in query.lower():
                say("Stopping the program. Have a good day.")
                sys.exit()
            found = False
            for site in sites:
                if f"open {site[0]}".lower() in query.lower():
                    webbrowser.open(site[1])
                    say(f"Opening {site[0]}")
                    found = True
                    break
            if not found:
                for app in deviceapps:
                    if f"open {app[0]}".lower() in query.lower():
                        say(f"Opening {app[0]}")
                        os.system(app[1])
                        found = True
                        break
            if not found:
                if "the time" in query:
                    strftime = datetime.datetime.now().strftime("%H:%M:%S")
                    say(f'Sir, the time is {strftime}')
                    found = True
            if not found:
                say("Searching on Google")
                webbrowser.open(f"https://www.google.com/search?q={query}")
