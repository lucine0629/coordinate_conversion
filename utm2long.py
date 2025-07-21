# %%
### This script converts UTM coordinate to LATlONG

import utm
import os
#import nbconvert


#define file name
inpshot = 'obx_sps_SEM4.r01'
outshot = 'sem4_obx_loc.txt'

#Check existence of output file.
#If output file exists, remove it.
if os.path.isfile(outshot):
    os.remove(outshot)

#read the file
tmp = open(inpshot, "r")
data = tmp.read().split('\n')


with open(outshot, 'a') as f:
    header = "obx,utmlon,utmlat,lon,lat"
    f.write(header + "\n")

    
nodes = list("#A_CN{0}".format(i) for i in range(1,180))    
    
#coordinate conversion
for a ,element in enumerate(data):
#     a1 = data[a].split(',')   ## if delimeter is comma
    a1 = data[a].split()   ## if delimeter is space
    utmlon = float(a1[1])
    utmlat = float(a1[2])
    obx = int(a1[0])
    tmpy,tmpx = utm.to_latlon(utmlon, utmlat, 23, 'R')
    y = round(tmpy, 6)
    x = round(tmpx, 6)
    with open(outshot, 'a') as f:
        outp = str(utmlon)+str('\t')+str(utmlat)+str('\t')+str(x)+str('\t')+str(y)+str('\t')+str(obx)
        f.write("%s\n" % outp)

# %%
### This script converts UTM coordinate to LATlONG

# import utm
# import os
# import nbconvert


# #define file name
# inpshot = 'Semenov5.gmt'
# outshot = 'Semenov5.txt'

# #Check existence of output file.
# #If output file exists, remove it.
# if os.path.isfile(outshot):
#     os.remove(outshot)

# #read the file
# tmp = open(inpshot, "r")
# data = tmp.read().split('\n')

# with open(outshot, 'a') as f:
#     header = "lon,lat,distance"
#     f.write(header + "\n")

# #coordinate conversion
# for a ,element in enumerate(data):
# #     a1 = data[a].split(',')   ## if delimeter is comma
#     a1 = data[a].split()   ## if delimeter is space
#     utmlon = float(a1[0])
#     utmlat = float(a1[1])
# #     dist = float(a1[2])/1000
#     #print(utmlon,utmlat)
#     tmpy,tmpx = utm.to_latlon(utmlon, utmlat, 23, 'R')
#     y = round(tmpy, 6)
#     x = round(tmpx, 6)
#     with open(outshot, 'a') as f:
# #         outp = str(x)+str(',')+str(y)+str(',')+str(dist)
#         outp = str(x)+str(',')+str(y)
#         f.write("%s\n" % outp)

# %%
print(utmlon,utmlat,x,y)

# %%
