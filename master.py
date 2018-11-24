import math
import json
import subprocess
from subprocess import Popen, PIPE
import os

centreX = 1920/2
centreY = 1080/2
process = subprocess.Popen(['gcloud', 'ml', 'vision', 'detect-text', 'image.jpg'], stdout=subprocess.PIPE)
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
        if ( (vertex.get("x") is None) or vertex.get("y") is None):
          return [0,0]  
        sumx += vertex["x"]
        sumy += vertex["y"]
    return [sumx/4.0, sumy/4.0]

def getDist(curCenter):
    val = math.sqrt( (centreX - curCenter[0] ) ** 2 + (centreY - curCenter[1] ) ** 2 )
    print val
    return val

for words in wordsArr:
  word = words["description"]
  print words
  print ""
  curCenter = getCenter(words["boundingPoly"]["vertices"])
  curDist = getDist(curCenter)
  if(curDist < maxDist):
      maxDist = curDist
      midWord = word
print midWord
os.system("say " + midWord)
