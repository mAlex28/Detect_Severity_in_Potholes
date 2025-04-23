# Detect_Severity_in_Potholes

## Dataset

**Research** [An annotated water-filled, and dry potholes dataset for deep learning applications](https://www.sciencedirect.com/science/article/pii/S2352340923003256) </br>
**Download** https://data.mendeley.com/datasets/tp95cdvgm8/1

## Severity Levels

- **Immediate Attention**: Bounding box area > 20% of the image area.
- **Moderate**: Bounding box area between 10-20%.
- **No Immediate Attention**: Bounding box area < 10%.

## Clone YOLOv5 repository

```python
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
```

## Metrics

- **Precision & Recall**: Computed per class to evaluate detection accuracy.
- **mAP (mean Average Precision)**:
  - **mAP@0.5**: IoU threshold of 0.5
  - **mAP@0.5:0.95**: Averaged over multiple IoU thresholds (0.5 to 0.95)

## Loss Curves

Visualisation of:

- **Training Loss**
- **Validation Loss**

Helps diagnose overfitting or underfitting during training.

## Output Location

You can find the metrics and plots under the `runs/train/` directory.

## Recreate the Project

Due to the large size of the dataset and the YOLOv5 repository, these have not been uploaded to GitHub. However, you can recreate the project by following the steps below:

### 1. Download the Dataset

You can download the dataset from the following link:

- [Download the pothole dataset](https://data.mendeley.com/datasets/tp95cdvgm8/1)

This dataset contains annotated pothole images that will be used for training and evaluation.

### 2. Clone the YOLOv5 Repository

Clone the official YOLOv5 repository from GitHub. This repository contains the necessary files to train the YOLO model for object detection.

```python
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
```

### 3. Organise the Dataset

├── dataset/
│ ├── IMG/ # Raw pothole images
│ ├── XML/ # Original XML annotations
│ ├── Updated_XML/ # Cleaned/modified XML files
│ └── YOLO/ # YOLO-formatted annotations

📦dataset
┣ 📂IMG
┣ 📂XML
┣ 📂Updated_XML
┗ 📂YOLO
