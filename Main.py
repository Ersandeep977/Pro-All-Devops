# this file is main file which is connted to all the file
#
# import all the library 
import os
from time import sleep
import JenkinsService as JS
import AwsService as AWS
# os.system('ls')

# main code started 
###################################################################################
def MainFun():
    while True:
        print()
        print('*'*80)
        print('*'*24,'Welcome to Devops Menu Program','*'*24)
        print('*'*80)
        print('''
            [1] Press A ---> Jenkins Service
            [2] Press B ---> AWS Cloud Service
            [3] Press C ---> Ansible Service 
            [4] Press D ---> Prometheus Monitoring
            If you Want Exit Press'(N/n)'
            ''')
        print('*'*80)
        UserInput = input('Choose Your option: ')
        if UserInput == 'A' or UserInput == 'a':
            JS.JenkinsInfo()
            os.system('clear')
        elif UserInput == 'B' or UserInput == 'b':
            AWS.Aws_Serive()
            os.system('clear')
        elif UserInput == 'C' or UserInput == 'c':
            print('c')
            os.system('clear')
        elif UserInput == 'D' or UserInput == 'd':
            print('d')    
        elif UserInput == 'N' or UserInput == 'n':
            print('*'*80)
            print('*'*21,'Thank You For Using Devops Program..','*'*21)
            print('*'*80)
            exit()   
        else:
            print('woring optin')
            os.system('clear')


