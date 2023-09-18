import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Figure Parameters Input
dist_x = 0.08
count_y = 1
count_x = 1
text_gap = 0.5
shapes = 0.02

fig, axe = plt.subplots(figsize=(7, 3.5), dpi=800)
axe.axis([0,2,0.5,5])

#Text gap length
Y = []
for gap_length in range(0,8):
    Y.append(count_y)
    count_y += text_gap
print(Y)

x = []
for gap_dist in range(0,8):
    x.append(count_x)
    count_x += dist_x
print(x)

#Inputs Convert
input_first = "AATTAATT"  # 1. Asagıdan yukarıya
input_second = "TTAATTAA"  # 2. Asagıdan yukarıya (yeşilden sarıya)
input_third = "AATTAATT"  # 3. Asagıdan yukarıya (yeşilden sarıya)
input_fourth = "TTAATTAA" # 4. Asagıdan yukarıya

def split(word):
    return [char for char in word]

seq_first = split(input_first)
seq_second = split(input_second)
seq_third = split(input_third)
seq_fourth = split(input_fourth)

### First Line
axe.vlines(x[0], min(Y)-text_gap/2, max(Y)+text_gap/2, color = (float(68/255),float(114/255),float(196/255)), linewidth= 3)
### First Text
for i in range(0,len(seq_first)):
    axe.text(x[1], Y[i], seq_first[i], color = [float(68/255),float(114/255),float(196/255)], fontsize = 20, weight = 'heavy',family='Courier New', ha='center', va='center', ma ='center')


### End Shapes for first
first_3 = np.array([[x[0]-shapes,max(Y)+text_gap/2], [x[0],max(Y)+text_gap/2+shapes*10], [x[0]+shapes,max(Y)+text_gap/2]])
first_3 = Polygon(first_3, closed=False, color= (float(68/255),float(114/255),float(196/255)))
first_5 = np.array([[x[0]-shapes,x[0]-text_gap/2], [x[0]+shapes,x[0]-text_gap/2], [x[0]+shapes,x[0]-text_gap/2-shapes*10], [x[0]-shapes,x[0]-text_gap/2-shapes*10]])
first_5 = Polygon(first_5, closed=False, color= (float(68/255),float(114/255),float(196/255)))

axe.add_patch(first_3)
axe.add_patch(first_5)

print('First Lines '+ str(x[0]))
print('First Text '+ str(x[1]))

### Second Text
for i in range(0,4):
    axe.text(x[2], Y[i], seq_second[i], color = [float(0),float(176/255),float(80/255)], fontsize = 20, weight = 'heavy',family='Courier New', ha='center', va='center', ma ='center')
for i in range(4,len(seq_second)):
    axe.text(x[2], Y[i], seq_second[i], color = [float(255/255),float(192/255),float(0)], fontsize = 20, weight = 'heavy',family='Courier New', ha='center', va='center', ma ='center')

### Medium Lines

half_y = ((max(Y)+text_gap/2) - (min(Y)-text_gap/2))/2
axe.vlines(x[3], min(Y)-text_gap/2,min(Y)-text_gap/2 + half_y - 0.08, color = (float(0),float(176/255),float(80/255)), linewidth= 3)
axe.vlines(x[3], min(Y)-text_gap/2 + half_y + 0.08, max(Y)+text_gap/2, color = (float(255/255),float(192/255),float(0)), linewidth= 3)

axe.plot([x[3],x[4]],[min(Y)-text_gap/2 + half_y - 0.08, min(Y)-text_gap/2 + half_y - 0.08], color = (float(0),float(176/255),float(80/255)), linewidth= 3)
axe.plot([x[3],x[4]],[min(Y)-text_gap/2 + half_y + 0.08, min(Y)-text_gap/2 + half_y + 0.08], color = (float(255/255),float(192/255),float(0)), linewidth= 3)

second_3 = np.array([[x[3]-shapes,min(Y)-text_gap/2], [x[3]+shapes,min(Y)-text_gap/2], [x[3],min(Y)-text_gap/2-shapes*10]])
second_3 = Polygon(second_3, closed=False, color= (float(0),float(176/255),float(80/255)))
second_5 = np.array([[x[3]-shapes,max(Y)+text_gap/2], [x[3]+shapes,max(Y)+text_gap/2], [x[3]+shapes,max(Y)+text_gap/2+shapes*10], [x[3]-shapes,max(Y)+text_gap/2+shapes*10]])
second_5 = Polygon(second_5, closed=False, color= (float(255/255),float(192/255),float(0)))

axe.add_patch(second_3)
axe.add_patch(second_5)

print('Second Lines ' + str(x[3]))
print('Second Text '+ str(x[4]))

### Third

for i in range(0,4):
    axe.text(x[5], Y[i], seq_third[i], color = [float(0),float(176/255),float(80/255)], fontsize = 20, weight = 'heavy',family='Courier New', ha='center', va='center', ma ='center')
for i in range(4,len(seq_second)):
    axe.text(x[5], Y[i], seq_third[i], color = [float(255/255),float(192/255),float(0)], fontsize = 20, weight = 'heavy',family='Courier New', ha='center', va='center', ma ='center')

axe.vlines(x[4], min(Y)-text_gap/2,min(Y)-text_gap/2 + half_y - 0.08, color = (float(0),float(176/255),float(80/255)), linewidth= 3)
axe.vlines(x[4], min(Y)-text_gap/2 + half_y + 0.08, max(Y)+text_gap/2, color = (float(255/255),float(192/255),float(0)), linewidth= 3)

third_3 = np.array([[x[4]-shapes,max(Y)+text_gap/2], [x[4],max(Y)+text_gap/2+shapes*10], [x[4]+shapes,max(Y)+text_gap/2]])
third_3 = Polygon(third_3, closed=False, color= (float(255/255),float(192/255),float(0)))
third_5 = np.array([[x[4]-shapes,min(Y)-text_gap/2], [x[4]+shapes,min(Y)-text_gap/2], [x[4]+shapes,min(Y)-text_gap/2-shapes*10], [x[4]-shapes,min(Y)-text_gap/2-shapes*10]])
third_5 = Polygon(third_5, closed=False, color= (float(0),float(176/255),float(80/255)))

axe.add_patch(third_3)
axe.add_patch(third_5)

print('Third Lines ' + str(x[4]))
print('Third Text '+ str(x[5]))

### Fourth

for i in range(0,len(seq_first)):
    axe.text(x[6], Y[i], seq_fourth[i], color = [float(68/255),float(114/255),float(196/255)], fontsize = 20, weight = 'heavy',family='Courier New', ha='center', va='center', ma ='center')

axe.vlines(x[7], min(Y)-text_gap/2, max(Y)+text_gap/2, color = (float(68/255),float(114/255),float(196/255)), linewidth= 3)

fourth_3 = np.array([[x[7]-shapes,min(Y)-text_gap/2], [x[7]+shapes,min(Y)-text_gap/2], [x[7],min(Y)-text_gap/2-shapes*10]])
fourth_3 = Polygon(fourth_3, closed=False, color= (float(68/255),float(114/255),float(196/255)))
fourth_5 = np.array([[x[7]-shapes,max(Y)+text_gap/2], [x[7]-shapes,max(Y)+text_gap/2+shapes*10], [x[7]+shapes,max(Y)+text_gap/2+shapes*10], [x[7]+shapes,max(Y)+text_gap/2]])
fourth_5 = Polygon(fourth_5, closed=False, color= (float(68/255),float(114/255),float(196/255)))

axe.add_patch(fourth_3)
axe.add_patch(fourth_5)

print('Fourth Lines ' + str(x[6]))
print('Fourth Texts ' + str(x[7]))

## Output

fig.gca().set_axis_off()
#fig.subplots_adjust(top = 0.45, bottom = 0, right = 0.5, left = 0, hspace = 0, wspace = 0)
fig.gca().xaxis.set_major_locator(plt.NullLocator())
fig.gca().yaxis.set_major_locator(plt.NullLocator())
fig.savefig("sequence.png", bbox_inches = 'tight', pad_inches = 0, dpi=1000, transparent='True')


from PIL import Image
im = Image.open("sequence.png")
im.size
im.getbbox()
im2 = im.crop(im.getbbox())
im2.size
im2.save("sequence.png")

