from flask import Flask,jsonify,request
import werkzeug
app = Flask(__name__)

@app.route("/api",methods=["GET"])
def function():
    if(request.method == 'GET'):
        d = {}
        text = "Hello Boyyy"
        d["query"] = text
        return jsonify(d)
@app.route('/upload',methods = ['POST'])
def upload():
    if(request.method == 'POST'):
        imagefile = request.files['image']
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        imagefile.save('uploadedimages/'+filename)
        return jsonify({"message":"Img Uplo one"})


if __name__ == "__main__":
    app.run(port=4000,debug=True)