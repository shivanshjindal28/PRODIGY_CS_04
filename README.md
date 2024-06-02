# PRODIGY_CS_04
Simple Keylogger - Created a basic keylogger program that records and logs keystrokes. The program focuses on logging the keys pressed and saving them to a file. Note: Ethical considerations and permissions are crucial for projects involving keyloggers.<br>
Creating a keylogger involves ethical and legal considerations. Keyloggers can be used for malicious purposes, so it is crucial to ensure you have explicit permission to use it on any system.<br>
Here's a simple keylogger implemented in Python using the 'pynput' library. This script will log keystrokes to a file named 'keylog.txt'.<br><br>
Installation of Required Library:<br>
First, you need to install the 'pynput' library. You can do this using pip. Command: pip install pynput<br><br>
Working of the script:<br>
1. Import Required Libraries: The script imports necessary components from 'pynput'.<br>
2. Log File: The script defines the name of the log file where keystrokes will be recorded.<br>
3. on_press Function: This function handles the key press event. It attempts to write the character of the key pressed to the log file. If the key is a special key (like space, enter, or tab), it writes a corresponding representation to the log file.<br>
4. on_release Function: This function is defined but not utilized. It could be used to add functionality for stopping the keylogger or other purposes.<br>
5. Start Listener: The script starts the keylogger by creating an instance of 'Listener' with the 'on_press' and 'on_release' functions and then calls 'listener.join()' to keep the program running and listening for keystrokes.<br><br>
To run the keylogger, simply execute the script.<br>
As you type, the keystrokes will be logged to a file named 'keylog.txt' in the same directory as your script.<br>
Open 'keylog.txt' to see the logged keystrokes.<br><br>
Important ethical and legal considerations:-<br>
a. Obtain Permission: Ensure you have explicit permission to run the keylogger on any computer. Unauthorized use is illegal and unethical.<br>
b. Use for Educational Purposes: Use this script only for educational purposes or authorized security testing.<br>
c. Inform Users: If you are using this script in a shared environment, inform all users about the keylogging and its purpose.<br>
By following these steps, you can create, run, and verify a basic keylogger using any code editor while adhering to ethical guidelines.<br>
