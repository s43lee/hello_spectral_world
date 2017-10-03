import numpy.fft as fft
import numpy as nu

def efft(v,ftpts=None,flscale=True,flswap=True,flscale_1stpt=False,axis=-1):
    '''flswap=True (default), index ftps/2 zero freq,
    flswap=False, zero freq at index 0, if ftpts<len(v), v is truncated
    flscale=True, spectrum scaled by 1/ftpts
    flscale1stPt=True, scale 1st pt by 2 before fft
    if ftpts>len(v), v is zero filled
    aixs=-1, by default last axis used for fft
    returns fft scaled by factor 1/ftpts'''
    if not ftpts:
        ftpts=len(v)
    if ftpts < len(v):
        v=v[0:ftpts]
    if flscale_1stpt:
        v[0]=v[0]/2.
    if flscale:
        scale_factor=1./ftpts
    else:
        scale_factor=1.
    spec=fft.fft(v,n=ftpts,axis=axis)*scale_factor
    if flswap:
        return nu.roll(spec,ftpts/2)
    else:
        return spec

def faxis(sw,npts):
    '''faxis(sw,npts):
    n/2 is zero frequency where n=0,1,...,n-1'''
    return nu.arange(float(npts))*sw/npts - sw/2.


