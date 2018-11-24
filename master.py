import math
import json
import subprocess
from subprocess import Popen, PIPE

centerx = 276
centery = 276
maxDist = 1000
process = subprocess.Popen(['../../google-cloud-sdk/bin/gcloud', 'ml', 'vision', 'detect-text', 'test.jpg'], stdout=subprocess.PIPE)
wordsArr, err = process.communicate()
wordsArr = json.loads(wordsArr)["responses"][0]["textAnnotations"][1:]
#print wordsArr

midWord = ""
for words in wordsArr:
  word = words["description"]
  vertices = words["boundingPoly"]["vertices"]
  if(vertices[0]["x"] < centerx and vertices[0]["y"] < centery):
      if(vertices[1]["x"] > centerx and vertices[1]["y"] < centery):
          if(vertices[2]["x"] > centerx and vertices[2]["y"] > centery):
              if(vertices[3]["x"] < centerx and vertices[3]["y"] > centery):
                  print word
                  break


#   curCenter = getCenter(words["boundingPoly"]["vertices"])
#   curDist = getDist(curCenter)
#   if(curDist < maxDist):
#       curDist = maxDist
#       midWord = word

# def getCenter(vertices):
#     sumx = 0
#     sumy = 0
#     for vertex in vertices:
#         sumx += vertex["x"]
#         sumy += vertex["y"]
#     return [sumx/4.0, sumy/4.0]

# def getDist(curCenter):
#     return math.sqrt( (center["x"] - curCenter["x"] ) ** 2 + (center["y"] - curCenter["y"] ) ** 2 )

