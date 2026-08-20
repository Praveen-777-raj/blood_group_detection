import cv2

def preprocess_image(image_path):

    # Read image
    image = cv2.imread(image_path)

    # Resize image (same size used during training)
    image = cv2.resize(image, (128, 128))

    # Save processed image
    cv2.imwrite("static/uploads/processed_image.jpg", image)

    return image