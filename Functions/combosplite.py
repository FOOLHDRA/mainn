import os
import time



def pathh(inpath) : 
    global path
    os.system('cls')
    data_file = input("""


    \033[1;32mPlease Enter the Combo splitid by ':'
    \033[1;30mexemple : (email@email.com:password)

    \033[1;32mThanck you For Buying The Key and Welcome  :)


    \033[1;36m>> Please Enter The Combo (Ex : File.txt) : """) # hda 4ir lfile 
    path = (inpath + '\\' + data_file) # hada lpath + lfile 
    return path # hada lpath m3a lfile data.txt

def df():
    if os.path.exists('Result/Combo_To_Emaillist/') :
        return
    else:
        os.makedirs('Result/Combo_To_Emaillist/')





def starrt():
    with open(path , 'r') as file:
        
        ff = (file.readline())
        with open('Result/Combo_To_Emaillist/Emaillist.txt' , 'w+') as f:
            ask = input('''
            
    Combo splited with ? ( ; / : / . ) =   ''')
            try :
                while ff != '':
                    li , l = ff.split(ask,1)
                    if li :
                        f.write(str(li) + '\n')
                        ff = (file.readline())
            except Exception as fj :
                    print(' << Error Found .. >>')
                    return
            print('''
            
            Done ...

            Output :  /Result/Combo_To_Emaillist/Emaillist.txt
           
           
            ''')
            global re
            re = 1

def start_file(o):
    try :   
        if re == 1 :
            r = o + '\\Result\\Combo_To_Emaillist\\Emaillist.txt'
            os.startfile(r)
            telll()
    except : 
        pass


def telll(NNNN = 0,hhhh = 0):  
    os.system('cls')
    pr = input('''





       [1] Get Back To the Tool 



        Please choose One Number [x] :  ''')  
    if pr == '1':
        NNNN
    else : 
        os.system('exit')





