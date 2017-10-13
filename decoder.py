from PIL import Image
import os
import time

def shoot(cap_name):
    img = Image.open(cap_name+'.JPEG')
    img = img.convert("RGB")
    pixdata = img.load()
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][0] < 90:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][1] < 136:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][2] > 0:
                pixdata[x, y] = (255, 255, 255, 255)
    ext = ".tif"
    img.save(cap_name + ext)


    command = "tesseract -psm 7 "+cap_name +".tif "+os.curdir+"/text"
    os.system(command)
    time.sleep(1)


    Text  = open ("text.txt","r")
    decoded = Text.readline().strip('\n')
    if decoded.isdigit():
        print '[+}CAPTCHA number are ' + decoded
    else:
        print decoded


def main():

    getlist = os.listdir(os.curdir)
    number = int (len(getlist))
    for cap in range(1,number+1):
        print cap
        shoot(str(cap))

main()
