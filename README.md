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
