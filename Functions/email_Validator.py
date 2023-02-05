import os 
import re
import time




def func(value):
    return ''.join(value.splitlines())

def drrf():
    if os.path.exists('Result/Email_Validator/') :
        return
    else:
        os.makedirs('Result/Email_Validator/')



def validate(path):
    drrf()
    os.system('cls')
    assk = input(""" 
    
    
    Please Enter The Emaillist (exemple.txt) : """)
    drrf()
    pathx = path + "\\" + assk
    with open(pathx , 'r') as f :
        bf = f.readline()
        print('''
        
        the Validation Start after 5 secondes ... 
        
        ''')
        time.sleep(5)

        # while bf != '' :
        #     obj = re.search(r'[\w.]+\@[\w.]+', bf ) 
        #     with open('Result/Email_Validator/ValidEmail.txt',"a") as fol:
        #         fol.write(bf)
        #     bf = f.readline()

        while bf != '' :
            obj = re.search(r'[\w.]+\@[\w.]+', bf ) 
            if obj:
                print(func(bf),"\033[1;32m   ====> Valid Email \033[1;0m")
                with open('Result/Email_Validator/ValidEmail.txt',"a") as fol:
                    fol.write(bf)
            else : 
                print (func(bf), '\033[1;31m ====> Not Valid \033[1;0m')
                with open('Result/Email_Validator/FakeEmail.txt',"a") as fol:
                    fol.write(bf)
            bf = f.readline()
    print('''

    [1] Get Back To The Tool

    ''')
    global pr
    pr = input('''

        Please choose One Number [x] :  ''')
    print(pr)

def tell(NNNN,hhhh):    
    if pr == '1':
        NNNN
    else : 
        pass


    
        
