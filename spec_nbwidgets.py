#! /usr/bin/env python

import matplotlib.pyplot as pl
import ipywidgets 
from ipywidgets import Layout
from IPython.display import display
import spec_data

class SpectralAnalysis:
    def __init__(self):
        self.sd=spec_data.SpectralData()
        self.cont_update=False

    def make_widgets(self):
        self.display_sel=ipywidgets.Dropdown(
            options=['time_series','spectrum'],
            description='displaytype')
        self.freq_slide=ipywidgets.FloatSlider(
            description='freqency',
            min=-200,
            value=10,
            max=200,
            layout=Layout(width='50%'),
            continuous_update=self.cont_update)
        self.decay_slide=ipywidgets.FloatSlider(
            description='decay',
            min=0,
            max=200,
            layout=Layout(width='50%'),
            continuous_update=self.cont_update)
        self.noise_slide=ipywidgets.FloatSlider(
            description='noise',
            min=0,
            max=.5,
            step=.01,
            layout=Layout(width='50%'),
            continuous_update=self.cont_update)
        vbox=ipywidgets.VBox()
        widget_tuple=(self.display_sel,self.freq_slide,self.decay_slide,self.noise_slide)
        vbox.children=widget_tuple
        display(vbox)
        for widget in widget_tuple:
            widget.on_trait_change(self.update_plot)
        self.plot_data()

    def update_plot(self,name):
        noise=self.noise_slide.value
        decay=self.decay_slide.value
        freq=self.freq_slide.value
        displaytype=self.display_sel.value
        self.plot_data(displaytype=displaytype,freq=freq,decay=decay,noiseamp=noise)

    def plot_data(self,displaytype='time_series',freq=10,decay=0,noiseamp=0):
        pl.clf()
        self.sd.gen_spec_data(displaytype,decay,freq,noiseamp) 
        pl.plot(self.sd.x,self.sd.data.real,linewidth=3,alpha=.6)
        pl.plot(self.sd.x,self.sd.data.imag,linewidth=3,alpha=.6)

