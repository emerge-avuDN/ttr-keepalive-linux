# keepalive.py
# Keeps your toon awake in ToonTown Rewritten by sending periodic keypresses.
# Uses xdotool to send keypresses to the TTR window.
import subprocess
import time
import random


# Gets TTR's unique X11 window ID. The window ID is dynamic
# so it cannot be hard-coded.
def getWindowID(win_name) -> list:
    try:
        output = subprocess.check_output(
        ['xdotool', 'search', '--name', win_name]
        ).split()
        window_ids = [win.decode("utf-8") for win in output]
        print(f"Found the following windows: {window_ids}")
        return window_ids
    except subprocess.CalledProcessError:
        print("ToonTown was not found.")
        return []

# Gets the time (in seconds) to send the keypress in a 1-2 min interval. 
def randomVariance():
    delay = random.uniform(60, 120) 
    keys = ["End", "Home"] # List of keys
    return delay, random.choice(keys)

# Send the keypress
def sendInput(win_id, key):
    # Send key to window
    subprocess.call(['xdotool', 'key', '--window', win_id, key])

# Run the program
if __name__ == "__main__":
    win_name = "Toontown Rewritten"
    while True:
        delay, key = randomVariance()
        
        print(f"Delay: {delay}\nKey: {key}")
        # Find all instances of TTR
        win_ids = getWindowID(win_name)
        if not win_ids:
            print("Failed to find any windows. Please open the game first.")
            break # Terminate if TTR isn't open
        
        for i, win_id in enumerate(win_ids, start=1):
            sendInput(win_id, key)
            print(f"Keypress {key} sent to Window #{i} @ Window ID {win_id}") 

        print(f"Waiting {(delay/60):.2f} minutes..")
        time.sleep(delay) 
        