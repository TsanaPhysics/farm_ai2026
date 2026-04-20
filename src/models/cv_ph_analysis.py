import cv2
import numpy as np
import json
import sys
import os

def analyze_ph(image_path):
    try:
        # 1. Load image
        img = cv2.imread(image_path)
        if img is None:
            return {"status": "error", "message": "Image not found"}

        # 2. Pre-processing (Auto White Balance / Normalization)
        # Simple normalization to handle lighting variations
        img_norm = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

        # 3. Convert to HSV
        hsv = cv2.cvtColor(img_norm, cv2.COLOR_BGR2HSV)

        # 4. Extract Central ROI (Focus on the center of the photo)
        height, width, _ = img.shape
        roi_size = int(min(height, width) * 0.15) # 15% of the frame
        cy, cx = height // 2, width // 2
        roi = hsv[cy-roi_size:cy+roi_size, cx-roi_size:cx+roi_size]

        # 5. Calculate Average Hue
        avg_h = np.mean(roi[:, :, 0])
        avg_s = np.mean(roi[:, :, 1])
        avg_v = np.mean(roi[:, :, 2])

        # 6. Real-world Calibration Mapping (Simplified for Demo)
        # In a real model, this would be a trained regressor or a dense lookup table
        predicted_ph = 0.0
        confidence = 0.0
        
        # Simulated Mapping based on Typical Soil Color Curves
        if avg_h < 15:   # Reddish/Dark Brown (Peat/Laterite)
            predicted_ph = 4.5
            soil_type = "Red/Peat Soil"
            confidence = 0.88
        elif avg_h < 35: # Brown/Yellow (Alluvial/Loamy)
            predicted_ph = 6.8
            soil_type = "Loamy/Alluvial Soil"
            confidence = 0.92
        elif avg_h < 60: # Dark Grey/Black (Clay)
            predicted_ph = 7.2
            soil_type = "Clay Soil"
            confidence = 0.85
        else:
            predicted_ph = 6.0
            soil_type = "General Mix"
            confidence = 0.70

        result = {
            "status": "success",
            "ph": round(float(predicted_ph), 1),
            "soil_type": soil_type,
            "confidence": round(float(confidence * 100), 2),
            "hsv": [round(float(avg_h), 2), round(float(avg_s), 2), round(float(avg_v), 2)],
            "recommendation": "Optimal" if 6.0 <= predicted_ph <= 7.5 else "Adjustment needed"
        }
        return result

    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    if len(sys.argv) > 1:
        img_file = sys.argv[1]
        res = analyze_ph(img_file)
        print(json.dumps(res))
    else:
        print(json.dumps({"status": "error", "message": "No image provided"}))
