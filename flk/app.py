from flask import Flask,jsonify,request
import werkzeug
import sys
import cv2
import os
sys.path.append("../flk/Mask_RCNN/demo")

from train_mask_rcnn_demo import *
from mrcnn.visualize import random_colors,get_mask_contours,draw_mask


app = Flask(__name__)


@app.route("/api",methods=["GET"])
def function():
    if(request.method == 'GET'):
        file_ = os.listdir("../uploadedimages/")[0]
        img = cv2.imread(file_)
        test_model, inference_config = load_inference_model(1,'../flk/mask_rcnn_object_0005.h5')
        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Detect results
        r = test_model.detect([image])[0]
        object_count = len(r["class_ids"])
        colors = random_colors(object_count)
        for i in range(object_count):
            # 1. Mask
            mask = r["masks"][:, :, i]
            contours = get_mask_contours(mask)
            for cnt in contours:
                cv2.polylines(img, [cnt], True, colors[i], 2)
                img = draw_mask(img, [cnt], colors[i])
        print(object_count)
        os.remove(file_)
        d = {}
        text = "Number Of Object" + object_count
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
