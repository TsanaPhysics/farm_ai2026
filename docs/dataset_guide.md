# 📘 คู่มือการใช้งานชุดข้อมูลดินและระบบวิเคราะห์ AI (xAI 2026)
**โปรเจกต์:** Python xAI Next GEN Young Digital Scientist

---

## 📂 รายละเอียดชุดข้อมูลและสคริปต์วิเคราะห์

คู่มือนี้สรุปวิธีการใช้งานสคริปต์ Python ทั้ง 3 รูปแบบที่เชื่อมต่อกับฐานข้อมูลจริงจาก GitHub พร้อมระบบแสดงผลด้วยกราฟ (Data Visualization)

### 1. ระบบแนะนำพืช (Crop Recommendation)
*   **ไฟล์:** `soil_analysis_crop_rec.py`
*   **คำอธิบาย:** ใช้โมเดล **Random Forest Classifier** เพื่อจำแนกประเภทพืชที่เหมาะสมที่สุดตามคุณสมบัติของดิน
*   **กราฟที่แสดงผล:**
    1.  **Correlation Heatmap:** แสดงความสัมพันธ์ระหว่างสารอาหารต่างๆ (เช่น N สัมพันธ์กับความชื้นอย่างไร)
    2.  **Feature Importance:** แสดงปัจจัยที่มีผลต่อการเลือกพืชมากที่สุด (เช่น ปริมาณฝนหรือค่า pH)
*   **การรัน:** `python3 manual/soil_analysis_crop_rec.py`

### 2. ระบบพยากรณ์ไนโตรเจนเชิงลึก (AgriTech Analysis)
*   **ไฟล์:** `soil_analysis_agritech.py`
*   **คำอธิบาย:** ใช้โมเดล **Random Forest Regressor** เพื่อพยากรณ์ปริมาณ Nitrogen จากธาตุอาหารรอง (Zn, Fe, Cu, ฯลฯ)
*   **กราฟที่แสดงผล:**
    1.  **Actual vs Predicted Scatter Plot:** กราฟจุดเปรียบเทียบค่าที่ AI ทำนายกับค่าจริงในห้องแล็บ
    2.  **Feature Importance:** แสดงว่าธาตุอาหารรองตัวใด (เช่น Zinc หรือ Boron) มีความสัมพันธ์กับ Nitrogen มากที่สุด
*   **การรัน:** `python3 manual/soil_analysis_agritech.py`

### 3. ระบบพยากรณ์จากปัจจัยแวดล้อม (Nutrient Predictor)
*   **ไฟล์:** `soil_analysis_nutrient_pred.py`
*   **คำอธิบาย:** วิเคราะห์ความสัมพันธ์ระหว่างสภาพอากาศ (อุณหภูมิ, ความชื้น) และคาร์บอนอินทรีย์ ต่อปริมาณธาตุอาหาร
*   **กราฟที่แสดงผล:**
    1.  **Nitrogen Distribution:** กราฟระฆังคว่ำแสดงการกระจายตัวของปริมาณ Nitrogen ในพื้นที่ศึกษา
    2.  **Environmental Factors Bar Chart:** เปรียบเทียบอิทธิพลของปัจจัยแวดล้อมต่อความสมบูรณ์ของดิน
*   **การรัน:** `python3 manual/soil_analysis_nutrient_pred.py`

### 📈 กราฟแสดงผลที่ถูกสร้างขึ้น (Generated Visualizations)
หลังจากรันสคริปต์ ระบบจะบันทึกกราฟลงในโฟลเดอร์ `manual/images/` ดังนี้:
*   **Crop Recommendation:** `crop_rec_heatmap.png`, `crop_rec_feature_importance.png`
*   **AgriTech Analysis:** `agritech_actual_vs_pred.png`, `agritech_feature_importance.png`
*   **Nutrient Predictor:** `nutrient_pred_distribution.png`, `nutrient_pred_feature_importance.png`

---

## 🛠️ ขั้นตอนการเตรียมเครื่องมือ (Prerequisites)


เพื่อให้สคริปต์ทำงานได้สมบูรณ์และแสดงกราฟได้ คุณต้องติดตั้ง Library ดังนี้:

```bash
pip install pandas scikit-learn matplotlib seaborn
```

---

## 💡 แนวทางการสอนนักเรียน/นักศึกษา
1.  **การสังเกต Heatmap:** ให้นักเรียนลองดูว่าตัวแปรไหนมีสีเข้ม (Correlation สูง) และวิเคราะห์ว่าทำไมถึงเป็นเช่นนั้น
2.  **การเปรียบเทียบ R-squared:** ให้นักเรียนสังเกตว่าข้อมูลจากแหล่งใดที่ AI สามารถพยากรณ์ได้แม่นยำกว่ากัน
3.  **การทดลองเปลี่ยนค่า:** ลองเปลี่ยนตัวเลขในส่วน `sample` ของโค้ด เพื่อดูว่าพืชที่แนะนำจะเปลี่ยนไปอย่างไร

---
*จัดทำโดย: ทีมพัฒนา Python xAI (เมษายน 2026)*
