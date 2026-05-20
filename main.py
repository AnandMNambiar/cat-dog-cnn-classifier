import tensorflow as tf
from tensorflow.keras import layers, models

# Load training data
train_data = tf.keras.preprocessing.image_dataset_from_directory(
    ".",
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(150, 150),
    batch_size=32
)

# Load validation data
val_data = tf.keras.preprocessing.image_dataset_from_directory(
    ".",
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(150, 150),
    batch_size=32
)

# Build CNN model
model = models.Sequential([

    # Normalize pixels
    layers.Rescaling(1./255),

    # CNN layers
    layers.Conv2D(16, (3,3), activation='relu'),
    layers.MaxPooling2D(),

    layers.Conv2D(32, (3,3), activation='relu'),
    layers.MaxPooling2D(),

    # Convert to single line
    layers.Flatten(),

    # Neural network
    layers.Dense(64, activation='relu'),

    # Final output
    layers.Dense(1, activation='sigmoid')
])

# Configure model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train model
model.fit(
    train_data,
    validation_data=val_data,
    epochs=5
)

# Save model
model.save("cat_dog_model.keras")

print("Training Complete!")