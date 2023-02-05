import os
import time
import random
import requests
import mechanize


# CHECK IF FILE EXIST
def insta_path():
    path = 'Result/Instagram_Validator/'
    if os.path.exists(path) and os.path.exists(f'{path}Instagram_Invalid.txt') :
            try : 
                os.remove(f'{path}Instagram_Invalid.txt')
                os.remove(f'{path}Instagram_Valid.txt')
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
    ('Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36 EdgA/107.0.1418.62'),
    ('Mozilla/5.0 (Linux; Android 12; M2101K7AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Mobile Safari/537.36 EdgA/104.0.1293.47'),
    ('Deezer/6.2.22.90 (Android; 10; Mobile; en) HUAWEI CDY-NX9A'),
    ('Deezer/6.2.21.90 (Android; 10; Mobile; us) OnePlus GM1915'),
    ('Deezer/6.2.22.90 (Android; 10; Mobile; nl) HUAWEI JNY-LX1'),
    ('Deezer/6.2.23.93 (Android; 10; Mobile; uk) HUAWEI MAR-LX1M')]
    r= random.choice(Headears)
    headekrs = {
    'User-Agent': f'{r}',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-CSRFToken': 'missing',
    'X-Instagram-AJAX': 'c6412f1b1b7b',
    'X-IG-App-ID': '936619743392459',
    'X-ASBD-ID': '198387',
    'X-IG-WWW-Claim': '0',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://www.instagram.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://www.instagram.com/accounts/password/reset/',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'csrftoken=9e7U8qRNqAbazRC0kwrRgyN2okh1kihx; mid=YsM1_AALAAEG2fGCvkPXE5DVlJD0; ig_did=494394E2-A583-4F01-BC32-5E4344FE2C4D',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
    }
    r = requests.session()

    url = "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/"
    r = r.post(url,data={'email_or_username':f'{tr[count]}'},headers=headekrs)

    time.sleep(5)

    if count != -1  :
        if '/challenge/' in r.text :
            with open('Result/Instagram_Validator/Instagram_Valid.txt','a') as gmal:
                gmal.write(tr[count])
                pass
            print( '   ',tr[count].strip() ,'\033[1;32m    =====>>>  Valid email\033[1;0m')


        else : 
            print ('   ', tr[count].strip() ,'\033[1;31m   =====>>>  Invalid email\033[1;0m')
            with open('Result/Instagram_Validator/Instagram_Invalid.txt','a') as gmail:
                gmail.write(tr[count])
                pass



