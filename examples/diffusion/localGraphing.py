# -*- coding: utf-8 -*-
"""
Created on Sun May  3 12:33:44 2015

@author: cstark
"""

import matplotlib.pyplot as plt
import matplotlib as mpl

try:
    import fipy as fi
except:
    pass

try:
    plt.close("all")
except:
    pass

def closeAll():
    plt.close("all")

def setParams(doPlotInline):
    if not(doPlotInline):
        mpl.rcParams.update(setPlotDefaults(8,8,19,18,16))
    else:
        mpl.rcParams.update(setPlotDefaults(8,6,12,12,11))
    return
    
    
bigFont = {'family': 'Arial', 'weight': 'bold',  'verticalalignment':'bottom'}
#axisFont = {'fontname':'Arial', 'size':'16'}
#mathtext.fontset : Should be 'cm','stix','stixsans' or 'custom'

def setPlotDefaults(xSize,ySize,titleSize,labelsize,ticklabelsize):
    defaultDict = {'figure.figsize': (xSize,ySize), 
                     'font.size': labelsize,
                     'font.serif': 'Arial',
                     'axes.titlesize': titleSize,
                     'axes.labelsize': labelsize,
                     'xtick.labelsize': ticklabelsize,
                     'ytick.labelsize': ticklabelsize,
                     'savefig.format': 'png',
                     'savefig.dpi': 100,
                     'mathtext.fontset': 'stix'}
    return defaultDict
    
def createViewer(graphTitle, varSet, labelSet, limits):
    if limits=={}:
        viewer = fi.Viewer(vars = varSet, title=graphTitle, #legend=None,
                           datamin=-0.005,datamax=1.05)
    else:
        viewer = fi.Viewer(vars = varSet, title=graphTitle, limits=limits)        
    ax = viewer.axes
    ax.xaxis.set_label_text(labelSet[0])
    ax.yaxis.set_label_text(labelSet[1])
#     viewer1.axes.set_aspect('equal')
    return viewer