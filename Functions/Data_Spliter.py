import os 
import time



def paths():
    path = 'Result/Data_Spliter_To_2/'
    if os.path.exists(path) and os.path.exists(f'{path}DataSplited1.txt') :
            try : 
                os.remove(f'{path}DataSplited1.txt')
                os.remove(f'{path}DataSplited2.txt')
                return
            except:
                pass
    else:
        if os.path.exists(path):
            pass
        else :     
            os.makedirs(path)























def pathc():
    path = 'Result/Data_Cleaner/'
    if os.path.exists(path) and os.path.exists(f'{path}DataClean.txt') :
            try : 
                os.remove(f'{path}DataClean.txt')
                return
            except:
                pass
    else:
        if os.path.exists(path):
            pass
        else :     
            os.makedirs(path)






def path_f():
    path = 'Result/Spam_Trap_Cleaner/'
    if os.path.exists(path) and os.path.exists(f'{path}SpamTrap_Found.txt') :
            try : 
                os.remove(f'{path}DataClean_Without_Spamtrap.txt')
                os.remove(f'{path}SpamTrap_Found.txt')
                return
            except:
                pass
    else:
        if os.path.exists(path):
            pass
        else :     
            os.makedirs(path)
















def s(pathss):

    path = input("""
    
    Please Enter Your DateFile (exemple.txt) : """)
    os.system('cls')
    inaa = (pathss + '\\' + path)
    with open(inaa,'r+')as f :
        pf = f.writelines('\n')
        pf = (f.readlines())
    count = 0
    limit = len(pf)
    pathx = input("""
    
    Please Enter Your SpamtTrapFile (exemple.txt) : """)
    ina = (pathss + '\\' + pathx)

    while limit > count :
# GIVE A PRAMETRE A DEF CLEAN(EMAIL, NUMBUR[0,1])
        clean(pf,count,ina)
        count += 1
    check(inaa)



# DEF CLEAN WITH PF AND COUNETR NUMBER
def clean(pf,count,path):

    with open(path,'r+')as fd : #OPNING THE SPAM TRAP FILE 
        pd = fd.writelines('\n')
        pd = (fd.readlines())

    con = 0
    lim = len(pd)
    while lim > con :
        if pf[count] in pd[con]:
            with open('Result/Spam_Trap_Cleaner/SpamTrap_Found.txt','a+')as fl : # ADD THE SPAM TRAP TO VALIDSPAMTRAP.TXT
                fl.writelines(pd[con])
        con += 1
    


def check(inaa):
    with open(inaa, "r") as file1:
        lines_file1 = file1.readlines()
    try : 
        with open('Result/Spam_Trap_Cleaner/SpamTrap_Found.txt', "r") as file2:
            lines_file2 = file2.readlines()
        with open('Result/Spam_Trap_Cleaner/DataClean_Without_Spamtrap.txt', "w") as f_w:
            for line  in lines_file1:
                if line not in lines_file2:
                    f_w.write(line)
        print('''
    Done.. 

    Data Cleaned From SpamTrap in /Result/Spam_Trap_Cleaner/DataClean_Without_Spamtrap.txt

    ''')
    except:
        os.system('cls')
        print('''
        
        
        NO Spam Trap Found in This List
        
        ''')












def pathsx():
    path = 'Result/Data_Spliter_ByLine/'
    if os.path.exists(path) :
        pass
    else:
        os.makedirs(path)




def Splite(path):
    name = input('''
    


         \033[1;33mPlease Enter The File To split it : \033[1;0m''')
    pathx = (path + '\\' + name)
    data1 = (path + '\\Result\Data_Spliter_To_2\DataSplited1.txt')
    data2 = (path + '\\Result\Data_Spliter_To_2\DataSplited2.txt')
    with open(pathx,'r+') as sp:
        tab = sp.readlines()

        count = 0
        limit = len(tab)
        print('''
        
        Please Wait ....
        
        ''')
    
        while limit >= count :
            if (int(limit/2)) > count:
                with open(data1 ,'a') as sp:
                    sp.writelines(str(tab[count]))
            else :
                try : 
                    with open(data2 ,'a') as sp:
                        sp.writelines(str(tab[count]))
                except:
                    pass

            count +=1
    os.system('cls')
    print('''
    
    
    Done ...



    The Tool close After 10s

    ''')

    time.sleep(10)

def Lines(pathh):
    name = input('''
    


         \033[1;33m Please Enter The File To split it (exemple.txt) : \033[1;0m''')
    pathxx = (pathh + '\\' + name)
    os.system('cls')

    what = input(f'''




    \033[1;34m      - If File Are Large up to 1Million Line Select Between (100000-500000)\033[1;0m

    \033[1;34m      - If File Are Small or Moyenne  Select Between           (1000-5000)\033[1;0m


    \033[1;32m          OUTPUT IN : {pathh}Result\\Data_Spliter_ByLine\\ \033[1;0m





    \033[1;33mNumber Of Line in One File  : \033[1;0m''')

    lines_per_file = int(what)
    print(lines_per_file)
    smallfile = None
    with open(pathxx) as bigfile:
        for lineno, line in enumerate(bigfile):
            if lineno % lines_per_file == 0:
                if smallfile:
                    smallfile.close()
                small_filename = f'Result/Data_Spliter_ByLine/{name}_small_file_{lineno + lines_per_file}.txt'
                smallfile = open(small_filename, "w")
            smallfile.write(line)
        if smallfile:
            smallfile.close()
    print('''
    
    
    Done ...


    Press Enter To Back To Tools
    ''')

    time.sleep(10)
            

def selecte(pathh,path,pathss):
    chose = input("""

    



           \033[1;33m[1] For Splite The File To Two Files \033[1;0m

           \033[1;33m[2] For Splite The File To Number Of Lines \033[1;0m

           \033[1;33m[3] Remove All SpamTrap From EmailList  \033[1;0m




            \033[1;37mPlease choose One Option : \033[1;0m""")
    if chose == '1':
        os.system('cls')
        paths()
        Splite(path)
    if chose == '2':
        os.system('cls')
        Lines(pathh)
        pathsx()
    if chose == '3':
        os.system('cls')
        path_f()
        s(pathss)
        




