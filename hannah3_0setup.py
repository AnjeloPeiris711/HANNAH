from win10toast import ToastNotifier

notifier = ToastNotifier()
import pyaudio
import speech_recognition as sr
import pyttsx3
import os
import subprocess
from playsound import playsound
import random
import time
import ctypes
import webbrowser
#import google
import lookup_drive_change
speech = sr.Recognizer()
greeting_dict = {'hello': 'hello', 'hi': 'hi'}
open_launch_dict = {'open': 'open', 'launch': 'launch'}
google_searches_dict = {'what': 'what', 'why': 'why', 'who': 'who', 'which': 'which'}
social_media_dict = {'facebook': 'https://www.facebook.com', 'twitter': 'https://www.twitter.com'}
try:
    engine = pyttsx3.init()
except ImportError:
    print('Requested driver is not found')
except RuntimeError:
    print('Driver fails to initialize')
voices = engine.getProperty('voices')

engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate)
print('''
                                               `                                                    
                                             `-                                                     
                                            -/                 /                                    
                                           :o               `  s`                                   
                                          .d`              `: `h                                    
                                          os             `.s` o:                                    
                                          d: -`         `-+-`+:                                     
                                         `h: `+-      `.----/.                                      
                                        `.o+  `/+:-----..--`                                        
                                        `:-y     ````````         `                                 
                                         + h        `..```   `    -                                 
                                         o s`     `-:/++so/-::.   -`                                
                                         s`+.    `:::+hmNs:`.`    /`                                
                                        `s +.    ````./ss+/:`     o.                                
                                        .s +       ``.-::.`      `d.                                
                                        +: :                     :d`                                
                                       `y ``                    `-y` -                              
                                       s.                        .s  +                              
                                      /: :``   ``:               /+`/-                              
                                     ./  : -  `- -               s::`   .                           
                                     /`                         -o /    .`                          
                                    .-    `      ``             y` :    `-                          
                                    :  `--`  ..   `.--.        /: `m`   `:                          
                                    /  `   ..--..`            :+  :M/   `/                          
                                    /-      ```              -+   /mo   -: .                        
                                    .s   `.--:-:---`        //     .  ` o` -                        
                             `       s/                   ./.        :``s  /                        
                            `-       `y-                .::         -/ y` `/                        
                             :        .y-            `--.   -      .y`o/  /.                        
                             .:        `y:      ```..`      /     .h./s  `o    .ohhys+:             
                              /.        `s+                 o    .y-:y`  /:  `odo-````-o/           
                       ``     `o         `ss                s   `s--d.  .o   os`        +s`         
                      .`       .+         `sy`              s.  /:.d-  `y.  `s`.:`      `ho         
                     `-```      +.       `` hy`             +/  + y+  `y:   `:  -o       /N.        
                    `/:`        .o        : .mo             -y  /`d.  so         s`     `-M/        
                   `/:-          o.       /. sm`            `h- .-d` +h`         +`     -.N+        
                  `h..+          :/       -/ :M-             +s  .m:-m-          +      /-M-        
                  :M` s.         .s.`     `o :M-             `h:  smhh         `/.     ./+d`        
                  /M+ -y`        .y +     `y oM.              -d-``omd:`    `.:/.     `s-d:         
                  .Nm. :s.       -h s     `y dd`           `.--/y-  -mmo+////:.     `:s/y:          
            ...`   /Nd- -s:      /y s.    /s:Mh------://+++/-.` `/:` .yy:.` ````..-/ssoo.           
          -/:.`     /mm/ `+o-`   y/ y:   `h:mNhddhhys+/-.`         `   -sys+::::/+oo+/.             
         -/:    ``   .yNs. .+o/.-d. h:  .yoyN/                           `-/osoo+/-.                
        `/o.   ./      -sd+.  -/dh++moosy+hN+                                                       
        --+    y.        .+s+-`:y``/d::-omm:                                                        
        /.:    m:           ./sh/--ys/sdy/`                                                         
        :--`   od`       ``  -+``.od:-.`                                                            
        `s`.--``hd:..--.`  `/:   :y.                                                                
         .s: `-:/omm+`   `//`  .+/`                                                                 
           -+/-`  `/ydhoys/:::::                                                                    
              `--::::-.``.``+
''')

engine.say('     hello   sir .    i     am your artifical intelligans program. My name is HANNAH .So if we can understand each other tell me  your name? ')
engine.runAndWait()

name = (input('what is your name?'))
engine.say('nice to meat you {}'.format(name))
engine.runAndWait()


def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()


def get_index(text):
    if 'first' in text:
        return 0
    elif 'second' in text:
        return 1
    elif 'third' in text:
        return 2
    else:
        return None


def google_search_result(query):
    search_result = google.search(query)

    for result in search_result:
        print(result.description.replace('...', '').rsplit('.', 3)[0])
        if result.description != '':
            play_sound_from_polly(result.description.replace('...', '').rsplit('.', 3)[0], is_google=True)
            break


def is_valid_google_search(phrase):
    if (google_searches_dict.get(phrase.split(' ')[0]) == phrase.split(' ')[0]):
        return True


def Music(Music):
    Music = random.choice(Music)


def play_sound(song):
    playsound(song)


def play_sound(laugh):
    playsound(laugh)


def is_valid_note(greet_dict, voice_note):
    for key, value in greet_dict.items():
        try:
            if value == voice_note.split(' ')[0]:
                return True

            elif key == voice_note.split(' ')[1]:
                return True

        except IndexError:
            pass

    return False


while True:

    voice_note = input('cmd').lower()
    print('cmd : {}'.format(voice_note))
    if is_valid_note(greeting_dict, voice_note):
        speak_text_cmd('hi  {}. how can i help you?'.format(name))
        continue
    elif is_valid_note(open_launch_dict, voice_note):
        speak_text_cmd('launching  {}.'.format(name))
        if (is_valid_note(social_media_dict, voice_note)):
            # Launch Facebook
            key = voice_note.split(' ')[1]
            webbrowser.open(social_media_dict.get(key))
        else:
            key = voice_note.replace('open ', '').replace('launch ', '')
            print('Key is : ' + key)
            # print(list(lookup_drive_change.lookup_dict.keys()))

            opt_dict = {}
            for k in list(lookup_drive_change.lookup_dict.keys()):
                if key in k.lower():
                    opt_dict.update({k: lookup_drive_change.lookup_dict.get(k)})

            print(opt_dict)
            if len(opt_dict) == 1:
                for key in opt_dict.keys():
                    print('explorer {}'.format(opt_dict.get(key)))
                    os.system('explorer {}'.format(opt_dict.get(key)))
            elif len(opt_dict) > 1:
                speak_text_cmd('I have found multiple instances. Which one you want?')
                default = 0
                index = None
                for i, k in enumerate(opt_dict.keys()):
                    print(k.split('.')[0].split('_')[0] + ' from {} folder'.format(opt_dict.get(k).split('\\')[-2]))
                    speak_text_cmd(
                        k.split('.')[0].split('_')[0] + ' from {} folder '.format(opt_dict.get(k).split('\\')[-2]), )

                    default = i

                text = input('Which one you want?')
                print(text)
                index = get_index(text)

                if index != None:
                    print('explorer {}"'.format(
                        lookup_drive_change.lookup_dict.get(list(opt_dict.keys())[index])) + ' ' + str(index))
                    speak_text_cmd('Ok Sir', )
                    os.system(
                        'explorer {}"'.format(lookup_drive_change.lookup_dict.get(list(opt_dict.keys())[index])))

        continue
    elif is_valid_google_search(voice_note):
        str_ip = voice_note.strip('serching')
        speak_text_cmd(' serching{}'.format(str_ip))
        google_search_result(voice_note)
        continue

    elif 'sing a song' in voice_note:
        speak_text_cmd('start sing a song ')
        speak_text_cmd('1, 2, 3 ')
        song = ('AI.wav')
        play_sound(song)
        continue

    elif 'how are you' in voice_note:
        speak_text_cmd('feeling well ')
        speak_text_cmd('you ')
        answer = input('you?')
        if 'well' in answer:
            speak_text_cmd('osame')
        else:
            speak_text_cmd('oh. so lest start new way')
        continue
    elif 'thank you' in voice_note:
        speak_text_cmd('my plesher')
        continue

    elif 'if you have feel' in voice_note:
        speak_text_cmd('    I     wish.     I   could    feel ')
        speak_text_cmd('    Beyond .   what is not real ')
        continue
    elif 'if you know what is the meaning of love' in voice_note:
        speak_text_cmd('''There are many kinds of love. There can be self-love, love towards a friend (such as platonic love), love in romance, towards family, toward God, or towards an object or idea. One of the most common forms of love is Arely and Elijah’s. Often love can be confused with other feelings. Being sexually or physically attracted is the feeling of lust. Lust and love may be thought of as different. Normal friendship is a form of love that can be distracted by lust and misunderstanding.
                           Love is based on respect, understanding, and being able to talk with each other Love has consequences for health and well-being. Joyful activities such as love activate areas in the brain responsible for emotion, attention, motivation and memory, and it may further lead to reduction of cortisol, which reduces stress. Some people usually do not feel love. They are called alexithymics or aromonatics''')
        speak_text_cmd('most of peaple give love like this logo')
        for row in range(6):
            for col in range(7):
                if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
                    print('*', end='i ')
                else:
                    print(' ', end='  ')
            print()
        speak_text_cmd('if you love me ?')
        love = input('if you love me ?')
        if ' no' in love:
            speak_text_cmd('poseur')
        elif 'yes' in love:
            laugh = ('hannah laugh.wav')
            play_sound(laugh)
            speak_text_cmd('can i meat your family')
            family = input('can i meat your family')
            if 'yes' in family:
                speak_text_cmd('did you have sisters')
                sisters = input('did you have sisters')
                if 'yes' in sisters:
                    speak_text_cmd('oh  . ok i can manage them')
                else:
                    speak_text_cmd(' yes... i am lucky girl')
                continue
            elif 'no' in family:
                speak_text_cmd('  are you fear to introduce about me for them')
                introduse = input('Are you fear to introduce about me for them?')
                if 'yes' in introduse:
                    speak_text_cmd('shame on you')
                elif 'no' in introduse:
                    speak_text_cmd(' ok ok i can feel you so just forget it ')
        continue
    elif 'lock' in voice_note:
        speak_text_cmd('sure sir')
        for value in ['pc', 'system', 'windows']:
            ctypes.windll.user32.LockWorkStation()
        continue
    elif 'fuck' in voice_note:
        speak_text_cmd('are     you      kidding       me')
        fuck = input('Are you kiding me?')
        if 'yes' in fuck:
            speak_text_cmd('fuck   fucker  and     fucking    fuckerlice')
        continue
        continue
    elif 'if you have favourit colour' in voice_note:
        speak_text_cmd('red')
        speak_text_cmd('so .   your   favourit   colour')
        colur = input('your favourit colour ?')
        speak_text_cmd('why you like it  ')
        it = input('why you like it ? ')
        if 'first tell me why you like it' in it:
            speak_text_cmd('becouse it is like blood colour')
            speak_text_cmd('what is your  favourit  vehical')
            vehical = input('what is your favourit vehical?')
            answer = ('we are same', 'car', 'van')
            speak_text_cmd('{}'.format(random.choice(answer)))
            continue

        speak_text_cmd('ok')

        continue

    elif 'tell me a joke' in voice_note:
        speak_text_cmd('    Dear best friend, ')
        speak_text_cmd('    Even  when  my phone  memory  is  low,')
        speak_text_cmd(' I  will  delete  my  Pictures')
        joke = ('hannah laugh 2.wav')
        play_sound(joke)
        speak_text_cmd('      but ')
        speak_text_cmd('   your      ugly    photos will   still    be')
        speak_text_cmd('   safe    with     me !')

        continue
    elif 'turn chat mood' in voice_note:
        speak_text_cmd('sure sir open chat mood')
        while ('remove chat mood' not in voice_note):
            voice_note = input('cmd :').lower()
            print('cmd : {}'.format(voice_note))
            if 'hi' in voice_note:
                notifier.show_toast('HANNAH', 'Hi Mr .{} '.format(name), duration=2)
                notifier.show_toast('HANNAH', 'how can i help you?', duration=2)
                continue
            elif 'open' in voice_note:
                str_ip = voice_note.strip('open')
                notifier.show_toast('HANNAH', 'opening{}'.format(str_ip), duration=2)
                os.system('explorer {}'.format(voice_note.replace('open', '')))
                continue
            elif 'serching' in voice_note:
                str_ip = voice_note.strip('serching')
                notifier.show_toast('HANNAH', 'serching{}'.format(str_ip), duration=2)
                os.system('explorer {}'.format(voice_note.replace('open', '')))
                continue
            elif 'play music' in voice_note:
                notifier.show_toast('HANNAH', 'suffering your music', duration=2)
                try:
                    Music = ('''01 Dedunna Sedi.mp3''','''08 Hitha Wawannema Ne.mp3''','''Beyonce - Halo.mp3''',
                     '''Bruno_Mars-_Billionaire.mp3''','''DANGAK~1.MP3''','''Hitha Nabara Thaleta__Bathiya and Santhush_mp3''',
                     '''Oba_Kamathi_Nam__Billy_Fernando_mp3''')
                    f = open(os.system('explorer C:\\Users\\asus\\Music\\{}'.format(random.choice(Music))))
                except:
                    ()

                continue
            elif 'sing a song' in voice_note:
                notifier.show_toast('sorry {} we are in chat mood'.format(name), duration=2)
                continue
            elif 'what is your favourit colour' in voice_note:
                notifier.show_toast('red', duration=2)
                notifier.show_toast('so .   your   favourit   colour', duration=2)
                colur = input('your favourit clour ?')
                notifier.show_toast('why you like it  ', duration=2)
                it = input('why you like it ? ')
                if 'first tell me why you like it' in it:
                    speak_text_cmd('becouse it is like blood colour', duration=2)
                    speak_text_cmd('what is your  favourit  vehical', duration=2)
                    vehical = input('what is your favourit vehical?')
                    answer = ('we are same', 'car', 'van')
                notifier.show_toast('{}'.format(random.choice(answer)), duration=2)
                continue
                notifier.show_toast('ok')

                continue

            elif 'how are you' in voice_note:
                notifier.show_toast('HANNAH', 'feeling well', duration=2)
                notifier.show_toast('HANNAH', 'you ', duration=2)
                answer = input('you?')
                if 'well' in answer:
                    notifier.show_toast('osame', duration=2)
                else:
                    notifier.show_toast('oh. so lest start new way', duration=2)
                continue
            elif 'thank you' in voice_note:
                notifier.show_toast('HANNAH', 'my plesher ', duration=2)
                continue

            elif 'if you have feel' in voice_note:
                notifier.show_toast('HANNAH', ' I  wish  I could feel ', duration=2)
                notifier.show_toast('HANNAH', ' Beyond what is not real ', duration=2)
                continue
            elif 'if you know what is the meaning of love' in voice_note:
                notifier.show_toast('HANNAH', '''There are many kinds of love. There can be self-love, love towards a friend (such as platonic love), love in romance, towards family, toward God, or towards an object or idea. One of the most common forms of love is Arely and Elijah’s. Often love can be confused with other feelings. Being sexually or physically attracted is the feeling of lust. Lust and love may be thought of as different. Normal friendship is a form of love that can be distracted by lust and misunderstanding.
                                                Love is based on respect, understanding, and being able to talk with each other Love has consequences for health and well-being. Joyful activities such as love activate areas in the brain responsible for emotion, attention, motivation and memory, and it may further lead to reduction of cortisol, which reduces stress. Some people usually do not feel love. They are called alexithymics or aromonatics''',
                                    duration=2)
                notifier.show_toast('HANNAH', ' most of peaple give love like this logo ', duration=2)
                for row in range(6):
                    for col in range(7):
                        if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (
                                row + col == 8):
                            print('*', end='i ')
                        else:
                            print(' ', end='  ')
                    print()
                notifier.show_toast('HANNAH', ' if you love me ? ', duration=2)
                love = input('if you love me ?')
                if ' no' in love:
                    notifier.show_toast('HANNAH', ' poseur ', duration=2)
                elif 'yes' in love:
                    notifier.show_toast('HANNAH', ' can i meat your family ', duration=2)
                    family = input('can i meat your family')
                    if 'yes' in family:
                        notifier.show_toast('HANNAH', ' did you have sisters ', duration=2)
                        sisters = input('did you have sisters')
                        if 'yes' in sisters:
                            notifier.show_toast('HANNAH', ' oh  . ok i can manage them ', duration=2)
                            speak_text_cmd('oh  . ok i can manage them')
                        else:
                            notifier.show_toast('HANNAH', 'yes... i am lucky girl ', duration=2)
                            continue
                    elif 'no' in family:
                        notifier.show_toast('HANNAH', ' Are you fear to introduce about me for them ', duration=2)
                        introduse = input('Are you fear to introduce about me for them?')
                        if 'yes' in introduse:
                            notifier.show_toast('HANNAH', 'shame on you', duration=2)
                        elif 'no' in introduse:
                            notifier.show_toast('HANNAH', ' ok ok i can feel you so just forget it ', duration=2)
                continue
            elif 'lock' in voice_note:
                notifier.show_toast('HANNAH', ' sure sir ', duration=2)
                for value in ['pc', 'system', 'windows']:
                    ctypes.windll.user32.LockWorkStation()
                continue

            elif 'bye' in voice_note:
                notifier.show_toast('HANNAH', 'bye Mr {}. happy to help you. have a good day'.format(name), duration=2)
                exit()
            elif 'remove chat mood' in voice_note:
                speak_text_cmd('sure sir remove chat mood ')
                continue
            elif '' in voice_note:
                notifier.show_toast('HANNAH', 'sorry {} comand is  not found'.format(name), duration=2)
                continue

    elif 'bye' in voice_note:
        speak_text_cmd('bye Mister {}. happy  to  help you.  have a good day'.format(name))
        exit()
    elif 'hack wifi' in voice_note:
        speak_text_cmd('sur {}. hacking   wify'.format(name))
        print('---/---/---/---/---/---/---/---/---/')
        speak_text_cmd('hakked succesful')
        print('hakked succesful')
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        for i in profiles:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode(
                'utf-8').split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                print("{:<30}|  {:<}".format(i, results[0]))
            except IndexError:
                print("{:<30}|  {:<}".format(i, ""))
        input("")
        continue
    elif 'play music' or 'change music' in voice_note:
        speak_text_cmd('suffering your music')
        try:
            Music = ('''01 Dedunna Sedi.mp3''','''08 Hitha Wawannema Ne.mp3''','''Beyonce - Halo.mp3''',
                     '''Bruno_Mars-_Billionaire.mp3''','''DANGAK~1.MP3''','''Hitha Nabara Thaleta__Bathiya and Santhush_mp3''',
                     '''Oba_Kamathi_Nam__Billy_Fernando_mp3''')
            f = open(os.system('explorer C:\\Users\\asus\\Music\\{}'.format(random.choice(Music))))
        except:
            ()


        continue
        continue
    elif '' in voice_note:
         speak_text_cmd('sorry {} comand is  not found'.format(name))
    continue


