import os
import time
import random
import mechanize



# CHECK IF FILE EXIST
def aol_path():
    path = 'Result/Aol_Validator/'
    if os.path.exists(path) and os.path.exists(f'{path}Aol_Invalid.txt') :
           os.remove(f'{path}Aol_Invalid.txt')
           os.remove(f'{path}Aol_Valid.txt')
           return
    else:
        if os.path.exists(path):
            pass
        else :     
            os.makedirs(path)





# START CHECKING

def valid(count,pathx,rm):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.set_proxies({"http": "43.255.113.232:85"})
    Headears = [
    ('User-Agent','Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36 EdgA/107.0.1418.62'),
    ('User-Agent','Mozilla/5.0 (Linux; Android 12; M2101K7AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Mobile Safari/537.36 EdgA/104.0.1293.47'),
    ('User-Agent','Deezer/6.2.22.90 (Android; 10; Mobile; en) HUAWEI CDY-NX9A'),
    ('User-Agent','Deezer/6.2.21.90 (Android; 10; Mobile; us) OnePlus GM1915'),
    ('User-Agent','Deezer/6.2.22.90 (Android; 10; Mobile; nl) HUAWEI JNY-LX1'),
    ('User-Agent','Deezer/6.2.23.93 (Android; 10; Mobile; uk) HUAWEI MAR-LX1M')]
    browser.addheaders= [random.choice(Headears)]
    browser.open('https://login.aol.com/', timeout=5)
    browser.select_form(nr=0)

    medd = (pathx +'\\'+ rm)
    with open(medd , 'r+') as fe:
        tr = fe.readlines()

    browser.form['username'] =  tr[count]
    

    sub = browser.submit()
    tam = (sub.geturl())



    if count != -1  :
        if 'recaptcha?' in tam :
            with open('Result/Aol_Validator/Aol_Valid.txt','a') as gmal:
                gmal.write(tr[count])
                pass
            print('  ','\033[1;32m    [Valid email]  ====>   \033[1;0m',tr[count].strip() ,)


        else : 
            print ('  ','\033[1;31m   [Invalid email] ====>   \033[1;0m',tr[count].strip())
            with open('Result/Aol_Validator/Aol_Invalid.txt','a') as gmail:
                gmail.write(tr[count])
                pass



