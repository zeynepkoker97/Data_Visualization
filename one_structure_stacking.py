#!/usr/bin/env python
# coding: utf-8

from shapely.geometry import Point, Polygon
import math
import shapely.geometry
import shapely.wkt
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import glob
from PIL import Image
import matplotlib.font_manager as font_manager
from matplotlib import cm
from matplotlib.colors import ListedColormap,LinearSegmentedColormap
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

#determinant of matrix a
def det(a):
    return a[0][0]*a[1][1]*a[2][2] + a[0][1]*a[1][2]*a[2][0] + a[0][2]*a[1][0]*a[2][1] - a[0][2]*a[1][1]*a[2][0] - a[0][1]*a[1][0]*a[2][2] - a[0][0]*a[1][2]*a[2][1]

#unit normal vector of plane defined by points a, b, and c
def unit_normal(a, b, c):
    x = det([[1,a[1],a[2]],
             [1,b[1],b[2]],
             [1,c[1],c[2]]])
    y = det([[a[0],1,a[2]],
             [b[0],1,b[2]],
             [c[0],1,c[2]]])
    z = det([[a[0],a[1],1],
             [b[0],b[1],1],
             [c[0],c[1],1]])
    magnitude = (x**2 + y**2 + z**2)**.5
    return (x/magnitude, y/magnitude, z/magnitude)

#dot product of vectors a and b
def dot(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

#cross product of vectors a and b
def cross(a, b):
    x = a[1] * b[2] - a[2] * b[1]
    y = a[2] * b[0] - a[0] * b[2]
    z = a[0] * b[1] - a[1] * b[0]
    return (x, y, z)

#area of polygon poly
def area(poly):
    if len(poly) < 3: # not a plane - no area
        return 0
    total = [0, 0, 0]
    for i in range(len(poly)):
        vi1 = poly[i]
        if i is len(poly)-1:
            vi2 = poly[0]
        else:
            vi2 = poly[i+1]
        prod = cross(vi1, vi2)
        total[0] += prod[0]
        total[1] += prod[1]
        total[2] += prod[2]
    result = dot(total, unit_normal(poly[0], poly[1], poly[2]))
    return abs(result/2)


def Stacking(Stacking_input_file, Stacking_output_file):
    stacking = open(Stacking_input_file,'r')
    stacking_out = open(Stacking_output_file,'w')
    frames = stacking.readlines()
    percentage_matrix = []
    for i in range(0,len(frames)):
        frames[i] = frames[i].replace('{','')
        frames[i] = frames[i].replace('}','')
        frames[i] = frames[i].split(',')
        for j in range(0,len(frames[i])):
            numbers = frames[i][j].split()
            for n in range(0,len(numbers)):
                numbers[n] = float(numbers[n])
            polygon = []
            for m in range(0,len(numbers),3):
                polygon.append((numbers[m],numbers[m+1],numbers[m+2]))
            frames[i][j] = polygon
        percentage_array = []
        for k in range(0,len(frames[i])-1):
            poly1 = Polygon(frames[i][k])
            poly2 = Polygon(frames[i][k+1])
            poly1 = poly1.buffer(0)
            poly2 = poly2.buffer(0)
            isIntersection = poly1.intersection(poly2)
            shapely.geometry.GeometryCollection([poly1, poly2])
            percentage = (isIntersection.area/poly2.area)*100
            percentage_array.append(percentage)
        percentage_matrix.append(percentage_array)

    transposed_matrix = []

    for i in range(0,len(percentage_matrix[0])):
        zero_temp = []
        for j in range(0,len(percentage_matrix)):
            zero_temp.append(0)
        transposed_matrix.append(zero_temp)

    for i in range(0,len(percentage_matrix)):
        for j in range(0,len(percentage_matrix[0])):
            transposed_matrix[j][i] = percentage_matrix[i][j]

    stacking_out.write(str(transposed_matrix))

    stacking.close()
    stacking_out.close()
    return transposed_matrix

def threeDimensionPlot(Stacking_input_file1, Stacking_input_file2, figure_png):
    stacking = open(Stacking_input_file1,'r')
    frames = stacking.readlines()
    stacking2 = open(Stacking_input_file2,'r')
    frames2 = stacking2.readlines()
    for i in range(0,len(frames)):
        X = []
        Y = []
        Z = []
        frames[i] = frames[i].replace('{','')
        frames[i] = frames[i].replace('}','')
        frames[i] = frames[i].split(',')
        X2 = []
        Y2 = []
        Z2 = []
        frames2[i] = frames2[i].replace('{','')
        frames2[i] = frames2[i].replace('}','')
        frames2[i] = frames2[i].split(',')
        for j in range(0,len(frames[i])):
            x = []
            y = []
            z = []
            numbers = frames[i][j].split()
            x2 = []
            y2 = []
            z2 = []
            numbers2 = frames2[i][j].split()
            for n in range(0,len(numbers)):
                numbers[n] = float(numbers[n])
                numbers2[n] = float(numbers2[n])
            for m in range(0,len(numbers),3):
                x.append(numbers[m])
                y.append(numbers[m+1])
                z.append(numbers[m+2])
                x2.append(numbers2[m])
                y2.append(numbers2[m+1])
                z2.append(numbers2[m+2])
            X.append(x)
            Y.append(y)
            Z.append(z)
            X2.append(x2)
            Y2.append(y2)
            Z2.append(z2)
        fig = plt.figure(figsize=(5,5))
        ax = fig.add_subplot(111, projection='3d')
        for j in range(0,len(X)):
            fig.add_axes(ax)
            x = X[j]
            y = Y[j]
            z = Z[j]
            verts = [list(zip(x,y,z))]
            ax.scatter(x, y, z)
            ax.add_collection3d(Poly3DCollection(verts, alpha = 0.5))
            ax.view_init(90, 180)
        for j in range(0,len(X)):
            fig.add_axes(ax)
            x2 = X2[j]
            y2 = Y2[j]
            z2 = Z2[j]
            verts2 = [list(zip(x2,y2,z2))]
            ax.scatter(x2, y2, z2)
            ax.add_collection3d(Poly3DCollection(verts2, alpha = 0.5, facecolor= 'red'))
            #ax.view_init(0, 90) #yandan
            ax.view_init(90, 180) #üstten
            ax.set_title("Stacking Plotting" + '\n' + str(figure_png))
        #ax.plot(x,y,z, label= Stacking_input_file1)
        #ax.legend(loc="lower right")
        #ax.plot(x2,y2,z2, label= Stacking_input_file2)
        #ax.legend(loc="lower right")
        plt.savefig(figure_png, pad_inches = 0)
        plt.show()

def Stacking_Graph(main_strand, axes, transposed_matrix, file_name_png):
    plt.figure(figsize=(25,4))
    ax = sns.heatmap(transposed_matrix,cmap='seismic', cbar = False)
    sns.heatmap(transposed_matrix,cmap='seismic', vmin=0, vmax=100 )
    Time = ['0', '10', '20', '30', '40', '50']
    plt.xticks([0,5000,10000,15000,20000,25000],Time,rotation=0,fontsize='18')
    plt.yticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5], reversed(axes), rotation=0, family = "monospace", fontsize='18', va='center')
    font_seq = font_manager.FontProperties(family='Courier New',weight='bold',style='normal', size=20)
    font = font_manager.FontProperties(weight='bold',style='normal', size=20)
    ax.set_title(main_strand, font=font_seq)
    plt.ylabel('Strands',font=font)
    plt.xlabel('Time (ns)',font=font)
    plt.savefig(file_name_png, bbox_inches = 'tight', pad_inches = 0)
    plt.grid()
    im = Image.open(file_name_png)
    im.size
    im.getbbox()
    im2 = im.crop(im.getbbox())
    im2.size
    im2.save(file_name_png)
    plt.show()


#    plt.savefig(file_name_png)

def readSeq(seq_txt_file):
    seq_matrix = []
    axes = []
    with open(seq_txt_file) as my_file:
        for line in my_file:
            line = line.replace('\n','')
            seq_matrix.append(line)
    for each_seq in seq_matrix:
        letter_axes = []
        for i in range(0,len(each_seq)-1):
            letter_axes.append(each_seq[i] + each_seq[i+1])
        axes.append(list(letter_axes))
    return seq_matrix, axes

def comp_strand(X):
    new_list = []
    for base in X:
        if base == 'A':
            new_list.append('T')
        elif base == 'T':
            new_list.append('A')
        elif base == 'G':
            new_list.append('C')
        elif base == 'C':
            new_list.append('G')
    return new_list

main_strand, axes = readSeq('sequence_list.txt')

#transposed_matrix_03 = Stacking('S1-AT-BaseCenters1.dat','S1-AT-stacking-Helix1.dat')
#threeDimensionPlot('S1-AT-BaseCenters1.dat','S1-AT-BaseCenters2.dat')
#Stacking_Graph(main_strand[0], axes[0], transposed_matrix_03, 'S1-AT-Stacking-Helix1.png') #başarılı

for i in range(1,7):
    for j in range(1,5):
        if j%2==1:
            Stacking('S'+str(i)+'-AT-BaseCenters'+str(j)+'.dat','S'+str(i)+'-AT-stacking-Helix'+str(math.ceil(j/2))+'_left.dat')
            Stacking('S'+str(i)+'-GC-BaseCenters'+str(j)+'.dat','S'+str(i)+'-GC-stacking-Helix'+str(math.ceil(j/2))+'_left.dat')
            threeDimensionPlot('S'+str(i)+'-AT-BaseCenters'+str(j)+'.dat','S'+str(i)+'-AT-BaseCenters'+str(j+1)+'.dat', 'S'+str(i)+'-AT-Helix'+str(math.ceil(j/2)))
            threeDimensionPlot('S'+str(i)+'-GC-BaseCenters'+str(j)+'.dat','S'+str(i)+'-GC-BaseCenters'+str(j+1)+'.dat', 'S'+str(i)+'-GC-Helix'+str(math.ceil(j/2)))
        else:
            Stacking('S'+str(i)+'-AT-BaseCenters'+str(j)+'.dat','S'+str(i)+'-AT-stacking-Helix'+str(math.ceil(j/2))+'_right.dat')
            Stacking('S'+str(i)+'-GC-BaseCenters'+str(j)+'.dat','S'+str(i)+'-GC-stacking-Helix'+str(math.ceil(j/2))+'_right.dat')






'''
main_strand, axes = readSeq('third_sequence_list.txt')

transposed_matrix_03 = Stacking('TM9_03_Stacking1.dat','TM9_03_stacking_percentage_buffer.dat')
Stacking_Graph(main_strand[0], axes[0], transposed_matrix_03, 'TM9_03_stacking_percentage_buffer.png') #başarılı


for file_name in glob.glob("*_Stacking1.dat"):
    file = file_name.replace('_Stacking1.dat','')
    transposed_matrix = Stacking(file_name,file + '_stacking1_percentage.dat')
    for i in range(0,len(seq_txt)):
        Stacking_Graph(seq, transposed_matrix, file + '_stacking1_percentage.png') 


for file_name in glob.glob("*_Stacking2.dat"):
    file = file_name.replace('_Stacking2.dat','')
    transposed_matrix = Stacking(file_name,file + '_stacking2_percentage.dat')
    Stacking_Graph(transposed_matrix, file + '_stacking2_percentage.png')
'''
