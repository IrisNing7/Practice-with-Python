import pyautogui
pyautogui.size()

width, height = pydutogui.size()
width
height
pyautogui.position()


pyautogui.moveTo(10, 10)
pyautogui.moveTo(10, 10,duration=1.5) #duration is moving time

pyautogui.moveRel(20, 0)
pyautogui.moveRel(200, 0, duration=2)
pyautogui.moveRel(0, -100) #move fast
pyautogui.moveRel(0, -100, duration=1) #move slow

pyautogui.position()
pyautogui.click(339, 38) #x=339 y=38 can be any number
pyautogui.doubleclick(339, 38)


pyautogui.displayMousePosition() #better to show mouse position via terminal
