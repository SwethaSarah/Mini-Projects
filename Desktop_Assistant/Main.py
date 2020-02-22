import os
import datetime
import playsound
import speech_recognition as sr
from gtts import gTTS
import subprocess
import webbrowser

class Voice_Assistant:
      
  def __init__(self):
    self.Assistant=' Maaya '
    self.User='Inspire'
    self.User_info='Computer Engineering Student'
    self.txt=1


  def Speak(self,text):
    tts=gTTS(text=text,lang="en")
    file=str(self.txt)+".mp3"
    tts.save(file)
    playsound.playsound(file,True)
    self.txt+=1
    os.remove(file)


  def Listen_to_source(self):
    rec_obj=sr.Recognizer()
    print('listening')
    with sr.Microphone() as source:
     audio=rec_obj.listen(source)
     resp_text=""
    try:
        resp_text=rec_obj.recognize_google(audio).lower()
        return resp_text
    except:
        self.Speak("Sorry,I didn't get you.Try again") 
      

  def Initialize_VA(self):
     curr_time=int(datetime.datetime.now().hour)
     if curr_time>=0 and curr_time<12:
       self.Speak('Good morning '+self.User)
     elif curr_time>=12 and curr_time<17:
       self.Speak('Good afternoon '+self.User)
     else:
        self.Speak('Good evening '+self.User)
     self.Speak('How can I help you')
  

  def Notepad(self):
    self.Speak('Ok,tell me how should I save it')
    filename=self.Listen_to_source()
    self.Speak('What should I write down')
    content=self.Listen_to_source()
    filename=str(filename)+".txt"
    with open(filename,"w") as f:
        f.write(content)
    subprocess.Popen(["notepad.exe",filename])
    self.Speak("Do you want me to save it?")
    text=self.Listen_to_source()
    if 'no' in text:
       os.remove(filename)
    else:
       self.speak("Saved it for future reference")


  def Open_browser(self):
    url="http://www.google.com"
    chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
    webbrowser.open_new_tab(url)
    self.Speak("here you go")

  
  def Change_user_details(self):
      self.Speak('How should I call you')
      self.User=self.Listen_to_source()
      self.Speak=('What are you')
      self.User_info=self.Listen_to_source()
      self.Speak('User information changed successfully')
  
  def Details(self):
      self.Speak("I am  "+self.Assistant+"  voice assistant of "+self.User)
      self.Speak('User '+self.User+' she is '+self.User_info +'she made me')


VA_obj=Voice_Assistant()
VA_obj.Initialize_VA()
text=VA_obj.Listen_to_source()
while(True):
  if 'stop' in text:
      break
  elif 'who are you' in text or 'details' in text:
    VA_obj.Details()
  elif 'notepad' in text or 'make a note' in text:
    VA_obj.Notepad()
  elif 'browser' in text or 'google' in text:
    VA_obj.Open_browser()
  elif 'change user information' in text:
    VA_obj.Change_user_details()
  text=VA_obj.Listen_to_source()