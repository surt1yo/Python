# Create a Simple Digit Recogniser model using 
# TensorFlow and Keras to get MNIST using Python.
import tensorflow as tf 
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import os 
os.environ["TF_ENABLE_ONEDNN_OPTS"]="0"

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize the data
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build the model
model = models.Sequential([
    layers.Input(shape=(28, 28)),       
    layers.Flatten(),
    layers.Dense(128, activation='relu')
])


# Compile the model
model.compile(optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5, validation_split=0.1, verbose=1)

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
print(f"Test accuracy: {test_acc}")

# Make predictions
predictions = model.predict(x_test, verbose=0)

# Display the first image and prediction
plt.imshow(x_test[0], cmap=plt.cm.binary)
plt.title(f"Predicted: {predictions[0].argmax()}")
plt.show()
