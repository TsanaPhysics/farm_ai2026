import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def fetch_nasa_power_data(lat, lon, start_date, end_date):
    """
    ดึงข้อมูลสภาพอากาศสำหรับการเกษตรจาก NASA POWER API
    """
    url = "https://power.larc.nasa.gov/api/temporal/daily/point"
    
    # พารามิเตอร์ที่สำคัญสำหรับการเกษตร:
    # T2M: อุณหภูมิเฉลี่ยที่ 2 เมตร
    # PRECTOTCORR: ปริมาณน้ำฝนที่ปรับแก้แล้ว
    # RH2M: ความชื้นสัมพัทธ์ที่ 2 เมตร
    # ALLSKY_SFC_SW_DWN: การแผ่รังสีดวงอาทิตย์ (Insolation)
    
    parameters = "T2M,PRECTOTCORR,RH2M,ALLSKY_SFC_SW_DWN"
    
    params = {
        "request": "execute",
        "power_project": "AGR", # Agroclimatology
        "temporal_api": "daily",
        "latitude": lat,
        "longitude": lon,
        "start": start_date,
        "end": end_date,
        "parameters": parameters,
        "format": "JSON"
    }
    
    print(f"--- กำลังดึงข้อมูลจาก NASA POWER สำหรับพิกัด ({lat}, {lon}) ---")
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        # แปลงข้อมูลจาก JSON เป็น DataFrame
        records = data['properties']['parameter']
        df = pd.DataFrame(records)
        
        # ปรับแต่งวันที่ (Index)
        df.index = pd.to_datetime(df.index, format='%Y%m%d')
        df.index.name = 'Date'
        
        return df
    else:
        print(f"Error: ไม่สามารถดึงข้อมูลได้ (Status Code: {response.status_code})")
        return None

# --- ตัวอย่างการใช้งาน ---

# 1. กำหนดค่า (ตัวอย่าง: จังหวัดจันทบุรี)
lat = 12.611
lon = 102.103
end_date = (datetime.now() - timedelta(days=2)).strftime('%Y%m%d') # ข้อมูล NASA มักจะดีเลย์ 2 วัน
start_date = (datetime.now() - timedelta(days=32)).strftime('%Y%m%d') # ดึงข้อมูลย้อนหลัง 1 เดือน

df_weather = fetch_nasa_power_data(lat, lon, start_date, end_date)

if df_weather is not None:
    print("\n--- ตัวอย่างข้อมูล 5 วันล่าสุด ---")
    print(df_weather.tail())
    
    # 2. บันทึกข้อมูลเป็น CSV
    file_path = "/Applications/XAMPP/xamppfiles/htdocs/farm_ai/data/raw/nasa_weather_data.csv"
    df_weather.to_csv(file_path)
    print(f"\nบันทึกไฟล์เรียบร้อยที่: {file_path}")
    
    # 3. สร้างกราฟวิเคราะห์เบื้องต้น
    plt.figure(figsize=(12, 6))
    
    # กราฟอุณหภูมิ
    plt.subplot(2, 1, 1)
    plt.plot(df_weather.index, df_weather['T2M'], color='red', marker='o')
    plt.title('Daily Average Temperature (C) - NASA POWER')
    plt.ylabel('Temp (C)')
    plt.grid(True)
    
    # กราฟปริมาณฝน
    plt.subplot(2, 1, 2)
    plt.bar(df_weather.index, df_weather['PRECTOTCORR'], color='blue', alpha=0.7)
    plt.title('Daily Precipitation (mm)')
    plt.ylabel('Rainfall (mm)')
    plt.xlabel('Date')
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('/Applications/XAMPP/xamppfiles/htdocs/farm_ai/output/images/weather_analysis.png')
    print("สร้างกราฟวิเคราะห์สภาพอากาศเรียบร้อยที่: output/images/weather_analysis.png")

    # plt.show()
