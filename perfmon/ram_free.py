##########################
# IF FREE_RAM < CRITICAL_VALUE : { ACTION }
##########################

import os

# Critical value
critical = 13

# Free memory percentage
mem=str(os.popen('free | grep Mem | awk \'{print 100*$4/$2}\' ').readlines())
value = float(mem[2:-4])

print(value)

if value < critical:
  print('reboot')
  #os.system('reboot')
else:
  print('No reboot')
