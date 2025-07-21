# %%
### This script converts LONLAT 2 UTM coordinate

import utm
import os
import nbconvert


#define file name
inpshot = 'allobx_depth.txt'
outshot = 'utm_allobx_depth.txt'

#Check existence of output file.
#If output file exists, remove it.
if os.path.isfile(outshot):
    os.remove(outshot)

#read the file
tmp = open(inpshot, "r")
data = tmp.read().split('\n')

with open(outshot, 'a') as f:
#     header = "long,lat,shot_num,easting,northing,zone_number"
    header = "long,lat,depth,easting,northing,obx_num, depth(km), zone_number"
    f.write(header + "\n")

#coordinate conversion
for a ,element in enumerate(data):
    a1 = data[a].split()
    lon = round(float(a1[0]),6)
    lat = round(float(a1[1]),6)
    obx = a1[2]
    depth = round(float(a1[3])/-1000,3)
    x,y,zn,zl = utm.from_latlon(lat,lon)
    fn_x = round(float(x))
    fn_y =round(float(y))
    
    
    with open(outshot, 'a') as f:
        outp = str(lon)+str(',')+str(lat)+(',')+str(obx)+str(',')+str(fn_x)+str(',')+str(fn_y)+str(',')+str(depth)+str(',')+str(zn)+str(zl)
        f.write("%s\n" % outp)

# %%
print(lon,lat,obx,fn_x,fn_y,depth)

# %%
