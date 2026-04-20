# 🚜 Farm AI: Python xAI Next GEN Project (2026)
**ศูนย์เรียนรู้เกษตรดิจิทัลอัจฉริยะ | "Universe of Learning"**

ยินดีต้อนรับสู่โครงการพัฒนาทักษะนักวิทยาศาสตร์ข้อมูลรุ่นเยาว์ (Young Digital Scientist) เพื่อการเกษตรแม่นยำด้วยเทคโนโลยี AI รุ่นล่าสุด

---

## 📂 โครงสร้างโปรเจกต์ (Project Architecture)

โปรเจกต์ถูกจัดระเบียบแบบ Modular เพื่อรองรับการขยายตัวในอนาคต:

*   **`docs/`**: คู่มือและทฤษฎี (The Knowledge Hub)
    *   [workshop_2026.md](docs/workshop_2026.md) - กำหนดการอบรม 2 วัน
    *   [soil_theory.md](docs/soil_theory.md) - ทฤษฎี AI วิเคราะห์ดิน
    *   [weather_theory.md](docs/weather_theory.md) - ทฤษฎี AI วิเคราะห์อากาศ
    *   [dataset_guide.md](docs/dataset_guide.md) - คู่มือการใช้ฐานข้อมูล GitHub
*   **`src/`**: โค้ดโปรแกรม (Source Code)
    *   `data_fetchers/` - สคริปต์ดึงข้อมูลจาก NASA และสร้างข้อมูลจำลอง
    *   `models/` - โมเดล AI (Classification & Regression) สำหรับวิเคราะห์ดิน
*   **`data/`**: คลังข้อมูล (Data Warehouse)
    *   `raw/` - เก็บไฟล์ CSV/Excel ดิบที่ดึงมาจากแหล่งต่างๆ
*   **`output/`**: ผลลัพธ์การวิเคราะห์
    *   `images/` - กราฟ Visualization และแผนภูมิต่างๆ
*   **`website/`**: ส่วนแสดงผล Landing Page ของโครงการ

---

## 🚀 ลำดับการเรียนรู้ (Learning Path)

1.  **ทำความเข้าใจทฤษฎี:** อ่านคู่มือใน [docs/](docs/) เพื่อเข้าใจพื้นฐาน xAI
2.  **เตรียมข้อมูล:** รันสคริปต์ใน `src/data_fetchers/` เพื่อเตรียมไฟล์ข้อมูลลงใน `data/raw/`
3.  **ฝึกสอน AI:** ใช้สคริปต์ใน `src/models/` เพื่อสร้างโมเดลและวิเคราะห์ความสำคัญของตัวแปร (Feature Importance)
4.  **แสดงผล:** ตรวจสอบกราฟสรุปผลใน `output/images/` และอัปเดตข้อมูลบน `website/`

---

## 🔍 จุดเด่น: Explainable AI (xAI)
โปรเจกต์นี้ไม่ได้สอนเพียงแค่การสร้าง AI แต่สอนให้ **"เข้าใจ AI"** ผ่านการทำ Feature Importance เพื่อดูว่าปัจจัยใด (เช่น pH, ฝน, หรือ แร่ธาตุ) ที่ส่งผลต่อการตัดสินใจของ AI มากที่สุด เพื่อความโปร่งใสและแม่นยำในการเกษตร

---
*จัดทำและพัฒนาโดย อ.ชีวะ ทัศนา (เมษายน 2026)*
