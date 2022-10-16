print ('\n')
print ('||----------------------------------------------------------------------------------------------------------------------------------||')
print ('||                                                                                                                                  ||')
print ('||   ########  ########   #######        ## ########  ######  ########     ######  ########  ######  ##     ## ########  ########   ||')
print ('||   ##     ## ##     ## ##     ##       ## ##       ##    ##    ##       ##    ## ##       ##    ## ##     ## ##     ## ##         ||')
print ('||   ##     ## ##     ## ##     ##       ## ##       ##          ##       ##       ##       ##       ##     ## ##     ## ##         ||')
print ('||   ########  ########  ##     ##       ## ######   ##          ##        ######  ######   ##       ##     ## ########  ######     ||')
print ('||   ##        ##   ##   ##     ## ##    ## ##       ##          ##             ## ##       ##       ##     ## ##   ##   ##         ||')
print ('||   ##        ##    ##  ##     ## ##    ## ##       ##    ##    ##       ##    ## ##       ##    ## ##     ## ##    ##  ##         ||')
print ('||   ##        ##     ##  #######   ######  ########  ######     ##        ######  ########  ######   #######  ##     ## ########   ||')
print ('||                                                                                                                                  ||')
print ('||   Project Secure version 2.0                                                                                                     ||')
print ('||   Coded by Senesh Wijayarathne & Anodya Garusinghe                                                                               ||')
print ('||   Information Security Project                                                                                                   ||')
print ('||                                                                                                                                  ||')
print ('||----------------------------------------------------------------------------------------------------------------------------------||')

print ('\n    [1] Get started with' '\033[1m' + " Project Secure!" '\033[0m')
print ('    [2] SQLi Scanner')
print ('    [3] XSS Scanner')
print ('    [0] Exit')

selection = input("\nPlease Enter the Number of the task required: ")

import os
import sys

if selection == "1":
  print('\nInstalling Required Tools for' '\033[1m' + " Project Secure!" '\033[0m' '...')
  os.system("python get_started_with_PS.py")
   
elif selection == "2":  
  os.system ('python sqlitest.py') 
  
elif selection == "3":
  os.system("python xsstest.py")
  
elif selection == "0":
  print('\n    - Thank you for using' '\033[1m' + " Project Secure! " '\033[0m' '-\n')
  sys.exit()

exit()
