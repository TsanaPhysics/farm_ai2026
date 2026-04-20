# 🚜 คู่มืออบรมเชิงปฏิบัติการ: Python xAI Next GEN Young Digital Scientist
**หลักสูตร:** การประยุกต์ใช้ปัญญาประดิษฐ์เชิงพื้นที่ (GeoSpatial AI) เพื่อการเกษตรแม่นยำและความยั่งยืน

---

## 📅 กำหนดการอบรม (Workshop Agenda)

### 🗓️ วันที่ 1: พื้นฐาน AI และการเตรียมสภาพแวดล้อม
| เวลา | หัวข้อกิจกรรม | รายละเอียด |
| :--- | :--- | :--- |
| 09:00 - 09:30 | **ลงทะเบียน & ปฐมนิเทศ** | ชี้แจงวัตถุประสงค์และภาพรวมของเทคโนโลยี GeoSpatial AI |
| 09:30 - 10:30 | **บรรยาย: อนาคตเกษตรดิจิทัล** | บทบาทของ AI ในการแก้ปัญหาภาวะโลกร้อนและความมั่นคงทางอาหาร |
| 10:30 - 10:45 | *พักรับประทานอาหารว่าง* | |
| 10:45 - 12:00 | **Lab 1: Environment Setup** | ติดตั้ง Docker, Python และ FarmVibes.AI Local Cluster |
| 12:00 - 13:00 | *พักรับประทานอาหารกลางวัน* | |
| 13:00 - 14:30 | **Lab 2: Hello GeoSpatial AI** | เชื่อมต่อ Python Client และรัน Workflow "Hello World" ครั้งแรก |
| 14:30 - 14:45 | *พักรับประทานอาหารว่าง* | |
| 14:45 - 16:30 | **Lab 3: Data Exploration** | การเลือกพิกัดแปลงเกษตรและการดึงภาพถ่ายดาวเทียม (Sentinel-2) |

### 🗓️ วันที่ 2: การวิเคราะห์เชิงลึกและโปรเจกต์ยุวเกษตร
| เวลา | หัวข้อกิจกรรม | รายละเอียด |
| :--- | :--- | :--- |
| 09:00 - 10:30 | **Lab 4: NDVI & Harvest Prediction** | วิเคราะห์ดัชนีพืชพรรณและคาดการณ์ช่วงเวลาเก็บเกี่ยว |
| 10:30 - 10:45 | *พักรับประทานอาหารว่าง* | |
| 10:45 - 12:00 | **Lab 5: Carbon Footprint AI** | การจำลองการกักเก็บคาร์บอนเพื่อเกษตรกรรมยั่งยืน |
| 12:00 - 13:00 | *พักรับประทานอาหารกลางวัน* | |
| 13:00 - 15:30 | **Challenge: Mini-Project** | แบ่งกลุ่มวิเคราะห์พื้นที่จริงในท้องถิ่นโดยใช้ AI |
| 15:30 - 16:30 | **Pitching & Presentation** | นำเสนอแนวทางการเพิ่มประสิทธิภาพฟาร์มด้วยข้อมูล AI |

---

## 💻 ตัวอย่าง Code สำหรับกิจกรรม (Python Templates)

### 1. การเชื่อมต่อกับ FarmVibes.AI Client
```python
from vibe_core.client import get_default_vibe_client

# เชื่อมต่อกับระบบที่รันอยู่ในเครื่อง (Local Cluster)
client = get_default_vibe_client()

# ตรวจสอบ Workflows ที่มีให้ใช้งาน
workflows = client.list_workflows()
print(f"มี Workflow พร้อมใช้งานทั้งหมด {len(workflows)} รายการ")
print("ตัวอย่าง 5 รายการแรก:", workflows[:5])
```

### 2. การระบุพื้นที่และช่วงเวลา (Geometry & Time Range)
```python
from shapely import geometry as shpg
from datetime import datetime

# กำหนดพื้นที่ (Bounding Box) รอบพิกัดที่สนใจ (ตัวอย่าง: พื้นที่แถว มรภ.รำไพพรรณี)
# Format: shpg.box(min_lon, min_lat, max_lon, max_lat)
geom = shpg.box(102.100, 12.600, 102.110, 12.610)

# กำหนดช่วงเวลาที่ต้องการศึกษา
time_range = (datetime(2023, 1, 1), datetime(2023, 12, 31))

print(f"พื้นที่เป้าหมาย: {geom}")
print(f"ช่วงเวลา: {time_range}")
```

### 3. การรัน Workflow วิเคราะห์ NDVI (ดัชนีพืชพรรณ)
```python
# รัน Workflow สำหรับวิเคราะห์สุขภาพพืช
run_name = "Young_Scientist_NDVI_Test"
workflow_id = "farm_ai/agriculture/ndvi_timeseries" # ตัวอย่าง ID

run = client.run(
    workflow_id, 
    run_name, 
    geometry=geom, 
    time_range=time_range
)

# ติดตามสถานะการทำงาน
print(f"สถานะปัจจุบัน: {run.status}")
run.monitor() # แสดงตารางคืบหน้าการประมวลผล
```

---

## 🛠️ ข้อแนะนำการเตรียมตัวสำหรับวิทยากร
1. **Pre-download Docker Images:** เนื่องจาก Image ของ FarmVibes.AI มีขนาดใหญ่ ควรให้ผู้เข้าอบรมดาวน์โหลด/ดึง Image ไว้ก่อนเริ่มงานผ่านคำสั่ง `farmvibes-ai local setup`
2. **API Keys:** หากต้องการใช้ข้อมูลสภาพอากาศขั้นสูง หรือ Azure Maps อาจต้องเตรียม API Keys ไว้ให้ผู้เข้าอบรม
3. **Dataset:** เตรียมไฟล์ GeoJSON หรือพิกัด Lat/Lon ของพื้นที่เกษตรกรรมในท้องถิ่นไว้เป็นกรณีศึกษา

---

## 📝 เกณฑ์การประเมินผล (Certification Criteria)
- สามารถรัน Workflow และแสดงผลลัพธ์จาก AI ได้สำเร็จ
- สามารถแปลความหมายกราฟ NDVI หรือรายงานคาร์บอนเบื้องต้นได้
- มีส่วนร่วมในกิจกรรมกลุ่ม Mini-Project

---
*จัดทำโดย: ระบบผู้ช่วย AI (Antigravity)*
