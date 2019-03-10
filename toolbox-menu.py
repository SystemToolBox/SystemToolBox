import subprocess
import os
print('======================================')
print('        welcome to use Toolbox')
print('             This is menu')
print('   Here is a rundown of the options')
print('[1]init toolbox    [2]update toolbox')
print('[3]Reload-drivers  [4]Reload-hosts')
print('[exit]exit menu')
print('======================================')
while True:
    choose = int(input('your options is: '))
    if choose == 1:
        print("input 'Set-ExecutionPolicy UnRestricted' to powershell")
        cmd = subprocess.Popen(r'%SystemRoot%\system32\WindowsPowerShell\v1.0\powershell.exe',shell=True)
        cmd.wait()
    elif choose == 'exit':
        os._exit(0)