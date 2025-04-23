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
