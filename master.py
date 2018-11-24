import math
import json
import subprocess
from subprocess import Popen, PIPE
import os

centreX = 2592/2
centreY = 1944/2
process = subprocess.Popen(['../../google-cloud-sdk/bin/gcloud', 'ml', 'vision', 'detect-text', 'test.jpg'], stdout=subprocess.PIPE)
#process = subprocess.Popen(['gcloud', 'ml', 'vision', 'detect-text', 'image.jpg'], stdout=subprocess.PIPE)

wordsArr, err = process.communicate()
wordsArr = json.loads(wordsArr)["responses"][0]["textAnnotations"][1:]
#print wordsArr
midWord = ""
maxDist = 10000



def getCenter(vertices):
    sumx = 0
    sumy = 0
    for vertex in vertices:
        sumx += vertex["x"]
        sumy += vertex["y"]
    return [sumx/4.0, sumy/4.0]

def getDist(curCenter):
    return math.sqrt( (centreX - curCenter[0] ) ** 2 + (centreY - curCenter[1] ) ** 2 )

for words in wordsArr:
  word = words["description"]
  curCenter = getCenter(words["boundingPoly"]["vertices"])
  curDist = getDist(curCenter)
  if(curDist < maxDist):
      curDist = maxDist
      midWord = word
print midWord
os.system("say " + midWord)