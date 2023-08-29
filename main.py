import os
import librosa
#import webview
import subprocess
import numpy as np
from flask import Flask, request, jsonify, render_template


from helper.healing_therapies import healing_therapies
from main2 import main_2

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = r'C:\Users\soham\Desktop\Coding\Project\New folder\Music_classifier'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'audio_file' not in request.files:
            return "No audio file part"
        
        audio_file = request.files['audio_file']
        
        if audio_file.filename == '':
            return "No selected file"
        
        if audio_file:
            temp_file_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_file.filename)
            audio_file.save(temp_file_path)
            output = main(temp_file_path)
            return output
    
    return '''
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="audio_file">
        <input type="submit" value="Upload">
    </form>'''


def main(str):
    print("Enter song path : ")
    # path = r"Laga Chunari Mein Daag.wav"
    path = str
    try:
        os.remove('res.wav')
    except:
        """"""
    subprocess.call(['ffmpeg', '-i', path, 'res.wav'])
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
        
    print()
    print()
    print()
    for i in obtained_thaat:
        if(i in possible_thaat_list):
            idx = possible_thaat_list.index(i)
            thaat_count[idx] = thaat_count[idx] + 1
        else:
            possible_thaat_list.append(i)
            thaat_count.append(1)
    
    print(possible_thaat_list)
    
    therapy = healing_therapies(possible_thaat_list)
    
    return therapy




if __name__ == '__main__':
    app.run(debug=True)
    #webview.start()
