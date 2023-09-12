import librosa
import os

from helper.octave_table import octave_table

def main_2(y,sr):
    print()
    print()
    print()
    pitch, _ = librosa.piptrack(y=y, sr=sr)
    
    arr = []
    # Taking the pitches in a array which are in the range of 50-500
    for i in range(len(pitch)):
        for j in range(len(pitch[i])):
            if(int(pitch[i][j])>=int(50) and int(pitch[i][j])<=int(500)):
                arr.append(int(pitch[i][j]))

    # Finding the most prominent note
    most_prominent_note = max(set(arr), key=arr.count)
    print(most_prominent_note)

    # Finding the notes
    obtained_thaat = octave_table(most_prominent_note)
    try:
        os.remove("res.wav")
    except:
        """"""
    return obtained_thaat
