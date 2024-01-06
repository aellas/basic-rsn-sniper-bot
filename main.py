import pyautogui as pg
import time

username = pg.prompt(text="", title='Enter your username')

while True:
    search = pg.locateOnScreen('rsn-sniper/e.png', confidence=0.8)
    done = pg.locateOnScreen('rsn-sniper/done.png', confidence=0.8)
    check = pg.locateOnScreen('rsn-sniper/check.png', confidence=0.8)

    if check is not None:
        pg.click(check)
        time.sleep(0.5)

    pg.click(search)
    time.sleep(1)
    pg.typewrite(username)
    time.sleep(1)
    pg.click(done)
    time.sleep(1)

    username_length = len(username)

    for _ in range(username_length):
        pg.press('backspace')
        time.sleep(0.05)
    time.sleep(1)
    time.sleep(0.5)
