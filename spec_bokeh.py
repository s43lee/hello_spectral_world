#! /usr/bin/env python
from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource,Select
from bokeh.models.widgets import Slider
from bokeh.plotting import figure

import spec_data

class BkSpecPlotter:
    def __init__(self):
        self.sd=spec_data.SpectralData()

    def make_data_source(self):
        self.sd.gen_spec_data()
        self.rsource=ColumnDataSource(data=dict(x=self.sd.x,y=self.sd.data.real))
        self.isource=ColumnDataSource(data=dict(x=self.sd.x,y=self.sd.data.imag))

    def make_plot(self):
        self.plot = figure(plot_height=400, plot_width=500, title="spectral data",
                      tools="crosshair,pan,reset,save,wheel_zoom")
        self.plot.line('x', 'y', source=self.rsource, line_width=3, line_alpha=0.6,color="blue")
        self.plot.line('x', 'y', source=self.isource, line_width=3, line_alpha=0.6,color="green")
        return self.plot

    def make_widgets(self):
        self.freq_slide = Slider(title="frequency", value=10, start=-200, end=200)
        self.decay_slide = Slider(title="decay", value=0, start=0, end=200)
        self.noise_slide=Slider(title="noise level", value=0, start=0, end=.5,step=.01)
        self.display_sel=Select(title='display', value='time_series', options=["time_series","spectrum"])
        for widget in [self.freq_slide,self.decay_slide,self.noise_slide,self.display_sel]:
            widget.on_change("value",self.update_data)
        inputs=widgetbox(self.display_sel,self.freq_slide,self.decay_slide,self.noise_slide)
        self.layout = row(inputs,self.make_plot())
        curdoc().add_root(self.layout)
        curdoc().title = "Spectral analysis"

    def update_data(self,attr,old,new):
        freq=self.freq_slide.value
        decay=self.decay_slide.value
        noiseamp=self.noise_slide.value
        display=self.display_sel.value 
        self.sd.gen_spec_data(freq=freq,decay=decay,noiseamp=noiseamp,displaytype=display)
        self.rsource.data=dict(x=self.sd.x,y=self.sd.data.real)
        self.isource.data=dict(x=self.sd.x,y=self.sd.data.imag)

bsp=BkSpecPlotter()
bsp.make_data_source()
bsp.make_widgets()
