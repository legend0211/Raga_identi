import json
import os
from flask import Flask, request
import requests
from flask_cors import CORS
import time
# song id, song name, thaat name, playing time, Healing Therapies 
from main import main

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = r'assets'

@app.route('/test',methods=['GET'])
def hello():
    return "Fine"
@app.route('/link',methods=['GET','POST'])
def index2():
    if request.method == 'POST':
        start_time=time.time()
        link=request.json.get('link')
        song_path="assets/song.mp3"

        response=requests.get(link)

        if response.status_code==200:
            with open(song_path,'wb') as file:
                file.write(response.content)
            output=main(song_path)
            try:
                os.remove(song_path)
            except:
                """"""
            end_time=time.time()
            print(f"Time: {end_time-start_time}")
            print(type(output))
            print(output)
            return output
        else:
            print(f"Failed to download the song. Status Code: {response.status_code}")

    return '''
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="audio_file">
        <input type="submit" value="Upload">
    </form>'''


@app.route('/', methods=['GET', 'POST'])
def index():
    print(request.files)
    if request.method == 'POST':
        start_time=time.time()
        if 'audio_file' not in request.files:
            return "No audio file part"
        
        audio_file = request.files['audio_file']
        
        if audio_file.filename == '':
            return "No selected file"
        
        if audio_file:
            temp_file_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_file.filename)
            audio_file.save(temp_file_path)
            output = main(temp_file_path)
            try:
                os.remove(temp_file_path)
            except:
                """"""
            end_time=time.time()
            print(f"Time: {end_time-start_time}")
            print(type(output))
            print(output)
            return output
    
    return '''
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="audio_file">
        <input type="submit" value="Upload">
    </form>'''

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
