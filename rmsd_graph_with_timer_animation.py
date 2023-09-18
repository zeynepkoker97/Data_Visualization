from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

x = []
y = []
X = []
Y = []

fig, ax = plt.subplots()
string = []
final_frame = 25000
showed_time_count_step = 0.25
count = 0
for i in range(0,int((final_frame*0.002/showed_time_count_step)+showed_time_count_step)):
    string.append(str('%.2f'%(count)) + ' ns')
    count = count + showed_time_count_step

def animate(i):
    for line in open('MD_Model3_bsc1/analysis/RMSD.dat','r'):
        values = [float(s) for s in line.split( )]
        x.append(values[0])
        y.append(values[1])
    X.append(x[i*125])
    Y.append(y[i*125])
    ax.clear()
    ax.plot(X, Y)
    ax.set_xlim([0,50])
    ax.set_ylim([0,10])
    ax.text(40, 9, string[i], ha='center', va='center', fontsize=12, color="black")

anim = animation.FuncAnimation(fig, animate, frames = 200, interval = 20, repeat=False)
plt.show()
plt.rcParams['animation.ffmpeg_path'] = [r'C:\Users\user\ffmpeg-2023-02-27-git-891ed24f77-full_build\bin\ffmpeg.exe']
Writer = animation.writers[r'C:\Users\user\ffmpeg-2023-02-27-git-891ed24f77-full_build\bin\ffmpeg.exe']
writer = Writer(fps=15)
anim.save('Line Graph Animation.mp4', writer)
