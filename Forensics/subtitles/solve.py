import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image
import string

(
    (train_images, train_labels),
    (test_images, test_labels),
) = keras.datasets.mnist.load_data()

num_classes = 10
input_shape = (28, 28, 1)

train_images = train_images.astype("float32") / 255
test_images = test_images.astype("float32") / 255

train_images = np.expand_dims(train_images, -1)
test_images = np.expand_dims(test_images, -1)

print("train_images shape:", train_images.shape)

train_labels = keras.utils.to_categorical(train_labels, num_classes)
test_labels = keras.utils.to_categorical(test_labels, num_classes)

model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        tf.keras.layers.Conv2D(
            32, kernel_size=(3, 3), kernel_initializer="he_uniform", activation="relu"
        ),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(100, activation="relu", kernel_initializer="he_uniform"),
        tf.keras.layers.Dense(10, activation="softmax"),
    ]
)

model.summary()

batch_size = 128
epochs = 25

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

checkpoint_path = "training/cp.ckpt"

cp_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_path, save_weights_only=True, verbose=1
)

model.fit(
    train_images,
    train_labels,
    batch_size=batch_size,
    epochs=epochs,
    validation_split=0.1,
    validation_data=(test_images, test_labels),
    callbacks=[cp_callback],
)

video_nums = []
for i in range(847):
    image = Image.open(f"output_images/{i+1:05}.png").convert("L")
    pix = np.array(image).reshape(1, 28, 28, 1)
    pred = model.predict(pix)
    video_nums.append(np.argmax(pred))

with open("subtitles.srt") as f:
    lines = f.read().splitlines()

subtitle_nums = list(map(int, lines[2::4]))

result = []
temp = ""
in_group = False
for a, b in zip(subtitle_nums, video_nums):
    if a != b:
        temp += str(a)
        in_group = True
    if a == b and in_group:
        if len(temp) > 1:
            result.append(int(temp))
        temp = ""
        in_group = False

if len(temp) > 1 and in_group:
    result.append(int(temp))

print("".join(chr(i) if chr(i) in string.printable else "." for i in result))
