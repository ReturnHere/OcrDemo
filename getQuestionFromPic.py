coding="utf-8"

"""
author = gaokun.cug@gmail.com
"""

from  PIL import Image
from PIL import ImageFilter
import pytesseract
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

def getQuestion(imagePath):
    im  = Image.open(imagePath)
    newImage = im.crop((120,0,293,30))
    newname =  imagePath +".jpg"
    newImage.save(newname)
    im.close()
    return  pytesseract.image_to_string(newImage , lang="chi_sim", config = " -psm 7") , newname

def getResultFromDir(dirPath):
    testA = []
    failedNum  = 0 
    testB = []
    fp = open("resultOne.txt", "w")
    wp  = open("resultTwo.txt", "w")
    for root,dirs, files in os.walk(dirPath):
       for filename in files :
           imagePath = os.path.join(root, filename)
           result = getQuestion(imagePath)
           if result :
               if result[0] not in testA :

                   testA.append(result[0])
                   fp.write(result[0] + " \r\n")
                   cmd  = "tesseract  " + result[1] + " test -l chi_sim "
                   os.system(cmd)
                   zp = open("test.txt","r")
                   question = zp.read().strip()
                   if question not in testB :
                       wp.write(question + "\r\n")
                       os.remove("test.txt")
                   zp.close()
                   os.remove(result[1])

                   
               else :
                   pass
           else :
               failedNum = failedNum  + 1

    print failedNum 
     
    fp.close()
    wp.close()



if __name__ =="__main__" :
    imagePath = sys.argv[1]
    getResultFromDir(imagePath)

