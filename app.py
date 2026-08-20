from flask import Flask, render_template, request
import os
from image_processing.preprocess import preprocess_image
from model.predict import predict_blood_group

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/result")
def result():
    return render_template("result.html")

@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return "No image uploaded."

    uploaded_image = request.files["image"]

    if uploaded_image.filename == "":
        return "No image selected."

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], uploaded_image.filename)
    uploaded_image.save(filepath)

    # Process image
    preprocess_image(filepath)

    # Predict blood group and confidence
    prediction, confidence = predict_blood_group(filepath)

    return render_template(
        "result.html",
        image=uploaded_image.filename,
        prediction=prediction,
        confidence=f"{confidence}%"
    )

if __name__ == "__main__":
    app.run(debug=True)