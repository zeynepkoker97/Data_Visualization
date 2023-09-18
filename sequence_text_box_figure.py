import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
#Color Palette:
# ec= mavi_dis_kenarlik ---> (float(68/255),float(114/255),float(196/255))
# ec= sari_dis_kenarlik ---> (float(255/255),float(192/255),float(0))
# ec= yesil_dis_kenarlik ---> (float(0),float(176/255),float(80/255))
#---------------------------------------------------------------------------
# fc= mavi_ic ---> (float(189/255),float(215/255),float(238/255))
# fc= sari_ic ---> (float(255/255),float(230/255),float(153/255))
# fc= yesil_ic ---> (float(197/255),float(224/255),float(180/255))
# fc= beyaz_ic ---> (float(255/255),float(255/255),float(255/255))

X = []
#Inputs Convert
input_left = "ZTTTTTTT"  #En soldaki en aşağıdan en üste
input_upper = "ZTTTAAAA"  #Üst ortadaki sol üstten başlayarak sırayla
input_lower = "ZTTTAAAA"  #Alt ortadaki sol alttan başlayarak sırayla
input_right = "ZTTTTTTT" #En sağdaki en aşağıdan en yukarı

def split(word):
    return [char for char in word]

seq_left = split(input_left)
seq_upper = split(input_upper)
seq_lower = split(input_lower)
seq_right = split(input_right)

#Plotting Starts
fig = plt.figure()
ax = fig.add_subplot()
ax.axis([0.1,0.3,0.1,0.8])

count = 0.2
for gap_length in range(0,8):
    X.append(count)
    count += 0.06
print(X)

#Left

ec_color_array_left = []
fc_color_array_left = []

for m in range(0,len(seq_left)):
    if seq_left[m] == "G" or seq_left[m] == "A":
        ec_color_array_left.append((float(68/255),float(114/255),float(196/255)))
        fc_color_array_left.append((float(189/255),float(215/255),float(238/255)))
    else:
        ec_color_array_left.append((float(68/255),float(114/255),float(196/255)))
        fc_color_array_left.append((float(255/255),float(255/255),float(255/255)))

for i in range(0,4):
    ax.text(0.20, X[i], seq_left[i], size=10, rotation=0., family='Courier New', weight='heavy', style='normal',
                ha="center", va="center", ma ="center", wrap=True,
                bbox=dict(boxstyle="square",
                          ec=ec_color_array_left[i],
                          fc=fc_color_array_left[i]
                          )
                )
for i in range(4,len(X)):
    ax.text(0.20, X[i]+0.02, seq_left[i], size=10, rotation=0., family='Courier New', weight='heavy', style='normal',
                ha="center", va="center", ma="center",wrap=True,
                bbox=dict(boxstyle="square",
                          ec=ec_color_array_left[i],
                          fc=fc_color_array_left[i]
                          )
                )

#ax.text(0.20, 0.2-0.05, '5\'', size=10, rotation=0., weight='heavy', style='normal', ha="center", va="center")
#ax.text(0.20, max(X)+0.06, '3\'', size=10, rotation=0., weight='heavy', style='normal', ha="center", va="center")

ax.vlines(0.20, 0.2-0.03, 0.67, color = (float(68/255),float(114/255),float(196/255)))

left_3 = np.array([[0.198,0.67], [0.202,0.67], [0.2,0.69]])
left_3 = Polygon(left_3, closed=False, color= (float(68/255),float(114/255),float(196/255)))
left_5 = np.array([[0.198,0.2-0.05], [0.198,0.2-0.03], [0.202,0.2-0.03], [0.202,0.2-0.05]])
left_5 = Polygon(left_5, closed=False, color= (float(68/255),float(114/255),float(196/255)))

ax.add_patch(left_3)
ax.add_patch(left_5)

#Right

ec_color_array_right = []
fc_color_array_right = []

for m in range(0,len(seq_left)):
    if seq_left[m] == "G" or seq_left[m] == "A":
        ec_color_array_right.append((float(68/255),float(114/255),float(196/255)))
        fc_color_array_right.append((float(189/255),float(215/255),float(238/255)))
    else:
        ec_color_array_right.append((float(68/255),float(114/255),float(196/255)))
        fc_color_array_right.append((float(255/255),float(255/255),float(255/255)))

for i in range(0,4):
    ax.text(0.23, X[i], seq_right[i], size=10, rotation=0., family='Courier New', weight='heavy', style='normal',
            ha="center", va="center", ma ="center", wrap=True,
            bbox=dict(boxstyle="square",
                      ec=ec_color_array_right[i],
                      fc=fc_color_array_right[i]
                      )
            )
for i in range(4,len(X)):
    ax.text(0.23, X[i]+0.02, seq_right[i], size=10, rotation=0., family='Courier New', weight='heavy', style='normal',
            ha="center", va="center", ma="center",wrap=True,
            bbox=dict(boxstyle="square",
                      ec=ec_color_array_right[i],
                      fc=fc_color_array_right[i]
                      )
            )
#ax.text(0.23, max(X)+0.06, '5\'', size=10, rotation=0., weight='heavy', style='normal', ha="center", va="center")
#ax.text(0.23, 0.2-0.05, '3\'', size=10, rotation=0., weight='heavy', style='normal', ha="center", va="center")

right_3 = np.array([[0.228,0.2-0.03], [0.232,0.2-0.03], [0.23,0.2-0.05]])
right_3 = Polygon(right_3, closed=False, color= (float(68/255),float(114/255),float(196/255)))
right_5 = np.array([[0.228,0.67], [0.228,0.69], [0.232,0.69], [0.232,0.67]])
right_5 = Polygon(right_5, closed=False, color= (float(68/255),float(114/255),float(196/255)))

ax.add_patch(right_3)
ax.add_patch(right_5)


ax.vlines(0.23, 0.2-0.03, 0.67, color = (float(68/255),float(114/255),float(196/255)))

#Ic kisim

ec_color_array_upper = []
ec_color_array_lower = []
fc_color_array_upper = []
fc_color_array_lower = []

#UPPER

for m in range(0,len(seq_upper)):
    if seq_upper[m] == "G" or seq_upper[m] == "A":
        ec_color_array_upper.append((float(255/255),float(192/255),float(0)))
        fc_color_array_upper.append((float(255/255),float(230/255),float(153/255)))
    else:
        ec_color_array_upper.append((float(255/255),float(192/255),float(0)))
        fc_color_array_upper.append((float(255/255),float(255/255),float(255/255)))

for i in reversed(range(4,len(X))):
    ax.text(0.21, X[i]+0.02, seq_upper[-i-1], size=10, rotation=0., family='Courier New', weight='heavy', style='normal',
            ha="center", va="center", ma ="center", wrap=True,
            bbox=dict(boxstyle="square",
                      ec=ec_color_array_upper[-i-1],
                      fc=fc_color_array_upper[-i-1]
                      )
            )
for i in (range(4,len(X))):
    ax.text(0.22, X[i]+0.02, seq_upper[i], size=10, rotation=0., family='Courier New', weight='heavy', style='normal',
            ha="center", va="center", ma="center",wrap=True,
            bbox=dict(boxstyle="square",
                      ec=ec_color_array_upper[i],
                      fc=fc_color_array_upper[i]
                      )
            )
#ax.text(0.22, max(X)+0.06, '3\'', size=10, rotation=0., weight='heavy', style='normal', ha="center", va="center")
#ax.text(0.21,  max(X)+0.06, '5\'', size=10, rotation=0., weight='heavy', style='normal', ha="center", va="center")

ax.vlines(0.21, 0.67, X[4]+0.02, color = (float(255/255),float(192/255),float(0)))
ax.vlines(0.22, X[4]+0.02, 0.67, color = (float(255/255),float(192/255),float(0)))

ax.plot([0.21,0.22],[X[4]+0.02, X[4]+0.02], color = ((float(255/255),float(192/255),float(0))))

upper_3 = np.array([[0.218,0.67], [0.222,0.67], [0.22,0.69]])
upper_3 = Polygon(upper_3, closed=False, color= (float(255/255),float(192/255),float(0)))
upper_5 = np.array([[0.208,0.67], [0.208,0.69], [0.212,0.69], [0.212,0.67]])
upper_5 = Polygon(upper_5, closed=False, color= (float(255/255),float(192/255),float(0)))

ax.add_patch(upper_3)
ax.add_patch(upper_5)


#LOWER

for m in range(0,len(seq_lower)):
    if seq_lower[m] == "G" or seq_lower[m] == "A":
        ec_color_array_lower.append((float(0),float(176/255),float(80/255)))
        fc_color_array_lower.append((float(197/255),float(224/255),float(180/255)))
    else:
        ec_color_array_lower.append((float(0),float(176/255),float(80/255)))
        fc_color_array_lower.append((float(255/255),float(255/255),float(255/255)))

for i in range(0,4):
    ax.text(0.21, X[i], seq_lower[i], size=10, rotation=0., family='Courier New', weight='heavy', style='normal',
            ha="center", va="center", ma ="center", wrap=True,
            bbox=dict(boxstyle="square",
                      ec=ec_color_array_lower[i],
                      fc=fc_color_array_lower[i]
                      )
            )
for i in reversed(range(0,4)):
    ax.text(0.22, X[i], seq_lower[-i-1], size=10, rotation=0., family='Courier New', weight='heavy', style='normal',
            ha="center", va="center", ma="center",wrap=True,
            bbox=dict(boxstyle="square",
                      ec=ec_color_array_lower[-i-1],
                      fc=fc_color_array_lower[-i-1]
                      )
            )
#ax.text(0.22, 0.2-0.05, '5\'', size=10, rotation=0., weight='heavy', style='normal', ha="center", va="center")
#ax.text(0.21, 0.2-0.05, '3\'', size=10, rotation=0., weight='heavy', style='normal', ha="center", va="center")

ax.vlines(0.22, X[3], 0.2-0.03, color = ((float(0),float(176/255),float(80/255))))
ax.vlines(0.21, 0.2-0.03, X[3], color = ((float(0),float(176/255),float(80/255))))

ax.plot([0.21,0.22],[X[3],X[3]], color = ((float(0),float(176/255),float(80/255))))


lower_3 = np.array([[0.208,0.2-0.03], [0.212,0.2-0.03], [0.21,0.2-0.05]])
lower_3 = Polygon(lower_3, closed=False, color= (float(0),float(176/255),float(80/255)))
lower_5 = np.array([[0.218,0.2-0.05], [0.218,0.2-0.03], [0.222,0.2-0.03], [0.222,0.2-0.05]])
lower_5 = Polygon(lower_5, closed=False, color= (float(0),float(176/255),float(80/255)))

ax.add_patch(lower_3)
ax.add_patch(lower_5)


#plt.show()

#çizdirme

fig.gca().set_axis_off()
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
