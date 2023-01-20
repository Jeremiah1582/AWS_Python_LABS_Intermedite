# WOW 👀 🤯 
import os 
import subprocess

#part 1
os.system('ls')
subprocess.Popen('ls')
subprocess.run(['ls','-l', "readme.md"])

# part 2 - get info about system user
command = "uname"
commandArgument="-a"
print(f"Gathering system info with command: {command} {commandArgument} ")
subprocess.run([command, commandArgument])

# part 3- get info systems Process Status
command2="ps"
commandArgument2="-a"
print(f'gathering active process information with command: {command2} {commandArgument2}')
subprocess.run( [command2, commandArgument2])

