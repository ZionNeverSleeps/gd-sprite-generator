import math
import pygame
import sys
from pygame.locals import *
#if testing is set to true, then a pygame window with all of the textures is displayed. when used in tandem with an object ID reference, entries in the spriteToObject dictionary can be filled in.
testing = False
if testing:
    fontpath = "C:\\Users\\hates\\Desktop\\stuff\\art\\aedimain\\mvboli.ttf"
    screen = pygame.display.set_mode((600,600))
    screen.fill((127,127,127))
    pygame.init()
def strToDec(l):
    returnVal = 0
    decPointPlace = len(l)
    negative = 0
    if l[0] == "-":
        negative = 1
    for i in range(len(l)):
        if l[i] == ".":
            decPointPlace = i
    for i in range(len(l)):
        if i < decPointPlace:
            if l[i] == '1':
                returnVal = returnVal + 1 * pow(10,-i+len(l)-1-(len(l)-decPointPlace))
            elif l[i] == '2':
                returnVal = returnVal + 2 * pow(10,-i+len(l)-1-(len(l)-decPointPlace))
            elif l[i] == '3':
                returnVal = returnVal + 3 * pow(10,-i+len(l)-1-(len(l)-decPointPlace))
            elif l[i] == '4':
                returnVal = returnVal + 4 * pow(10,-i+len(l)-1-(len(l)-decPointPlace))
            elif l[i] == '5':
                returnVal = returnVal + 5 * pow(10,-i+len(l)-1-(len(l)-decPointPlace))
            elif l[i] == '6':
                returnVal = returnVal + 6 * pow(10,-i+len(l)-1-(len(l)-decPointPlace))
            elif l[i] == '7':
                returnVal = returnVal + 7 * pow(10,-i+len(l)-1-(len(l)-decPointPlace))
            elif l[i] == '8':
                returnVal = returnVal + 8 * pow(10,-i+len(l)-1-(len(l)-decPointPlace))
            elif l[i] == '9':
                returnVal = returnVal + 9 * pow(10,-i+len(l)-1-(len(l)-decPointPlace))
        if i > decPointPlace:
            if l[i] == '1':
                returnVal = returnVal + 1 / pow(10,i-decPointPlace)
            elif l[i] == '2':
                returnVal = returnVal + 2 / pow(10,i-decPointPlace)
            elif l[i] == '3':
                returnVal = returnVal + 3 / pow(10,i-decPointPlace)
            elif l[i] == '4':
                returnVal = returnVal + 4 / pow(10,i-decPointPlace)
            elif l[i] == '5':
                returnVal = returnVal + 5 / pow(10,i-decPointPlace)
            elif l[i] == '6':
                returnVal = returnVal + 6 / pow(10,i-decPointPlace)
            elif l[i] == '7':
                returnVal = returnVal + 7 / pow(10,i-decPointPlace)
            elif l[i] == '8':
                returnVal = returnVal + 8 / pow(10,i-decPointPlace)
            elif l[i] == '9':
                returnVal = returnVal + 9 / pow(10,i-decPointPlace)
    if negative == 1:
        returnVal = returnVal * -1
    return returnVal
hostSheets = [pygame.image.load("C:\\Program Files (x86)\\Steam\\steamapps\\common\Geometry Dash\\Resources\\GJ_GameSheet-uhd.png"),pygame.image.load("C:\\Program Files (x86)\\Steam\\steamapps\\common\Geometry Dash\\Resources\\GJ_GameSheet02-uhd.png")]
class sprite:
    def __init__(self, name, offset, size, sSize, tRect, rotate, hs):
        self.name = name
        self.offset = offset
        self.size = size
        self.sSize = sSize
        self.tRect = tRect
        self.rotate = rotate
        self.hostSheet = hs
    def pr(self):
        print("name:", self.name)
        print("offset:", self.offset)
        print("size:", self.size)
        print("sSize:", self.sSize)
        print("tRect:", self.tRect)
        print("rotate:", self.rotate)
        print("host sheet:", self.hostSheet)
    def getSurface(self):
        sub = hostSheets[self.hostSheet].subsurface(self.tRect)
        if self.rotate:
            sub = pygame.transform.rotate(sub, 90)
        return sub
    def getSurface40(self):
        sub = hostSheets[self.hostSheet].subsurface(self.tRect)
        sub = pygame.transform.scale(sub, (40,40))
        if self.rotate:
            sub = pygame.transform.rotate(sub, 90)
        return sub
sprites = []
with open("C:\\Program Files (x86)\\Steam\\steamapps\\common\Geometry Dash\\Resources\\GJ_GameSheet-uhd.plist") as f:
    a = f.read()
dictStart = "<dict>"
dictEnd = "</dict>"
dictStarts = []
dictEnds = []
for i in range(237,len(a)-10):
    sub = a[i:i+6]
    sub2 = a[i:i+7]
    if sub == dictStart:
        dictStarts.append(i+6)
    elif sub2 == dictEnd:
        dictEnds.append(i)
dictStarts[-1:] = []
dictEnds[-3:] = []
keyStart = "<key>"
offs = [72,78,73]
for i in range(len(dictStarts)):
    sub = ""
    c = dictStarts[i]-25
    found = False
    while not found:
        c -= 1
        if a[c-5:c] == keyStart:
            found = True
    name = a[c:dictStarts[i]-25]
    prop = a[dictStarts[i]:dictEnds[i]]
    rCheck = a[dictEnds[i]-19:dictEnds[i]-15]
    rotated = (rCheck == "true")
    strStarts = [125]
    c = 125
    propsStrings = []
    while len(strStarts) < 5:
        c += 1
        if prop[c] == "<":
            propsStrings.append(prop[strStarts[-1]:c])
            if len(strStarts) < 4:
                c += offs[len(strStarts)-1]
            strStarts.append(c)
    vh = []
    props = []
    for j in range(4):
        sub = []
        for k in range(len(propsStrings[j])):
            if propsStrings[j][k] == ",":
                sub.append(strToDec(vh))
                vh = []
            else:
                if not (propsStrings[j][k] == "}" or propsStrings[j][k] == "{"):
                    vh.append(propsStrings[j][k])
        sub.append(strToDec(vh))
        vh = []
        props.append(sub)
    if rotated:
        sub = [props[3][0],props[3][1],props[3][3],props[3][2]]
        props[3] = sub
        sub2 = [props[1][1],props[1][0]]
        props[1] = sub2
        sub3 = [props[2][1],props[2][0]]
        props[2] = sub3
        sub4 = [props[0][1],props[0][0]]
        props[0] = sub4
    sprites.append(sprite(name, props[0], props[1], props[2], props[3], rotated, 0))
with open("C:\\Program Files (x86)\\Steam\\steamapps\\common\Geometry Dash\\Resources\\GJ_GameSheet02-uhd.plist") as f:
    b = f.read()
dictStarts = []
dictEnds = []
for i in range(237,len(b)-10):
    sub = b[i:i+6]
    sub2 = b[i:i+7]
    if sub == dictStart:
        dictStarts.append(i+6)
    elif sub2 == dictEnd:
        dictEnds.append(i)
dictStarts[-1:] = []
dictEnds[-3:] = []
keyStart = "<key>"
offs = [72,78,73]
for i in range(len(dictStarts)):
    sub = ""
    c = dictStarts[i]-25
    found = False
    while not found:
        c -= 1
        if b[c-5:c] == keyStart:
            found = True
    name = b[c:dictStarts[i]-25]
    prop = b[dictStarts[i]:dictEnds[i]]
    rCheck = b[dictEnds[i]-19:dictEnds[i]-15]
    rotated = (rCheck == "true")
    strStarts = [125]
    c = 125
    propsStrings = []
    while len(strStarts) < 5:
        c += 1
        if prop[c] == "<":
            propsStrings.append(prop[strStarts[-1]:c])
            if len(strStarts) < 4:
                c += offs[len(strStarts)-1]
            strStarts.append(c)
    vh = []
    props = []
    for j in range(4):
        sub = []
        for k in range(len(propsStrings[j])):
            if propsStrings[j][k] == ",":
                sub.append(strToDec(vh))
                vh = []
            else:
                if not (propsStrings[j][k] == "}" or propsStrings[j][k] == "{"):
                    vh.append(propsStrings[j][k])
        sub.append(strToDec(vh))
        vh = []
        props.append(sub)
    if rotated:
        sub = [props[3][0],props[3][1],props[3][3],props[3][2]]
        props[3] = sub
        sub2 = [props[1][1],props[1][0]]
        props[1] = sub2
        sub3 = [props[2][1],props[2][0]]
        props[2] = sub3
        sub4 = [props[0][1],props[0][0]]
        props[0] = sub4
    sprites.append(sprite(name, props[0], props[1], props[2], props[3], rotated, 1))
if testing:
    page = 0
    fonts = [0]
    for i in range(100):
        fonts.append(pygame.font.Font(fontpath, i+1))
    def dispText(t,p,s,c):
        textLines = []
        sub = ""
        for i in range(len(t)):
            if not t[i] == "\n":
                sub += t[i]
            else:
                textLines.append(sub)
                sub = ""
        textLines.append(sub)
        for i in range(len(textLines)):
            text = fonts[s].render(textLines[i], 1, c)
            screen.blit(text, text.get_rect(centerx=p[0], centery=p[1]-(len(textLines)-1)*s/2+s*i))
spriteToObject = [
    [1,[1521]],
    
    [8,[1513]],
    [39,[1514]],
    [103,[1515]],
    [392,[1516]],

    [10,[2140]],
    [11,[2144]],
    [12,[2148]],
    [13,[2152]],
    [45,[2154]],
    [46,[2156]],
    [47,[2160]],
    [99,[2162]],
    [101,[2164]],
    [111,[2168]],
    [286,[2170]],
    [287,[2172]],
    [660,[2176]],
    [745,[2180]],
    [747,[2182,2184]],
    [1331,[2188]],
    [1933,[2192]],
    [2926,[2196]],

    [35,[746]],
    [1332,[747]],
    [140,[748]],
    [67,[1126]],
    [3005,[1511]],

    [36,[1491]],
    [1333,[1492]],
    [141,[1494]],
    [1330,[1105]],
    [84,[1127]],
    [1022,[1124]],
    [1751,[1104]],
    [1704,[1103]],
    [3004,[1512]],

    [200,[1636]],
    [201,[1637]],
    [202,[1638]],
    [203,[1639]],
    [1334,[1640]],

    [1743,[1585,1410]],
    [1744,[1586,1409]],
    ]
mainIDList = []
for i in range(4385):
    mainIDList.append(None)
for i in range(len(spriteToObject)):
    sub = []
    for j in range(len(spriteToObject[i][1])):
        sub.append(sprites[spriteToObject[i][1][j]].getSurface())
    mainIDList[spriteToObject[i][0]] = sub
while testing:
    mp = pygame.mouse.get_pos()
    pygame.draw.rect(screen, (127,127,127), (0,0,600,600))
    for i in range(100):
        if i+page*100 < len(sprites):
            screen.blit(sprites[i+page*100].getSurface40(), ((i%10)*60+10, int(i/10)*60+10))
            dispText(str(i+page*100), [(i%10)*60+30, int(i/10)*60+55], 10, (0,0,0))
            if mp[0] > (i%10)*60+10 and mp[0] < (i%10)*60+50 and mp[1] > int(i/10)*60+10 and mp[1] < int(i/10)*60+50:
                sampSize = sprites[i+page*100].getSurface().get_size()
                dispText(str(sampSize), mp, 10, (0,0,0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == 1073741903:
                if page < int(len(sprites)/100):
                    page += 1
            elif event.key == 1073741904:
                if page > 0:
                    page -= 1
