import subprocess
import os
import time
# ================language variable begin========================
Tips_at_the_beginning = 'Type "help" or command for more information.'
# ================language variable finish========================
print(Tips_at_the_beginning)
while True:
    command = input('>> ')
    if command == 'help':
        helps = ['input "Reload_computer_drivers" can reload your computer drivers','input "Reload_computer_hosts_file" can reload your computer hosts file','input "exit" can exit System Tool Box']
        for i in helps:
            time.sleep(0.5)
            print(i)
    elif command == "Reload_computer_drivers":
        subprocess.Popen('Reload-drivers',shell=True)
    elif command == "Reload_computer_hosts_file":
        subprocess.Popen('Reload-hosts',shell=True)
    elif command == 'exit':
        print('good bye!')
        os._exit(0)
    elif command == '':
        pass
    else:
        if command in 'help':
            print('Type "help" for interactive help')
        elif command in 'Reload':
            print('"Reload_computer_drivers" of "Reload_computer_hosts_file"')
        elif command in 'reload':
            print('"Reload_computer_drivers" of "Reload_computer_hosts_file"')