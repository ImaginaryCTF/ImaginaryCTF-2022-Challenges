from Crypto.Util.number import bytes_to_long

from tensorflow import keras
import numpy as np
import random
from PIL import Image

flag = "ictf{i_hope_you_didnt_do_this_by_hand}"

(
    (train_images, train_labels),
    (test_images, test_labels),
) = keras.datasets.mnist.load_data()


def get_image(num):
    while True:
        index = random.randint(0, len(train_labels))
        if train_labels[index] == num:
            return train_images[index]


def get_random_digit_except(num):
    while True:
        r = random.randint(0, 9)
        if r != num:
            return r


random.seed(70262630165630058318679)
image_count = 0

image_nums = []
subtitle_nums = []

for char in flag:
    for i in range(random.randint(15, 25)):
        random_num = random.randint(0, 9)
        image_nums.append(random_num)
        subtitle_nums.append(random_num)
        pil_img = Image.fromarray(get_image(random_num))
        pil_img.save(f"images/{image_count:05}.png")
        image_count += 1

    for n in str(ord(char)):
        correct_num = int(n)
        random_num = get_random_digit_except(correct_num)
        image_nums.append(random_num)
        subtitle_nums.append(correct_num)
        pil_img = Image.fromarray(get_image(random_num))
        pil_img.save(f"images/{image_count:05}.png")
        image_count += 1

print(f"image_nums = {image_nums}")
print(f"subtitle_nums = {subtitle_nums}")

with open("subtitles.srt", "w") as f:
    for i, num in enumerate(subtitle_nums):
        f.write(str(i + 1) + "\n")
        start_minutes, start_seconds = divmod(i, 60)
        end_minutes, end_seconds = divmod(i + 1, 60)
        f.write(
            f"00:{start_minutes}:{start_seconds},000 --> 00:{end_minutes}:{end_seconds},000\n"
        )
        f.write(str(num) + "\n")
        f.write("\n")
