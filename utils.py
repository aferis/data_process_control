import matplotlib.pyplot as plt
import math
import scipy.stats as stats
import numpy as np
import glob
from PIL import Image
import pandas as pd
from sklearn.metrics import plot_confusion_matrix
from ipywidgets import interact, FloatSlider
from sklearn.metrics import r2_score
"""
Util functions for Notebook: Process_Control
"""

def labelsAndLegend():
    plt.xlabel(r'x $\longrightarrow$')
    plt.ylabel(r'y $\longrightarrow$')
    plt.legend()

def plotHist(y_test,y_hat,labelx,labely,title_hist,plot_name,test_size,plot_format):
    n, bins, patches = plt.hist((y_test - y_hat).values, bins=70, density=True, alpha=0.6, label='Fehlerverteilung')
    mu = np.mean((y_test-y_hat))
    sigma = np.std((y_test-y_hat))
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
    plt.plot(x, stats.norm.pdf(x, mu, sigma), color="red", label=r'Gaußscher Fit $\mu$ = %.2f, $\sigma$ = %.2f, $R^2$= %.3f'%(mu, sigma, r2_score(y_test, y_hat)))
    plt.axis( [-500, 500, 0, 0.01] )
    plt.title(title_hist + ' Residuum $e = y-\hat{y}$')
    plt.xlabel(labelx)
    plt.ylabel(labely) 
    plt.legend()
#    plt.savefig(plot_name+'_' +str(test_size)+ plot_format, dpi=800, facecolor='w', edgecolor='w',
#        orientation='portrait', papertype='a5',transparent=False, bbox_inches='tight', pad_inches=0.1)
    plt.show()

def rms(y, y_hat):
    return np.sqrt(np.mean((y-y_hat)**2))
def mae(y, y_hat):
    return np.mean(np.abs(y-y_hat))
def mse(y, y_hat):
    return np.mean((y-y_hat)**2)