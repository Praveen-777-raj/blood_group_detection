from tensorflow.keras.preprocessing.image import ImageDataGenerator
from cnn_model import create_model

# Dataset paths
train_dir = "dataset/train"
test_dir = "dataset/test"

# Data augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True
)

test_datagen = ImageDataGenerator(rescale=1./255)

# Load training data
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(128, 128),
    batch_size=32,
    class_mode='categorical'
)

# Load testing data
test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(128, 128),
    batch_size=32,
    class_mode='categorical'
)

# Number of classes
num_classes = len(train_generator.class_indices)

# Create model
model = create_model(num_classes)

# Train model
model.fit(
    train_generator,
    validation_data=test_generator,
    epochs=10
)

# Save model
model.save("model/blood_group_model.h5")

print("Model saved successfully!")