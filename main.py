import os
import librosa
import subprocess
import numpy as np
import json
from collections import Counter


from helper.healing_therapies import healing_therapies
from helper.playing_time import playing_time
from main2 import main_2

def main(str):
    #print("Enter song path : ")
    # path = r"Laga Chunari Mein Daag.wav"
    path = str
    #subprocess.call(['ffmpeg', '-i', path, 'res.wav'])
    y, sr = librosa.load(path, sr=22050, mono=True)
    print(len(y))
    
    obtained_thaat = []
    possible_thaat_list = []
    thaat_count = []
    d = 50
    
    n_frames = int(np.ceil(len(y) / sr))
    n_samples = int(np.ceil(n_frames / d))

    for i in range(n_samples):
        if(i==n_samples-1):
            end = len(y)
            start = end - sr * d
        else:
            start = i * sr * d
            end = start + sr * d

        y_sample = y[start:end]
        sr_sample = sr
        obt_thaat = main_2(y_sample, sr_sample)
        for i in obt_thaat:
            obtained_thaat.append(i)
        
        
    # for i in obtained_thaat:
    #     if(i in possible_thaat_list):
    #         idx = possible_thaat_list.index(i)
    #         thaat_count[idx] = thaat_count[idx] + 1
    #     else:
    #         possible_thaat_list.append(i)
    #         thaat_count.append(1)
    
    # print(possible_thaat_list,thaat_count)

    counter_thaat=Counter(obtained_thaat)
    possible_thaat_tuple=counter_thaat.most_common(3)
    possible_thaat_list.append(possible_thaat_tuple[0][0])
    for i in range(1,len(possible_thaat_tuple)):
        if(possible_thaat_tuple[i-1][1]==possible_thaat_tuple[i][1]):
            possible_thaat_list.append(possible_thaat_tuple[i][0])


    print(possible_thaat_list)
    time=playing_time(possible_thaat_list)
    therapy = healing_therapies(possible_thaat_list)
    
    dict={"thaat":possible_thaat_list,
          "time":time,
          "therapy":therapy,}
    
    final=json.dumps(dict)

    return final




