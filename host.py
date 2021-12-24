from flask import Flask,render_template,request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os 
from PIL import Image
import base64
app = Flask(__name__)

@app.route('/form')
def form():
    return render_template('index.html')
 
@app.route('/upload', methods = ['POST', 'GET'])
def upload():
    print(request.files['File'])
    if(request.method == 'POST'):
        request.files['File'].save("file.png")
        return "File saved successfully"
        
 
app.run(host='localhost', port=5000)
