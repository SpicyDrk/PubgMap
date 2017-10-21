from PIL import Image
import csv
import json

#im = Image.open('images\heatmapLit.png')
#im = Image.open('images\heatmapNormal.png')
im = Image.open('images\heatmapRandom.png')
pix=im.load()
print im.size


pix_val = list(im.getdata())
alpha_pix_val = zip(*pix_val)
alpha_pix_val = alpha_pix_val[3]
alpha_pix_val = map(str, alpha_pix_val)
location=0
alpha_pix_val_comb=[]
alpha_pix_val_comb_JSON=[]

for y in range(80):
    for x in range(80):
        location += 1
        alpha_pix_val_comb.append([x+1,y+1,int(alpha_pix_val[location-1])])
        alpha_pix_val_comb_JSON.append({"x":(x+1),"y":(y+1),"value":int(alpha_pix_val[location-1])})
print alpha_pix_val_comb

#        d["x"]=x+1
#        d["y"]=y+1
#        d["alpha"] = alpha_pix_val[location-1]


with open('heatmapRandom.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(['x','y','alpha'])
    writer.writerows(alpha_pix_val_comb)
   
    

#pix_val.append((255,255,255,0))


#write directly to json
#Get the file name for the new file to write
with open('json/heatmapRandom.json','w') as outfile:
    json.dump(alpha_pix_val_comb_JSON,outfile)