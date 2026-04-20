# 🚀 คู่มือการนำโครงการขึ้น GitHub และการใช้งานออนไลน์
**โปรเจกต์:** Farm AI xAI Next GEN 2026

ผมได้ทำการตั้งค่า Git ภายในเครื่อง (Local Repository) และทำการ Commit ไฟล์ทั้งหมดไว้ให้เรียบร้อยแล้ว ขั้นตอนต่อไปคือการเชื่อมโยงกับบัญชี GitHub ของคุณครับ:

---

## 🛠️ ขั้นตอนที่ 1: การนำขึ้น GitHub (Push to GitHub)
1.  **สร้าง Repository ใหม่:** เข้าไปที่ [github.com/new](https://github.com/new) แล้วตั้งชื่อว่า `farm_ai`
2.  **เชื่อมโยงและ Push:** เปิด Terminal ในโฟลเดอร์โครงการแล้วรันคำสั่งดังนี้:
    ```bash
    git remote add origin https://github.com/USER_NAME/farm_ai.git
    git branch -M main
    git push -u origin main
    ```
    *(เปลี่ยน `USER_NAME` เป็นชื่อบัญชี GitHub ของคุณ)*

---

## 🌐 ขั้นตอนที่ 2: การใช้งานออนไลน์ (Deployment)

### A. การแสดงผลหน้าเว็บ (GitHub Pages)
*   คุณสามารถเปิดใช้งาน **GitHub Pages** ในส่วน Settings ของ Repository เพื่อดูหน้า **Landing Page (index.html)** ได้ฟรี
*   **ข้อจำกัด:** GitHub Pages รองรับเฉพาะไฟล์ Static (HTML/CSS/JS) เท่านั้น **ไม่รองรับ PHP และ Python** ดังนั้นระบบ AI หลังบ้านจะไม่ทำงานในส่วนนี้

### B. การใช้งานระบบ AI แบบเต็มรูปแบบ (Full Stack Hosting)
เพื่อให้ระบบวิเคราะห์ดินและ API ทำงานได้ออนไลน์จริง คุณต้องใช้บริการ Hosting ที่รองรับ **PHP และ Python** เช่น:
1.  **VPS (DigitalOcean / AWS / Linode):** ติดตั้ง LAMP Stack และ Python สภาพแวดล้อมจะเหมือนใน XAMPP ที่เราพัฒนา
2.  **PythonAnywhere:** เหมาะสำหรับการรันสคริปต์ AI และ API โดยเฉพาะ
3.  **Heroku:** รองรับทั้ง PHP และ Python ผ่านการตั้งค่า Buildpacks

---

## 📱 การตั้งค่าสำหรับสมาร์ทโฟนในอนาคต
เมื่อคุณนำโครงการขึ้น Server ออนไลน์แล้ว:
1.  แก้ไข URL ในไฟล์ `website/admin/index.php` (ส่วนที่สร้าง QR Code) ให้เป็น URL ของ Server จริง
2.  สมาร์ทโฟนจากทุกที่ในโลกจะสามารถสแกน QR Code และส่งภาพมาวิเคราะห์ที่เซิร์ฟเวอร์ของคุณได้ทันทีครับ

---
*จัดทำโดย: ทีมพัฒนา Antigravity AI (20 เมษายน 2026)*
