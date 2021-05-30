#Imports
import pyautogui
import time


#Getting mouse position
# This will let you "measure" the coordinates of specific points on screen by hovering your mouse over it
# Very useful - you'll see why when I talk about the design process
def get_mouse_pos():
    while True:
        print(pyautogui.position())
        time.sleep(1)






time.sleep(2)
# ============================
#          MAIN BODY
# ============================
# This is where the actual code for the bot will be written
# Don't worry, it's not complicated, and I'll walk you through it in the workshop anyway :)
while True:

  # take and save ss

    ss = pyautogui.screenshot("pianotiles.jpeg").convert("RGB")

    col1 = 655, 525
    col2 = 730, 525
    col3 = 832, 525
    col4 = 902, 525

    col1_colour = ss.getpixel(col1)
    col2_colour = ss.getpixel(col2)
    col3_colour = ss.getpixel(col3)
    col4_colour = ss.getpixel(col4)

    if col1_colour == (0, 0, 0):
        pyautogui.click(col1)
    if col2_colour == (0, 0, 0):
        pyautogui.click(col2)
    if col3_colour == (0, 0, 0):
        pyautogui.click(col3)
    if col4_colour == (0, 0, 0):
        pyautogui.click(col4)
