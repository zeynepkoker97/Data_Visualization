import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def DataRead(Filename):
    with open(Filename, 'r') as f:
        data = [[float(num) for num in line.split(',')] for line in f]
        data = np.array(data)
    return data

fig, ax = plt.subplots()
def heatmap(data, ax=None, cbar_kw={}, **kwargs):
    if not ax:
        ax = plt.gca()

    im = ax.imshow(data, vmin=0, vmax=100, **kwargs)
    cbar = ax.figure.colorbar(im, ax = ax, **cbar_kw)
    cbar.ax.tick_params(labelsize=12)

    ax.spines[:].set_visible(False)
    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="black", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    plt.rcParams["axes.grid"] = True
    plt.axis('off')

    return im, cbar

def annotate_heatmap(im, data=None, valfmt="{x:.2f}", textcolors=("black", "white"), threshold=60, **textkw):
    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.
    kw = dict(horizontalalignment="center", verticalalignment="center")
    plt.rcParams["font.size"] = "15"
    kw.update(textkw)
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)
    return texts

file_name = 'H_30_N501'
data_input = DataRead(file_name + '.txt')
im, cbar = heatmap(data_input, ax=ax, cmap="YlGn")
texts = annotate_heatmap(im, valfmt="{x:.1f} %")
fig.tight_layout()
plt.savefig('crop_colorbar', pad_inches = 0, dpi=600, transparent='True')
plt.show()
