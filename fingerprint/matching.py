import cv2
import numpy as np
import os

# Function to compare two images using Mean Squared Error (MSE)
def compare_images(image1, image2):
    resized_image1 = cv2.resize(image1, (300, 300))
    resized_image2 = cv2.resize(image2, (300, 300))
    gray_image1 = cv2.cvtColor(resized_image1, cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(resized_image2, cv2.COLOR_BGR2GRAY)
    mse = np.mean((gray_image1 - gray_image2) ** 2)
    return mse

# Specify the path to the folder containing the fingerprint images and match images
folder_path = "matching"

# Load the dataset of fingerprint images
dataset = []
for i in range(1, 26):
    image_path = os.path.join(folder_path, f"{i}.png")
    image = cv2.imread(image_path)
    dataset.append(image)

# Ask the user for input
number = int(input("Enter a number between 1 and 25: "))

if number < 1 or number > 25:
    print("Invalid number!")
else:
    query_image = dataset[number - 1]

    # Compare the query image with each image in the dataset
    scores = []
    for i, image in enumerate(dataset):
        score = compare_images(query_image, image)
        scores.append((i, score))

    # Sort the scores in ascending order
    scores.sort(key=lambda x: x[1])

    # Get the most similar image
    most_similar_number = scores[0][0]

    # Output the corresponding match image if it exists
    match_image_path = os.path.join(folder_path, f"{most_similar_number + 1}_match.png")
    if os.path.exists(match_image_path):
        print("Most similar image:", match_image_path)
    else:
        print("No match image found.")
