import os
from flask import Flask, request
import time
# song id, song name, thaat name, playing time, Healing Therapies 
from main import main

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = r'assets'

@app.route('/test',methods=['GET'])
def hello():
    return "Fine"
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
            os.remove(temp_file_path)
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
    app.debug=True
    app.run(host="0.0.0.0")
