import time
from matplotlib import animation
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

fig, ax = plt.subplots()
ax.set(xlim=(-1, 1), ylim=(-1, 1))

string = []

final_frame = 25000
showed_time_count_step = 0.25
count = 0
for i in range(0,int((final_frame*0.002/showed_time_count_step)+showed_time_count_step)):
    string.append(str('%.2f'%(count)) + ' ns')
    count = count + showed_time_count_step

label = ax.text(0, 0, string[0], ha='center', va='center', fontsize=20, color="black")

def animate(i):
    label.set_text(string[i])
    time.sleep(0.5)

anim = animation.FuncAnimation(fig, animate, interval=200, frames=int(final_frame/50))
ax.axis('off')
plt.show()

