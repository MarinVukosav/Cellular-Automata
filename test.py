from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import numpy
import matplotlib.pyplot as plt
number=1
output_pattern = [int(x) for x in numpy.binary_repr(number, width=8)]
input_pattern = numpy.zeros([8,3])
for i in range(8):
    input_pattern[i, :] = [int(x) for x in numpy.binary_repr(7-i, width=3)]
columns = 21
rows = int(columns/2)+1
canvas = numpy.zeros([rows,columns+2])
canvas[0, int(columns/2)+1]=1
for i in numpy.arange(0, rows-1):
    for j in numpy.arange(0, columns):
        for k in range(8):
            if numpy.array_equal(input_pattern[k, :], canvas[i, j:j+3]):
                canvas[i+1, j+1] = output_pattern[k]



def f(number):
    output_pattern = [int(x) for x in numpy.binary_repr(number, width=8)]
    input_pattern = numpy.zeros([8,3])
    for i in range(8):
        input_pattern[i, :] = [int(x) for x in numpy.binary_repr(7-i, width=3)]
    columns = 21
    rows = int(columns/2)+1
    canvas = numpy.zeros([rows,columns+2])
    canvas[0, int(columns/2)+1]=1
    for i in numpy.arange(0, rows-1):
        for j in numpy.arange(0, columns):
            for k in range(8):
                if numpy.array_equal(input_pattern[k, :], canvas[i, j:j+3]):
                    canvas[i+1, j+1] = output_pattern[k]
    plt.imshow(canvas[:, 1:columns+1], cmap='Greys', interpolation='nearest')
    plt.title("Elementarni stanicni automat rule {}".format(number))
    plt.show()
                    
interact(f, number=widgets.IntSlider(min=1,max=255,step=1,value=10))