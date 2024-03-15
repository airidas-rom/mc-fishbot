import time
import cv2
import pyautogui
import numpy as np


def fish():
    img_path = 'catch.png'
    target_img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    target_img_bgra = cv2.cvtColor(target_img, cv2.COLOR_BGR2BGRA)

    while True:
        screenshot = pyautogui.screenshot()

        screenshot_np = cv2.cvtColor(
            cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR),
            cv2.COLOR_BGR2BGRA
        )
        result = cv2.matchTemplate(screenshot_np, target_img_bgra, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val > 0.8:  # You can adjust this threshold as needed
            pyautogui.click(button='right')
            break

def main():
    time.sleep(2) # you can adjust this as needed
    while True:
        time.sleep(0.5)
        pyautogui.click(button='right')
        time.sleep(3)
        fish()

main()