import os
from flask import Flask, request, jsonify, render_template

from main import main

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = r'assets'

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


if __name__ == '__main__':
    app.debug=True
    app.run()
    #webview.start()
