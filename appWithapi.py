from gtts import gTTS
from flask import Flask, render_template, request, send_file, jsonify
from langdetect import detect

app = Flask(__name__, static_folder='static/')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/convert', methods=['POST'])
def convert():
    if request.method == 'POST':
        data = request.form['data']
        language = detect(data)
        myfile = gTTS(text=data, lang=language, slow=False)
        temp_file_path = '/home/abdelbaki/mysite/static/temp.mp3'
        myfile.save(temp_file_path)
        return render_template('download.html', audio_file=temp_file_path)

@app.route('/download',methods=['POST'])
def download():
    if request.method=='POST':
        return send_file('/home/abdelbaki/mysite/static/temp.mp3',as_attachment=True)

@app.route('/api/convert', methods=['POST'])
def convert_text_to_speech():
    if request.method == 'POST':
        data = request.json.get('text')
        if not data:
            return jsonify({'error': 'Missing text parameter'}), 400
        
        language = detect(data)
        myfile = gTTS(text=data, lang=language, slow=False)
        temp_file_path = '/home/abdelbaki/mysite/static/temp.mp3'
        myfile.save(temp_file_path)
        return jsonify({'audio_file': temp_file_path}), 200

if __name__ == "__main__":
    app.run(debug=True)
