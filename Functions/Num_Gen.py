import random as r
import os




def num_path():
    path = 'Result/Num_Generator/'
    if os.path.exists(path) and os.path.exists(f'{path}Number Generated.txt') :
            try : 
                os.remove(f'{path}Number Generated.txt')
                return
            except:
                pass
    else:
        if os.path.exists(path):
            pass
        else :     
            os.makedirs(path)



def Num(path):
    os.system('cls')
    count = 0
    print('''
    
    -----------------------------------------------------------------------------------------------
    |                                                                                             |
    |                                                                                             |
    |     \033[1;34mNUMBER PHONE :     +1            [][][]            [][][][][][][]  \033[1;0m                     |
    |                                                                                       \033[1;0m      |
    |           \033[1;34m              ↑       |       ↑        |           ↑              \033[1;0m                |
    |         \033[1;34m              Fisrt     |     Area       |      Number After          \033[1;0m              |
    |           \033[1;34m            Number    |     Number     |       area code          \033[1;0m                |
    |                                                                                             |
    |                                                                                             |
    |                                                                                             |
    |     \033[1;33mexemple (maroc) :       0            6            54823569        \033[1;0m                      |
    |           \033[1;33m                                                                   \033[1;0m               |
    |          \033[1;33m           ||      ↑     |      ↑      |        ↑          ||       \033[1;0m               |
    |           \033[1;33m          ||    First   |     Area    |   Number After    ||       \033[1;0m               |
    |           \033[1;33m          ||     Num    |     code    |    area code      ||        \033[1;0m              |
    |\033[1;0m                                                                                             |
    |           \033[1;32mResult : 0654823569 \033[1;0m                                                              |
    |                                                                                             |
    |                Output : /Result/PhoneNumber                                                 |
    |                                                                                             |
    -----------------------------------------------------------------------------------------------
    
    ''')
    num = input('  >>>    First number : ')
    area = input('  >>>    Area Code : ')
    nudm = input('  >>>    Number After the Area Code (7-8-9-10-11-12) : ')
    limit = input('  >>>    How Much Number You Want (Max:100000): ')
    if limit :
        pass
    else :
        limit = 1000
    if area :
        pass
    else :
        area = 1
    if num :
        pass
    else :
        num = 1

    rm = int(limit)



    while rm > count :
        if nudm == '7':
            op = (f'{num}{area}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}')
            with open('Result/Num_Generator/Number Generated.txt','a') as gmal:
                gmal.write(op)
                gmal.write('\n')
            print(f'{num}{area}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}')
        
        if nudm == '8':
            op = (f'{num}{area}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}')
            with open('Result/Num_Generator/Number Generated.txt','a') as gmal:
                gmal.write(op)
                gmal.write('\n')            
            print(f'{num}{area}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}')
        
        elif nudm == '9':
            op = (f'{num}{area}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}')
            with open('Result/Num_Generator/Number Generated.txt','a') as gmal:
                gmal.write(op)
                gmal.write('\n')
            print(f'{num}{area}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}')
        
        elif nudm == '10':
            op = (f'{num}{area}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}')
            with open('Result/Num_Generator/Number Generated.txt','a') as gmal:
                gmal.write(op)
                gmal.write('\n')
            print(f'{num}{area}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}')
        
        elif nudm == '11':
            op = (f'{num}{area}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}')
            with open('Result/Num_Generator/Number Generated.txt','a') as gmal:
                gmal.write(op)
                gmal.write('\n')
            print(f'{num}{area}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}')
        
        elif nudm == '12':
            op = (f'{num}{area}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}')
            with open('Result/Num_Generator/Number Generated.txt','a') as gmal:
                gmal.write(op)
                gmal.write('\n')
            print(f'{num}{area}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}{r.randint(2,8)}')
        count += 1

            


