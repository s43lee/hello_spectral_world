#! /usr/bin/env python

import pandas as pd
import numpy as np

import lft2

class SpectralData:
    def __init__(self):
        self.npts=128
        dw=1e-3
        sw=1./dw
        sw2=int(sw/2)
        totaltime=dw*self.npts
        self.time_=np.linspace(0,totaltime,self.npts)
        self.freqaxis=lft2.faxis(sw,self.npts)
        self.fmin=-sw/2.
        self.fmax=sw/2

    def gen_spec_data(self,displaytype="time_series",decay=0,freq=10,noiseamp=0):
        #fmin,fmax=frange
        self.sig=np.exp((2*np.pi*freq*1j-decay)*self.time_)
        noise=(np.random.randn(self.npts)+np.random.randn(self.npts)*1j)*noiseamp
        self.sig += noise
        if displaytype=="time_series":
            self.data=self.sig
            self.x=self.time_
        else:
            self.spec=lft2.efft(self.sig)
            self.data=self.spec
            self.x=self.freqaxis


