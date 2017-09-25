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
    #newname =  imagePath +".jpg"
    #newImage.save(newname)
    im.close()
    binImage = picPreDo(newImage)
    return  pytesseract.image_to_string(binImage, lang="chi_sim", config = " -psm 7") 

def picPreDo(imageHandler):
    Lim = imageHandler.convert("L")
    threshold = 190
    table = [] 
    for i in range(256):
        if i < threshold :
            table.append(0)
        else :
            table.append(1)
    bim  = Lim.point(table,'1')
    #bim.save("xxx.jpg" )
    return bim 
    
    

def getResultFromDir(dirPath):
    testA = []
    failedNum  = 0 
    fp = open("resultOne.txt", "w")
    for root,dirs, files in os.walk(dirPath):
        for filename in files :
            imagePath = os.path.join(root, filename)
            try :
                result = getQuestion(imagePath)
                print result , "xxxx"
                if result :
                    if result not in testA :
                        testA.append(result)
                        fp.write(result + " \r\n")
          
                    else :
                        pass
                else :
                    failedNum = failedNum  + 1
            except Exception as e:
                print str(e)
    print failedNum    
    fp.close()
    



if __name__ =="__main__" :
    imagePath = sys.argv[1]
    getResultFromDir(imagePath)

