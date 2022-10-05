from PIL import Image
import sys
filename=sys.argv[1]
logo=Image.open(filename)
logo.save(filename.split('.')[0]+'.ico',format='ICO')