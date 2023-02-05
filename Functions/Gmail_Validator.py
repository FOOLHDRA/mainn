import os
import time
import random
import mechanize



# CHECK IF FILE EXIST
def dhf():
    path = 'Result/Gmail_EmailValidator/'
    if os.path.exists(path) and os.path.exists(f'{path}Gmail_Invalid.txt') :
           os.remove(f'{path}Gmail_Invalid.txt')
           os.remove(f'{path}Gmail_Valid.txt')
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
    Headears = [
    ('User-Agent','Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36 EdgA/107.0.1418.62'),
    ('User-Agent','Mozilla/5.0 (Linux; Android 12; M2101K7AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Mobile Safari/537.36 EdgA/104.0.1293.47'),
    ('User-Agent','Deezer/6.2.22.90 (Android; 10; Mobile; en) HUAWEI CDY-NX9A'),
    ('User-Agent','Deezer/6.2.21.90 (Android; 10; Mobile; us) OnePlus GM1915'),
    ('User-Agent','Deezer/6.2.22.90 (Android; 10; Mobile; nl) HUAWEI JNY-LX1'),
    ('User-Agent','Deezer/6.2.23.93 (Android; 10; Mobile; uk) HUAWEI MAR-LX1M')]
    browser.addheaders= [random.choice(Headears)]
    browser.open('https://accounts.google.com/')
    browser.select_form(nr=0)

    medd = (pathx +'\\'+ rm)
    with open(medd , 'r+') as fe:
        tr = fe.readlines()

    browser.form['identifier'] =  tr[count]
    

    sub = browser.submit()
    tam = (sub.geturl())



    if count != -1  :
        if '/rejected' in tam :
            with open('Result/Gmail_EmailValidator/Gmail_Valid.txt','a') as gmal:
                gmal.write(tr[count])
                pass
            print( '   ',tr[count].strip() ,'\033[1;32m    =====>>>  Valid email\033[1;0m')


        else : 
            print ('   ', tr[count].strip() ,'\033[1;31m   =====>>>  Invalid email\033[1;0m')
            with open('Result/Gmail_EmailValidator/Gmail_Invalid.txt','a') as gmail:
                gmail.write(tr[count])
                pass



