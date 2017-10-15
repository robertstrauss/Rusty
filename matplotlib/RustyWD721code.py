%matplotlib notebook
import matplotlib as mpl
import pylab as pl
import numpy as np
import seaborn as sns
WD721 = np.loadtxt("/home/russell/Desktop/matplotlib/WaveData721.csv", skiprows = 3, delimiter = ',')
pl.figure()
pl.clf()
fx2 = np.arange(0, 2001)
fx2 = fx2/0.02 #scaling factor
sns.set_context("notebook", rc={"lines.linewidth": 1.5})
sns.set_style("darkgrid")
sns.set_palette("husl")
wave = WD721[0:4000, 1] #The wave off the osciliscope
pl.subplot(2,2,1)
pl.title("Wave")
pl.plot(wave) #Plotting The Wave
pl.xlim([1050, 1600])
pl.subplot(2,2,2)
pl.title("Square of wave")
pl.plot(wave**2) #Plotting the square of The Wave
pl.xlim([1050, 1600])
pl.subplot(2,2,3)
pl.title("Spectrum of wave")
pl.plot(fx2, abs(pl.rfft(wave))) #Plotting the Fourier transform of The Wave
pl.xlim([36000, 44000])
pl.xlabel("frequency")
pl.subplot(2,2,4)
pl.title("Spectrum of wave^2")
pl.plot(fx2, abs(pl.rfft(wave**2)))
pl.xlim([-100, 4500])
pl.xlabel("frequency")
pl.tight_layout()