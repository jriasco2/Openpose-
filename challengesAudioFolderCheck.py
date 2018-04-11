#!/usr/bin/python

import sys
import os
from scipy.io import wavfile as wav
import glob
import numpy as np
import matplotlib.pyplot as plt
#python challengesAudioFolderCheck.py ~/Descargas/challenge/ICMI2018-EAT_package/audio/
location_file_wav = sys.argv[1] #location folder of wav files

files_wav_directory = glob.glob(location_file_wav + '*.wav')  #Let me count files of folder
number_files_wav_directory = len(glob.glob(location_file_wav + '*.wav'))  #Let me count files of folder
vector_sampling_frequency = []
vector_size_audio = []

for x in range(0, number_files_wav_directory):
    file = wav.read(files_wav_directory[x])
    vector_sampling_frequency.append(file[0])
    vector_size_audio.append(len(file[1]))

numpy_vector_sampling_frequency =np.asarray(vector_sampling_frequency)
numpy_vector_size_audio =np.asarray(vector_size_audio)
print numpy_vector_sampling_frequency
print numpy_vector_size_audio


#n, bins, patches = plt.hist(numpy_vector_sampling_frequency, 50, normed=1, facecolor='green', alpha=0.75
plt.hist(numpy_vector_sampling_frequency,facecolor='green')
plt.show()

plt.hist(numpy_vector_size_audio,facecolor='orange')
plt.show()

#plt.hist([numpy_vector_sampling_frequency,numpy_vector_size_audio], bins=20,color=['orange', 'green'])
plt.hist([numpy_vector_sampling_frequency,numpy_vector_size_audio])#,color=['orange', 'green'],alpha=0.75)
plt.legend(["Frequency","Size_Audio"])
plt.title('Challenge Audio Histogram')
plt.grid(True)
plt.show()

min_value = np.amin(numpy_vector_size_audio)
max_value = np.amax(numpy_vector_size_audio)
print "valor minimo: " + str(min_value)
print "valor maximo: " + str(max_value)
