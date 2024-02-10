from gtts import gTTS
from flask import Flask, render_template, request, send_file
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
        # حفظ الملف المؤقت (مثلاً temp.mp3)
        temp_file_path = './static/temp.mp3'
        myfile.save(temp_file_path)
        return render_template('download.html', audio_file=temp_file_path)




@app.route('/download',methods=['POST'])
def download():
    if request.method=='POST':
        return send_file('./static/temp.mp3',as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)