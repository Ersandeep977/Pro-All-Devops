import jenkins
import os
import time

j = jenkins.Jenkins('http://192.168.56.1:8080', username='admin', password='root')


while True:
    print()
    print('*'*80)
    print('*'*24,'Welcome to AWS Services ','*'*24)
    print('*'*80)
    print('''
            [1] Press A ---> Ansible_M_Server
            [2] Press B ---> Ansible_Node_A
            [3] Press C ---> Ansible_Node_B
            [4] Press D ---> All Ec2 Stop
            If you Want Exit Press'(E/e)'
            ''')
    print('*'*80)
    UserInput = input('Choose Your option: ')
    if UserInput == 'A' or UserInput == 'a':
        print(j.build_job("Ansible_M_Server"))
        print('Pipeline Start ...')
        time.sleep(2)
        print('EC2 Ansible M Server Stated')
        print('Plz Check.. jenkins dashboard')
        input('Do you Want to Continue Press Enter..')
    
    elif UserInput == 'B' or UserInput == 'b':
        print(j.build_job("Ansible_Node_A"))
        print('EC2 Ansible M Ansible_Node_A')
        print('Pipeline Start ...')
        time.sleep(2)
        print('Plz Check.. jenkins dashboard')
        input('Do you Want to Continue Press Enter..')
    
    elif UserInput == 'C' or UserInput == 'c':
        print(j.build_job("Ansible_Node_B"))
        print('EC2 Ansible Ansible_Node_B')
        print('Pipeline Start ...')
        time.sleep(2)
        print('Plz Check.. jenkins dashboard')
        input('Do you Want to Continue Press Enter..')

    elif UserInput == 'C' or UserInput == 'c':
        print(j.build_job("Stop All EC2 Instances"))
        print('EC2 Ansible Ansible_Node_B')
        print('Pipeline Start ...')
        time.sleep(2)
        print('Plz Check.. jenkins dashboard')
        input('Do you Want to Continue Press Enter..')    

    elif UserInput == 'E' or UserInput == 'e':
        print('*'*80)
        print('*'*21,'Thank You For Using AWS Services Page..','*'*21)
        print('*'*80)
        exit()   
    else:
        print('woring optin')
        os.system('clear')


    

