import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

model = load_model("model/blood_group_model.h5")

classes = [
    "A+", "A-", "AB+", "AB-",
    "B+", "B-", "Not_Valid",
    "O+", "O-"
]

def predict_blood_group(img_path):
    img = image.load_img(img_path, target_size=(128, 128))
    img = image.img_to_array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img, verbose=0)

    index = np.argmax(prediction)
    confidence = round(float(np.max(prediction)) * 100, 2)

    return classes[index], confidence