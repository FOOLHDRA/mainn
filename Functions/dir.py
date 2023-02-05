import os
import time
import random
import requests
import mechanize


# # START CHECKING

# def valid():
#     # browser = mechanize.Browser()
#     # browser.set_handle_robots(False)
#     # browser.set_handle_equiv(False)
#     proxies = {
#    'http': '87.159.111.178:80',
#     } 
#     Headears = [
#     ('User-Agent','Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36 EdgA/107.0.1418.62'),
#     ('User-Agent','Mozilla/5.0 (Linux; Android 12; M2101K7AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Mobile Safari/537.36 EdgA/104.0.1293.47'),
#     ('User-Agent','Deezer/6.2.22.90 (Android; 10; Mobile; en) HUAWEI CDY-NX9A'),
#     ('User-Agent','Deezer/6.2.21.90 (Android; 10; Mobile; us) OnePlus GM1915'),
#     ('User-Agent','Deezer/6.2.22.90 (Android; 10; Mobile; nl) HUAWEI JNY-LX1'),
#     ('User-Agent','Deezer/6.2.23.93 (Android; 10; Mobile; uk) HUAWEI MAR-LX1M')]

#     headekrs = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
#     'Accept': '*/*',
#     'Accept-Language': 'en-US,en;q=0.5',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     'X-CSRFToken': '9e7U8qRNqAbazRC0kwrRgyN2okh1kihx',
#     'X-Instagram-AJAX': 'c6412f1b1b7b',
#     'X-IG-App-ID': '936619743392459',
#     'X-ASBD-ID': '198387',
#     'X-IG-WWW-Claim': '0',
#     'X-Requested-With': 'XMLHttpRequest',
#     'Origin': 'https://www.instagram.com',
#     'DNT': '1',
#     'Connection': 'keep-alive',
#     'Referer': 'https://www.instagram.com/accounts/password/reset/',
#     # Requests sorts cookies= alphabetically
#     # 'Cookie': 'csrftoken=9e7U8qRNqAbazRC0kwrRgyN2okh1kihx; mid=YsM1_AALAAEG2fGCvkPXE5DVlJD0; ig_did=494394E2-A583-4F01-BC32-5E4344FE2C4D',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-origin',
#     # Requests doesn't support trailers
#     # 'TE': 'trailers',
#     }
    
#     url = "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/"
#     r = requests.post(url,data={'email_or_username':'gfhgfh'},headers=headekrs,proxies=proxies)
#     print(r.text)





# # # START CHECKING

# def valid():
#     browser = mechanize.Browser()
#     browser.set_handle_robots(False)
#     browser.set_handle_referer(True)
#     browser.set_handle_equiv(True)

#     Headears = [
#     ('User-Agent','Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36 EdgA/107.0.1418.62'),
#     ('User-Agent','Mozilla/5.0 (Linux; Android 12; M2101K7AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Mobile Safari/537.36 EdgA/104.0.1293.47'),
#     ('User-Agent','Deezer/6.2.22.90 (Android; 10; Mobile; en) HUAWEI CDY-NX9A'),
#     ('User-Agent','Deezer/6.2.21.90 (Android; 10; Mobile; us) OnePlus GM1915'),
#     ('User-Agent','Deezer/6.2.22.90 (Android; 10; Mobile; nl) HUAWEI JNY-LX1'),
#     ('User-Agent','Deezer/6.2.23.93 (Android; 10; Mobile; uk) HUAWEI MAR-LX1M')]
#     browser.addheaders= [random.choice(Headears)]
#     browser.open('https://login.aol.com/', timeout=5)

#     browser.select_form(nr=0)
#     browser.form['username'] =  "notbustamante@hotmail.com"
    

#     sub = browser.submit()
#     tam = (sub.geturl())

#     if 'recaptcha?' in tam :
#         print ('good')
#     else:
#        print('Not Found')
#     print(tam)







    # browser.addheaders= [random.choice(Headears)]

    # browser.open('https://www.instagram.com/accounts/password/reset/', timeout=5)
    # browser.select_form(nr=0)


    # browser.form['cppEmailOrUsername'] =  'decointext'
    

    # sub = browser.submit()
    # tam = (sub.geturl())
    # if 'recaptcha?' in tam :
    #     print ('good')
    # else:
    #    print('Not Found')
    # print(tam)






# valid()

what = input('number of line in one file  :')



lines_per_file = int(what)
print(lines_per_file)
smallfile = None
with open('really_big_file.txt') as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = 'small_file_{}.txt'.format(lineno + lines_per_file)
            smallfile = open(small_filename, "w")
        smallfile.write(line)
    if smallfile:
        smallfile.close()



