import subprocess

#part 1- find prime numbers .......
def find_primes(n):
    primes = []
    for num in range(2, n+1):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primes.append(num)
    return primes

primes_list = find_primes(250)

#part 2- log prime numbers into separate file......
current_directory = subprocess.run("cd",  #in windows systems use CD, Unix use PWD 
                                   shell=True, #shell=True argument to run it in the shell.
                                   stdout=subprocess.PIPE #subprocess.PIPE to get the output of the command as a variable
                                   )
absolute_path='/Users/jerem/OneDrive/Documents/CODE/Python/DCI-Python/intermediate/systemAdmin/labs/lab_141_scripting_exercise/' 
current_directory = current_directory.stdout.decode().strip() #.decode() to decode the output from bytes to a string, # '.strip()' method to remove any extra whitespace. then we concatenate the current directory with the file name and path to create the full file path.

file_path = absolute_path + "/results.txt"

with open(file_path, "w") as f:
    for prime in primes_list:
        f.write(str(prime) + "\n")

print("Primes have been written to the results.txt file.")


# do do the same thing using OS---------------------------------
# import os

# def find_primes(n):
#     primes = []
#     for num in range(2, n+1):
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             primes.append(num)
#     return primes

# primes_list = find_primes(250)

# file_path = os.path.join( #os.path.join() to join the current working directory and the file name results.txt to create the full path
    # os.getcwd() + "result.txt"
    # ) #.getcwd() function to get the current working 
# with open(file_path, "w") as f:
#     for prime in primes_list:
#         f.write(str(prime) + "\n")

# print("Primes have been written to the results.txt file.")


