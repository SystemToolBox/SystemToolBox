import subprocess
import os
print('======================================')
print('        welcome to use Toolbox        ')
print('             This is menu             ')
print('   Here is a rundown of the options   ')
print('[1]init toolbox    [2]update toolbox  ')
print('[3]Reload-drivers  [4]Reload-hosts    ')
print('[exit]exit menu                       ')
print('======================================')
while True:
    try:
        choose = int(input('your options is: '))
    except ValueError:
        print('please input your options again')
        choose = input('your options is: ')
    finally:
        if choose == 1:
            pass
        elif choose == 'exit':
            os._exit(0)