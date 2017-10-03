#! /usr/bin/env python

import matplotlib.pyplot as pl
import ipywidgets 
from ipywidgets import Layout
from IPython.display import display
import spec_data

class SpectralAnalysis:
    def __init__(self):
        self.sd=spec_data.SpectralData()

    def plot_data(self,displaytype='time_series',freq=10,decay=0,noiseamp=0):
        self.sd.gen_spec_data(displaytype,decay,freq,noiseamp) 
        pl.plot(self.sd.x,self.sd.data.real,linewidth=3,alpha=.6)
        pl.plot(self.sd.x,self.sd.data.imag,linewidth=3,alpha=.6)
        pl.show()

    def plot_interactive(self,modify_widgets=True):
        w=ipywidgets.interactive(self.plot_data,displaytype=['time_series','spectrum'],
                                freq=(-200,200),decay=(0,200),noiseamp=(0,.5,.01))
        if modify_widgets:
            for slider in w.children[1:]:
                slider.layout=Layout(width='50%')
                slider.continuous_update=False
        display(w)

