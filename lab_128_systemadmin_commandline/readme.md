You can use Linux to do many administrative tasks from the terminal, or the Bash command line. Python provides several modules that you can also use to run commands on the command line

In this lab, you will:
    -Use os.system() to run a Bash command
    -Use subprocess.run() to run Bash commands
    
OS 
# os.getlogin
# os.getlogin
# os.getgrouplist
# os.getenv
# os.uname
# os.system
# os.chown
# os.chmod
# os.remove
# os.getcwd
# os.mkdir
# os.pwd

Vs SUBPROCESS <!-- this method is safer and more powerful
# subprocess.Popn(<$enter command here>)<!-- returns the result of command as it run the command >
# subprocess.run(<$enter command here>) <!-- returns the result of command after it has run successfully >

<!-- You can use the subprocess module to spawn new processes, connect to input/output/error pipes, and obtain error codes. -->

The full list of arguments for subprocess.run() looks like the following list
# subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)


