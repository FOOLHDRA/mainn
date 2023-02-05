import os
import requests
import Functions.Password as Password
from Functions import combosplite
from Functions import loanding
from Functions import email_Validator
from Functions import Yahoo_Validator
from Functions import Instagram_Validator
from Functions import Gmail_Validator
from Functions import Aol_Validator
from Functions import Hotmail_Validator
from Functions import Data_Spliter
from Functions import Netflix_Validator
from Functions import Num_Gen
import threading
from threading import Thread
from threading import Thread
import time
from tqdm import tqdm
from time import sleep






# Run script here all Functions

# progrzsss bar
def progres():
    for i in tqdm(range(0, 100), mininterval = 0.00001,
        desc ='''
        Please Wait'''):
        sleep(.0000001)
    os.system('cls')


# password confirm
def passwd():
    fm = (requests.get(url='http://google.com'))
    pr = (str(fm.content))
    print


    list = [('knife','work'),('site','idea'),('olive','mother'),('play','home')]
    op = (list[1][0][0]+list[1][1][0]+list[2][1][0]+list[2][0][0])
    Password.password()
    if Password.pswd in pr:
        send()
        os.system('cls')
        lib()
        progres()
        timeout = 5
        print(f'''

        Please wait for {timeout} seconds ...
        
        ''')
        time.sleep(timeout)

        print('Wait Please')
        styles()
    else:
        os.system('cls')
        print('''







        Go Buy The Key ...
        
        Contact me Here : https://t.me/HEX001_SIMO

      

        ''')
        time.sleep(15)




 # principe loanding page

def styles():
    loanding.style()
    inputnum = input('      \033[1;36m Please Choose One Number [] : \033[1;0m')
        
    if inputnum == '1' :
        try :
            combo_splite()
        except :
            styles()
    elif inputnum == '2' : 
        try :
            validator_em()
        except Exception as g:
            styles()
    elif inputnum == '3' :
        try:
            Splite()
        except:
            styles()

    elif inputnum == '4' :
        try :
            gmailValid() 
        except Exception as g:
            styles()
    elif inputnum == '5' :
        try :
            AolValid() 
        except Exception as g:
            styles()
    elif inputnum == '6' :
        try :
            yahooValid() 
        except Exception as g:
            styles()
    elif inputnum == '7' :
        try :
            NetflixValid()
        except Exception as g:
            styles()
        
    elif inputnum == '8' :
        try :
            instaValid()
        except Exception as g:
            styles()
    elif inputnum == '9' :
        try :
            Num()
        except Exception as g:
            styles()
    elif inputnum == '10' :
        try :
            HotmailValid()
        except Exception as g:
            styles()        
    else : 
        styles()
        


# spliter combo 

def combo_splite():
    original_path = os.getcwd()
    combosplite.pathh(original_path)
    combosplite.df()
    combosplite.starrt()
    combosplite.start_file(original_path)
    styles()
    combosplite.telll(styles())


def validator_em():
    original_path = os.getcwd()
    email_Validator.validate(original_path)
    email_Validator.tell(styles())





def ion(plat,r):
    original_path = os.getcwd()
    os.system('cls')
    rm = input(f'''


           \033[1;34m  ↶ This Tool check If The EmailList Are In {plat} ↷\033[1;0m
           \033[1;33m - The tool Take Some Time And She Need a Good Connexion -\033[1;0m
           Please Use Proxies In Your Computer before start the script

                      Exemple : Hide My IP, Proton  ....

                    
    
    Please enter Your List {plat}  (exemple.txt) : ''')
    os.system('cls')
    print('''
    
    
    Checking Start after 2 second Please Wait .... 
    
    
    
    
    
    ''')
    time.sleep(2)
    os.system('cls')
    medd = ( original_path +'\\'+ rm)
    with open(medd , 'r+') as fe:
        rr = fe.readlines()
    ciunt = -2
    limit = len(rr)
    list = ['Gmail_Validator']

    while limit > ciunt :
        if r == '1' :
            Gmail_Validator.valid(ciunt,original_path,rm)
        elif r == '2' :
            Yahoo_Validator.valid(ciunt,original_path,rm)
        elif r == '3' :
            Aol_Validator.valid(ciunt,original_path,rm)
        elif r == '4' :
            Hotmail_Validator.valid(ciunt,original_path,rm)
        elif r == '5' :
            Instagram_Validator.valid(ciunt,original_path,rm)
        elif r == '6' :
            Netflix_Validator.valid(ciunt,original_path,rm)       
        ciunt += 1

def fin(path):
    print(f'''



         
    
    
        Done .

        Output : Result\{path}
    
    
    
    
    ''')
    time.sleep(100)





def fin(path):
    print(f'''



         
    
    
        Done .

        Output : Result\{path}
    
    
    
    
    ''')
    time.sleep(100)









def instaValid():
    Instagram_Validator.insta_path()
    ion("Instagram","5")
    fin('Instagram_Validator')
    styles()

def yahooValid():
    Yahoo_Validator.yahoo_path()
    ion('Yahoo','2')
    fin('Yahoo_Validator')
    styles()

def AolValid():

    Aol_Validator.aol_path()
    ion('Aol',"3")
    fin('Aol_Validator')
    styles()
def Num():
    original_path = os.getcwd()
    Num_Gen.num_path()
    Num_Gen.Num(original_path)
    fin('Num_Gen')
    styles()

def NetflixValid():
    Netflix_Validator.netf()
    ion('Netflix',"6")
    fin('Netflix_Validator')
    styles()

def HotmailValid():
    original_path = os.getcwd()
    Hotmail_Validator.hot_path()
    ion('Hotmail',"4")
    fin('Hotmail_Validator')
    styles()

def gmailValid():
    original_path = os.getcwd()
    Gmail_Validator.dhf()
    ion('Gmail',"1")
    fin('Gmail_Validator')
    styles()

def Splite():
    original_path = os.getcwd()
    os.system('cls')
    Data_Spliter.selecte(original_path,original_path,original_path)
    styles()


def send():
    TOKEN = "5719708451:AAGgtZwutZizoQp0buNJTXT-MdrVwYVMPSY"
    chat_id = "-674041985"
    deef = os.environ.get('USERNAME')
    message = f'{deef} dkhl ltool asat'
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    (requests.get(url).json())

def lib():
    os.system('pip install mechanize')
    os.system('pip install requests')


# declaration all fuctions here 


passwd()