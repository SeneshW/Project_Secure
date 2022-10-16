import os
import sys

input ('Press Enter to Start...\n')
print ('\nInstalling' '\033[1m' + " pip3" '\033[0m' ' to your system...\n')

os.system('sudo apt install python3-pip')

print ('\n')
print ('\033[1m' + "Completed!!" '\033[0m')

input ('\nPress Enter to Continue...')

print ('\nInstalling' '\033[1m' + " requests bs4 with pip3" '\033[0m' ' to your system...\n')

os.system('pip3 install requests bs4')

print ('\n')
print ('\033[1m' + "Completed!!" '\033[0m')

input ('\nPress Enter to Exit...')

print('\n- Enjoy using' '\033[1m' + " Project Secure! " '\033[0m' '-')

import isp_project.py
sys.exit()
