import math
import json
import subprocess
from PIL import Image
from subprocess import Popen, PIPE
import os

imageStr = 'image.jpg'
image = Image.open(imageStr)
centreX = image.size[0] / 2
centreY = image.size[1] / 2

process = subprocess.Popen(
    ['gcloud', 'ml', 'vision', 'detect-text', imageStr], stdout=subprocess.PIPE)
#process = subprocess.Popen(
#     ['gcloud', 'ml', 'vision', 'detect-text', imageStr], stdout=subprocess.PIPE)

wordsArr, err = process.communicate()
try:
	flag = True
	wordsArr = json.loads(wordsArr)["responses"][0]["textAnnotations"][1:]
except KeyError:
	flag = False
	print "No words"
#print wordsArr
midWord = ""
maxDist = 10000


def getCenter(vertices):
    sumx = 0
    sumy = 0
    for vertex in vertices:
        if (vertex.get("x") is None or vertex.get("y") is None):
            return [0, 0]
        sumx += vertex["x"]
        sumy += vertex["y"]
    return [sumx/4.0, sumy/4.0]


def getDist(curCenter):
    val = math.sqrt((centreX - curCenter[0]) ** 2
        + (centreY - curCenter[1]) ** 2)
    print val
    return val


for words in wordsArr:
    if not flag:
	break
    word = words["description"]
    print words
    print ""
    curCenter = getCenter(words["boundingPoly"]["vertices"])
    curDist = getDist(curCenter)
    if(curDist < maxDist):
        maxDist = curDist
        midWord = word
if flag:
    print midWord
    os.system("say " + midWord)
