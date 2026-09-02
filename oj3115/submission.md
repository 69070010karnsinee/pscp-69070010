1. ข้อมูล OJ
หมายเลข/ชื่อโจทย์ OJ: Arcade of Time: Store Check 3115
OJ submission ID ถ้ามีการส่งแล้ว: 
สถานะ OJ: pass
เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง: 30-45 นาที
2. ความเข้าใจโจทย์ของฉัน
รับ input มาจากนั้นสร้างลิสต์เก็บข้อมูล 1441 ช่องจากนั้นใช้ลูปหาเวลาเปิดปิดของร้าน รับค่าเวลาที่ต้องการตรวจสอบและเช็คกับค่าในลิสต์เพื่อหาจำนวนร้านที่เปิดในเวลานั้น
3. แผนแรกของฉัน
step 1: รับ input ทั้งหมด
step 2: สร้างลิสต์เก็บข้อมูล 1441 ช่อง
step 3: สร้าง for loop ตัวแรกจะรับค่าstartและstopของร้านค้าแต่ละร้าน
จากนั้นใช้ลูป for minute บวกค่าเพิ่ม 1 ในนาทีที่ร้านนั้นเปิดให้บริการ
step 4: รับค่าเวลาที่ต้องการตรวจสอบดึงข้อมูลจากลิสต์ open_stores ตามเวลาที่ระบุเก็บไว้ใน results 
4. วิธีสุดท้ายที่ใช้จริง
step 1: รับ input ทั้งหมด
step 2: สร้างลิสต์เก็บข้อมูล 1441 ช่อง
step 3: สร้าง for loop ตัวแรกจะรับค่าstartและstopของร้านค้าแต่ละร้าน
จากนั้นใช้ลูป for minute บวกค่าเพิ่ม 1 ในนาทีที่ร้านนั้นเปิดให้บริการ
step 4: รับค่าเวลาที่ต้องการตรวจสอบดึงข้อมูลจากลิสต์ open_stores ตามเวลาที่ระบุเก็บไว้ใน results 
5. การทดสอบของฉัน
Test Case 1
ทำไมเลือก case นี้: ทดสอบว่า input แสดง output ที่ถูกต้องหรือไม่
Input: 3 5
540 1020
600 660
1080 1200
600 659 660 900 1000
Expected output: 2 2 1 1 1
Actual output: 2 2 1 1 1
Result: Pass
Test Case 2
ทำไมเลือก case นี้: ทดสอบว่า input แสดง output ที่ถูกต้องหรือไม่
Input: 2 3
0 720
500 1000
100 700 700
Expected output: 1 2 2
Actual output: 1 2 2
Result: Pass
6. การใช้ AI
No
7. ความช่วยเหลือจากคน / การร่วมมือ
์์No
8. คำรับรองของนักศึกษา
Statement	Yes/No
I wrote this submission in my own words. Yes	
I understand my final code.	Yes
I recorded the real OJ status.	Yes
I did not copy AI-generated text directly into this file. Yes
I did not copy code from another person. Yes
If I received human help, I disclosed it in this file.	Yes
I submitted the final code to the OJ by myself.	Yes