import os

import seaborn as sns
import matplotlib.pyplot as plt

from PIL import Image, ImageDraw
import xml.etree.ElementTree as ET # Parse xml files

# Load directories
images_dir  = 'dataset/IMG/'
annotation_dir = 'dataset/XML/'

# sample_image = Image.open('dataset/IMG/Pothole-001.jpg')
# imgplot = plt.imshow(sample_image)
# plt.show()

# https://www.kaggle.com/code/mtszkw/reading-sample-image-and-bounding-boxes-from-xml/notebook
# Map XML to corresponding Image
def parse_voc_annotation(annotation_dir, image_dir):
    dataset = []
    for file in os.listdir(annotation_dir):
        tree = ET.parse(os.path.join(annotation_dir, file))
        root = tree.getroot()
        filename = root.find("filename").text
        image_path = os.path.join(image_dir, filename) # Find image using filename

        boxes = []
        for neighbor in root.iter('bndbox'):
            xmin = int(neighbor.find('xmin').text)
            ymin = int(neighbor.find('ymin').text)
            xmax = int(neighbor.find('xmax').text)
            ymax = int(neighbor.find('ymax').text)
            boxes.append((xmin, ymin, xmax, ymax))

        dataset.append({"image": image_path, "boxes": boxes})

    return dataset

# Create dataset
dataset = parse_voc_annotation(annotation_dir, images_dir)

# Preprocess data
def preprocess_image(image_path, boxes, target_size=(416,416)):
    image = Image.open(image_path)
    height, width = image.size

    # Resize images
    resized_images = image.resize(target_size)
    scale_x = target_size[0] / width
    scale_y = target_size[0] / height

    # Adjust bounding boxes
    resized_boxes = []
    for (xmin, ymin, xmax, ymax) in boxes:
        xmin = int(xmin * scale_x)
        ymin = int(ymin * scale_y)
        xmax = int(xmax * scale_x)
        ymax = int(ymax * scale_y)
        resized_boxes.append((xmin, ymin, xmax, ymax))

    return resized_images, resized_boxes

image_path = dataset[0]["image"]
boxes = dataset[0]["boxes"]
resized_image, resized_boxes = preprocess_image(image_path, boxes)

