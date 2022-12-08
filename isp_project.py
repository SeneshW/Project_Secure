import colorama
from colorama import Fore

print ('\n')
print (Fore.BLUE + '||----------------------------------------------------------------------------------------------------------------------------------||')
print ('||                                                                                                                                  ||')
print ('||   ########  ########   #######        ## ########  ######  ########     ######  ########  ######  ##     ## ########  ########   ||')
print ('||   ##     ## ##     ## ##     ##       ## ##       ##    ##    ##       ##    ## ##       ##    ## ##     ## ##     ## ##         ||')
print ('||   ##     ## ##     ## ##     ##       ## ##       ##          ##       ##       ##       ##       ##     ## ##     ## ##         ||')
print ('||   ########  ########  ##     ##       ## ######   ##          ##        ######  ######   ##       ##     ## ########  ######     ||')
print ('||   ##        ##   ##   ##     ## ##    ## ##       ##          ##             ## ##       ##       ##     ## ##   ##   ##         ||')
print ('||   ##        ##    ##  ##     ## ##    ## ##       ##    ##    ##       ##    ## ##       ##    ## ##     ## ##    ##  ##         ||')
print ('||   ##        ##     ##  #######   ######  ########  ######     ##        ######  ########  ######   #######  ##     ## ########   ||')
print ('||                                                                                                                                  ||')
print ('||   Project Secure version 3.2                                                                                                     ||')
print ('||   Information Security Project                                                                                                   ||')
print ('||                                                                                                                                  ||')
print ('||----------------------------------------------------------------------------------------------------------------------------------||')

print (Fore.GREEN + '\n    [1] Get started with' '\033[1m' + " Project Secure!" '\033[0m')
print (Fore.GREEN + '    [2] SQLi Scanner')
print (Fore.GREEN + '    [3] XSS Scanner')
print (Fore.GREEN + '    [0] Exit')

selection = input(Fore.WHITE + "\nPlease Enter the Number of the task required: ")

import os
import sys

if selection == "1":
  print('\nInstalling Required Tools for' '\033[1m' + " Project Secure!" '\033[0m' '...')
  os.system("python get_started_with_PS.py")
   
elif selection == "2":  
  os.system ('python sqli.py') 
  
elif selection == "3":
  os.system("python xss.py")
  
elif selection == "0":
  print('\n    - Thank you for using' '\033[1m' + " Project Secure! " '\033[0m' '-\n')
  sys.exit()

exit()
