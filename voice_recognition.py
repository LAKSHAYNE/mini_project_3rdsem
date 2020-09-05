import speech_recognition as sr
import webbrowser
sr.Microphone(device_index=1)
r=sr.Recognizer()
r.energy_threshold=5000
with sr.Microphone() as source:
    print("Say 'web search' for a web search or say 'video' to stream a youtube video")
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("you said {}".format(text))
        if(text=="video"):
            print("which video you want stream")
            audio=r.listen(source)
            src=r.recognize_google(audio)
            print("searching for {}".format(src))
            url="https://youtube.co.in/search?q="
        elif(text=="web search"):
            print("which what do you want to search ")
            audio=r.listen(source)
            src=r.recognize_google(audio)
            print("playing {} video".format(src))
            url="https://google.co.in/search?q="
        search_url=url+src
        webbrowser.open(search_url)
    except:
        print("can't recognize")
