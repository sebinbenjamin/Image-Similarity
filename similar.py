import argparse
import numpy as np
import sys
from SimpleCV import Image

parser = argparse.ArgumentParser()
parser.add_argument("URL_of_Image_1")
parser.add_argument("URL_of_Image_2")

args = parser.parse_args()    
total = len(sys.argv)
if total != 3 :
    sys.exit("Error: Enter URL of 2 images")
    
url1 = sys.argv[1]
url2 = sys.argv[2]        
img1 = Image(url1)    
img2 = Image(url2)

diff=img1 - img2
matrix = diff.getNumpy()
flat = matrix.flatten()
numchange = np.count_nonzero(flat)
percentchange = 100 * float(numchange) / float(len(flat))
if percentchange == 0:
    diff = img1 - img2
    matrix = diff.getNumpy()
    flat = matrix.flatten()
    numchange = np.count_nonzero(flat)
    percentchange = 100 * float(numchange) / float(len(flat))

print 'Similarity :',round(100 - percentchange,2),'%'
