#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 16:30:17 2020

@author: kartikmacbook
"""
import webbrowser
import os
import speech_recognition as sr
import subprocess
#import pyaudio
import pyttsx3


    

def process():
    
    
        if 'current' in text and 'process' in text:
                     
             os.system("ps -A > process.txt")
                     
             src_file = 'process.txt'
             src_dir = os.getcwd()
             src_file_location = os.path.join(src_dir, src_file)
             open(src_file_location)
             os.system("open process.txt") 
             print('Done!!')
        
        elif 'what' in text and 'can' in text and 'do' in text:
            pyttsx3.speak('I can create or remove directory, i can let you know the \
                          meaning of word, i can open any application for you\
                              i can let you know the current process running in your system')
        
        elif 'you' in text and 'mad' in text:
            pyttsx3.speak('yes i am mad')    
        
        elif ('create' in text) or ('make' in text) and ('directory' in text) or ('folder' in text):
            if ('desktop' in text):   
                pyttsx3.speak('Let me know the  name of your directory:')
                with sr.Microphone() as destination:
                    Path = r.listen(destination)
                Name_dir = r.recognize_google(Path)
                subprocess.getstatusoutput(f'mkdir /Users/kartik_rama_arora/Desktop/{Name_dir}')
                print('Done!!')

            elif ('documents' in text):
                pyttsx3.speak('Let me know the  name of your directory:')
                with sr.Microphone() as destination:
                    path = r.listen(destination)
                name_dir = r.recognize_google(path)
                subprocess.getstatusoutput(f'mkdir /Users/kartik_rama_arora/Documents/{name_dir}')
                print('Done!!')
            elif ('downloads' in text):
                pyttsx3.speak('Let me know the  name of your directory:')
                with sr.Microphone() as destination:
                    path = r.listen(destination)
                name_dir = r.recognize_google(path)
                subprocess.getstatusoutput(f'mkdir /Users/kartik_rama_arora/Downloads/{name_dir}')
                print('Done!!')
            else:
                pyttsx3.speak('Let me know the  name of your directory:')
                with sr.Microphone() as destination:
    
                    Path = r.listen(destination)
                Name_dir = r.recognize_google(Path)
                subprocess.getstatusoutput(f'mkdir {Name_dir}')
                print('Done!!')
        elif 'remove' in text or 'delete' in text and 'directory' in text or 'folder' in text:
            if ('desktop' in text):   
                pyttsx3.speak('Let me know the  name of your directory:')
                with sr.Microphone() as destination:
                    Path = r.listen(destination)
                Name_dir = r.recognize_google(Path)
                subprocess.getstatusoutput(f'rmdir /Users/kartik_rama_arora/Desktop/{Name_dir}')
                print('Done!!')

            elif ('documents' in text):
                pyttsx3.speak('Let me know the  name of your directory:')
                with sr.Microphone() as destination:
                    path = r.listen(destination)
                name_dir = r.recognize_google(path)
                subprocess.getstatusoutput(f'rmdir /Users/kartik_rama_arora/Documents/{name_dir}')
                print('Done!!')
            elif ('downloads' in text):
                pyttsx3.speak('Let me know the  name of your directory:')
                with sr.Microphone() as destination:
                    path = r.listen(destination)
                name_dir = r.recognize_google(path)
                subprocess.getstatusoutput(f'rmdir /Users/kartik_rama_arora/Downloads/{name_dir}')
                print('Done!!')
            else:
                pyttsx3.speak('Let me know the  name of your directory:')
                with sr.Microphone() as destination:
                    Path = r.listen(destination)
                Name_dir = r.recognize_google(Path)
                subprocess.getstatusoutput(f'rmdir {Name_dir}')
                print('Done!!')
        elif 'open' in text or 'run' in text or 'application' in text:
            if 'google chrome' in text or 'chrome' in text:
                subprocess.getstatusoutput("open -a 'google chrome'")
                print('Done!!')
            elif 'safari' in text or 'browser' in text:
                subprocess.getstatusoutput('open -a safari')
                print('Done!!')
            elif 'calc' in text or 'caculator' in text:
                subprocess.getstatusoutput('open -a Calculator')
                print('Done!!')
            elif 'calender' in text:
                subprocess.getstatusoutput('open -a Calendar')
                print('Done!!')
            elif 'Photo Booth' in text or 'camera' in text:
                subprocess.getstatusoutput("open -a 'Photo Booth'")
                print('Done!!')
            elif 'text editor' in text or 'editor' in text or 'textedit' in text:
                subprocess.getstatusoutput("open -a textedit")
                print('Done!!')
            elif 'facetime' in text:
                subprocess.getstatusoutput('open -a facetime')
                print('Done!!')
            elif 'maps' in text:
                subprocess.getstatusoutput('open -a  maps')
                print('Done!!')
            else:
                pyttsx3.speak('Application not found!!')
        elif 'meaning' in text or 'means' in text or 'meaning of word' in text:
            pyttsx3.speak('Let me know the word:')
            with sr.Microphone() as word:
                word_mean = r.listen(word)
            word_name = r.recognize_google(word_mean)
            webbrowser.open(f'https://www.dictionary.com/browse/{word_name}')
            print('Done!!')
       
        else:
            pyttsx3.speak("Not audible")



pyttsx3.speak("hello!! I am yatharth, How can help you??")
        
r = sr.Recognizer()
        
with sr.Microphone() as source:
      print("i am listening...")
      audio = r.listen(source)
      print("please wait...")

text = r.recognize_google(audio)
process()  
 

while True:
    
        pyttsx3.speak('let me know you want me to do!')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("i am listening...")
            audio = r.listen(source)
            print("please wait...")
        text = r.recognize_google(audio)
        if 'exit' in text:
            pyttsx3.speak('Thank you to using me')
            break
        else:
            process()
        
