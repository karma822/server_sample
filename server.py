import os
from flask import Flask, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename

global uploaded_ok

UPLOAD_FOLDER = './upload'
DOWNLOAD_FOLDER = './download'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif' , 'bmp'])

uploaded_ok = 0
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload/<filename>')
def uploaded_file( filename ):
    return filename

@app.route('/')
def hello():
	return 'hello'

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    print(request.method)
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return 'No file part'#redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return 'No selected file'#redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(filename)
            print(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            global uploaded_ok
            uploaded_ok += 1
            return redirect(url_for('uploaded_file',
                                    filename=filename))
            #return redirect(url_for('download_file'))
            #return 'ok'
    return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
          <p><input type=file name=file>
             <input type=submit value=Upload>
        </form>
        '''

@app.route('/download', methods=['GET'])
def download_file():
    if request.method == 'GET':
        global uploaded_ok
        if uploaded_ok > 0:
            try:
                filename = 'return.png'
                nom_image = secure_filename(filename)
                #uploaded_ok -= 1
                return send_file(os.path.join(app.config['DOWNLOAD_FOLDER'], nom_image), mimetype='image/jpeg', attachment_filename=nom_image, as_attachment=True)
            except Exception as e:
                print(e)
                return e
        else:
            return 'Empty'

    
    return 'wrong parameter'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
