import math
import json
import subprocess
from subprocess import Popen, PIPE
import os

centreX = 735/2
centreY = 1102/2
#process = subprocess.Popen(['../../google-cloud-sdk/bin/gcloud', 'ml', 'vision', 'detect-text', 'test.jpg'], stdout=subprocess.PIPE)
process = subprocess.Popen(['gcloud', 'ml', 'vision', 'detect-text', 'image.jpg'], stdout=subprocess.PIPE)

wordsArr, err = process.communicate()
wordsArr = json.loads(wordsArr)["responses"][0]["textAnnotations"][1:]
print wordsArr

for words in wordsArr:
  word = words["description"]
  vertices = words["boundingPoly"]["vertices"]
  if(vertices[0]["x"] < centreX and vertices[0]["y"] < centreY):
      if(vertices[1]["x"] > centreX and vertices[1]["y"] < centreY):
          if(vertices[2]["x"] > centreX and vertices[2]["y"] > centreY):
              if(vertices[3]["x"] < centreX and vertices[3]["y"] > centreY):
                  print word
                  os.system("say " + word)
                  break


