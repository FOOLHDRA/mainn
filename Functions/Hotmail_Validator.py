import os
import time
import random
import requests


# CHECK IF FILE EXIST
def hot_path():
    path = 'Result/Hotmail_Validator/'
    if os.path.exists(path) and os.path.exists(f'{path}Hotmail_Invalid.txt') :
            try : 
                os.remove(f'{path}Hotmail_Invalid.txt')
                os.remove(f'{path}Hotmail_Valid.txt')
                return
            except:
                pass
    else:
        if os.path.exists(path):
            pass
        else :     
            os.makedirs(path)





# START CHECKING

def valid(count,pathx,rm):



    medd = (pathx +'\\'+ rm)
    with open(medd , 'r+') as fe:
        tr = fe.readlines()
    Headears = [
    {'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36 Edg}A/107.0.1418.62'},
    {'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2101K7AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Mobile Safari/537.36 EdgA/104.0.1293.47'},
    {'User-Agent': 'Deezer/6.2.22.90 (Android; 10; Mobile; en) HUAWEI CDY-NX9A'},
    {'User-Agent': 'Deezer/6.2.21.90 (Android; 10; Mobile; us) OnePlus GM1915'},
    {'User-Agent': 'Deezer/6.2.22.90 (Android; 10; Mobile; nl) HUAWEI JNY-LX1'},
    {'User-Agent': 'Deezer/6.2.23.93 (Android; 10; Mobile; uk) HUAWEI MAR-LX1M'}]
    red = random.choice(Headears)

    url = "https://login.live.com/"
    r = requests.post(url,data={'username' :f'{tr[count].strip()}'},headers=red)


    if count != -1  :
        if '"IfExistsResult":0' in r.text :
            with open('Result/Hotmail_Validator/Hotmail_Valid.txt','a') as gmal:
                gmal.write(tr[count])
                pass
            print( '   ',tr[count].strip() ,'\033[1;32m    =====>>>  Valid email\033[1;0m')


        else : 
            print ('   ', tr[count].strip() ,'\033[1;31m   =====>>>  Invalid email\033[1;0m')
            with open('Result/Hotmail_Validator/Hotmail_Invalid.txt','a') as gmail:
                gmail.write(tr[count])
                pass





