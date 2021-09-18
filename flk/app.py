from flask import Flask,jsonify,request
import werkzeug
app = Flask(__name__)

@app.route('/upload',methods = ['POST'])
def upload():
    if(request.method == 'POST'):
        imageFile = request.files['img']
        filename = werkzeug.utils.secure_filename(imageFile.filename)
        imageFile.save('/uploadFolder/'+filename)
        return jsonify({"message":"Img Uplo one"})


if __name__ == "__main__":
    app.run(port=4000,debug=True)