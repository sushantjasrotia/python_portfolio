import time
import pyautogui
from PIL import Image, ImageGrab
# from numpy import asarray

def hit(key):
    pyautogui.keyDown(key)

def isCollide(data):

    #Draw the ractangle for birds
    for i in range(250, 300):
        for j in range(410, 563):
            if data[i, j] < 171:
                hit("down")
                return
    #caltus
    for i in range(300, 360):
        for j in range(563, 650):
            if data[i, j] < 100:  # 0 means black color
                hit("up")
                return
    return


if __name__=="__main__":
    print("hey.. game about to start in 3 sec")
    time.sleep(3)
    hit("up")
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
        # # print(asarray(image))

        #ractangel for cactus
        # for i in range(300, 415):
        #     for j in range(600, 650):
        #         data[i, j] = 0 #0 means black color

        #draw the ractangle for birds
        # for i in range(300, 415):
        #     for j in range(410, 610):
        #         data[i, j] = 171

        # image.show()




