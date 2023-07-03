from flask import Flask, render_template, request

app = Flask(__name__)

# Route to render the HTML form
@app.route('/')
def home():
    return render_template('upload.html')

# Route to handle the file upload
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        file.save('static/' + file.filename)
        return 'File uploaded successfully!'
    else:
        return 'No file selected!'

if __name__ == '__main__':
    app.run(debug=True)
