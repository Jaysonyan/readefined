import json
import math
import os
import subprocess
from PIL import Image
from subprocess import Popen, PIPE

imgStr = 'image.jpg'
img = Image.open(imgStr)
centreX = img.size[0] / 2
centreY = img.size[1] / 2

process = subprocess.Popen(
    ['gcloud', 'ml', 'vision', 'detect-text', imgStr], stdout=subprocess.PIPE)

wordsArr, err = process.communicate()
try:
    wordsDetected = True
    wordsArr = json.loads(wordsArr)["responses"][0]["textAnnotations"][1:]
except KeyError:
    wordsDetected = False
    print "No words"
#print wordsArr
midWord = ""
maxDist = 10000


def getCentre(vertices):
    sumX = 0
    sumY = 0
    for vertex in vertices:
        if (vertex.get("x") is None or vertex.get("y") is None):
            return [0, 0]
        sumX += vertex["x"]
        sumY += vertex["y"]
    return [sumX/4.0, sumY/4.0]


def getDist(curCentre):
    val = math.sqrt((centreX - curCentre[0]) ** 2
                    + (centreY - curCentre[1]) ** 2)
    print val
    return val


for words in wordsArr:
    if not wordsDetected:
        break
    word = words["description"]
    print words
    print ""
    curCentre = getCentre(words["boundingPoly"]["vertices"])
    curDist = getDist(curCentre)
    if(curDist < maxDist):
        maxDist = curDist
        midWord = word
if wordsDetected:
    print midWord
    os.system("say " + midWord)
