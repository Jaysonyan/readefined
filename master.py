import math
import json
import subprocess
import Foundation
from subprocess import Popen, PIPE
import os

centerx = 735/2
centery = 1102/2
#process = subprocess.Popen(['../../google-cloud-sdk/bin/gcloud', 'ml', 'vision', 'detect-text', 'test.jpg'], stdout=subprocess.PIPE)
process = subprocess.Popen(['gcloud', 'ml', 'vision', 'detect-text', './Documents/shot.jpg'], stdout=subprocess.PIPE)

wordsArr, err = process.communicate()
wordsArr = json.loads(wordsArr)["responses"][0]["textAnnotations"][1:]
#print wordsArr

for words in wordsArr:
  word = words["description"]
  vertices = words["boundingPoly"]["vertices"]
  if(vertices[0]["x"] < centerx and vertices[0]["y"] < centery):
      if(vertices[1]["x"] > centerx and vertices[1]["y"] < centery):
          if(vertices[2]["x"] > centerx and vertices[2]["y"] > centery):
              if(vertices[3]["x"] < centerx and vertices[3]["y"] > centery):
                  print word
                  os.system("say " + word)
                  break


