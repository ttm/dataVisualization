import pylab as p, numpy as n
from scipy.io import wavfile as w

fs = open('../data/mwavs.txt', 'r')
ll = fs.readlines()
sfiles = []
for l in ll:
    ff = l # l.split(" ")[-1][:-1]
    if 'nltk_data' in ff:
        sfiles.append(ff)

# duration
# power
# upper/lower energy

sounds = []
srates = []
durations = []
powers = []
spectral = []
fact = .2
for i, f in enumerate(sfiles):
    sound = w.read(f)
    srate = sound[0]
    sa = sonic_array = sound[1].astype("float64")
    sounds.append(sa)
    srates.append(srate)

    duration = len(sa)/srate
    durations.append(duration) ###

    power = (sa**2).sum()/len(sa)
    powers.append(power) ###

    spectrum = n.fft.fft(sa)
    energies_components = n.abs(spectrum[:spectrum.shape[0]//2])
    fact_ = int(fact*energies_components.shape[0])
    ratio = energies_components[:fact_].sum()/energies_components[fact_:].sum()
    spectral.append(ratio)
    print(i)

import pickle
pickle.dump([durations, powers, spectral, sounds, srates],open('../data/sFiles.pickle', 'wb'),-1)
