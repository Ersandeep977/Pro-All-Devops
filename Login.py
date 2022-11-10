import Main as m
   
print('*'*80)
print('*'*24,'Welcome to Devops Menu Program','*'*24)
print('*'*80)       
for _ in range(3):
    usr = input("Enter username: ")
    psw = input("Enter password: ")
    
    if usr == "s" and psw == 's':
        print('*'*80)
        print("Access Granted..!")
        print('*'*80)
        print('Welcome...')
        print('User Name ==>',usr)
        print('*'*80)
        m.MainFun()
        break
    else:
        print("Access Denied!")
    print("Try Again!")
else:
    print("No more attemps!")

