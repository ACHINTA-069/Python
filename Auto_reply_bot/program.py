import pyautogui
import time
import pyperclip  # install via: pip install pyperclip

# Step 1: Click on the icon
time.sleep(2)  # Small delay so you can switch to the target window
pyautogui.click(1294, 1059)

# Step 2: Drag to select text
time.sleep(1)  # Allow time for app to open
pyautogui.moveTo(522, 139)
pyautogui.dragTo(1896, 933, duration=1, button='left')

# Step 3: Copy the text (Ctrl+C)
pyautogui.hotkey("ctrl", "c")
time.sleep(0.5)  # Allow clipboard to update

# Step 4: Get the copied text into a variable
copied_text = pyperclip.paste()

print("Copied text:")
print(copied_text)
 