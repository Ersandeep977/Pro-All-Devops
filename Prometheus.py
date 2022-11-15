# Import the python Lib

import os
import time

# main code
 
def Prometheus_Monitoring():
    while True:
        print()
        print('*'*80)
        print('*'*18,'Welcome to Prometheus Monitoring Services ','*'*18)
        print('*'*80)
        print('''
                [1] Press A ---> Docker Service Monitoring
                [2] Press B ---> AWS Instances Service Monitoring
                [3] Press C ---> Node Service Monitoring
                If you Want Exit Press'(N/n)'
                ''')
        print('*'*80)
        UserInput = input('Choose Your option: ')
        if UserInput == 'A' or UserInput == 'a':
            print('Docker Service Monitoring ...')
            print()
            time.sleep(2)
            input('Do you Want to Continue Press Enter..')
            os.system('clear')
        
        elif UserInput == 'B' or UserInput == 'b':
            print('AWS Instances Service Monitoring...')
            print()
            time.sleep(2)
            input('Do you Want to Continue Press Enter..')
            os.system('clear')

        elif UserInput == 'C' or UserInput == 'c':
            print('Node Service Monitoring....')
            print()
            time.sleep(2)
            input('Do you Want to Continue Press Enter..')
            os.system('clear')    

        elif UserInput == 'N' or UserInput == 'n':
            print('*'*80)
            print('*'*15,'Thank You For Using Prometheus Monitoring Services..','*'*15)
            print('*'*80)
            exit()   
        else:
            print('*'*80)
            print('You are Choosing=>',UserInput,"it's not Right Option")
            print('Please Choose correct option..')
            print('*'*80)
            os.system('clear')

Prometheus_Monitoring()