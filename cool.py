import image
import pandas
# input the image name via command line
name = input("what is your filename?: ")
# check if the image name is valid or not. if valid, continue to the next step!
# use PIL for image manipulation
readmode=True
from PIL import Image
while readmode:
    try:
        img = Image.open(name)
        readmode = False
    except:
        print("can not read", name)
        print("please input your file name again: ")
        name = input("what is your filename?:")
# resize the image
basewidth = 100
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
# convert the image into an array object
# I also convert the image into a pandas DataFrame because I'm going to convert it into an excel file
import numpy as np
arr = np.array(img)
arr_container = np.empty((arr.shape[0], arr.shape[1]), dtype=np.str)
import pandas as pd
df = pd.DataFrame(arr_container)
# convert the R,G,B into hexadecimal
# populate the DataFrame with the hexadecimal value
for l,x in enumerate(arr):
    for m,y in enumerate(x):
        r,g,b = arr[l][m]
        hexval = '%02x%02x%02x' % (r, g, b)
        df[m][l] = hexval
# save it! yeay!
save_file_name = input("your excel file name, without '.xlsx' please: ")
df.to_excel(str(save_file_name) + ".xlsx")
print("success!! now colour the file")