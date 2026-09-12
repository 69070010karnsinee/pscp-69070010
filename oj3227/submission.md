1. ข้อมูล OJ
หมายเลข/ชื่อโจทย์ OJ: ไพ่ 44 ใบ 3227
OJ submission ID ถ้ามีการส่งแล้ว: 
สถานะ OJ: pass
เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง: 15-30 นาที
2. ความเข้าใจโจทย์ของฉัน
รับ input หมายเลขไพ่และกลุ่มของไพ่และแปลงเป็นชื่อไพ่ตามที่โจทย์กำหนด
3. แผนแรกของฉัน
step 1: รับ input และใช้ .upper เพื่อแปลงให้เป็นตัวพิมพ์ใหญ่
step 2: ใช้ string slicing กำหนดเงื่อนไขว่าหากตัวแรกเป็นตัวอักษร A,J,Q,K ให้กำหนดเงื่อนไขย่อยอีกว่าถ้าตำแหน่งถัดไปเป็น D,H,S,C จะแสดงผลเป็นชื่อไพ่ตามเงื่อนไข
step 3 : กำหนดเงื่อนไขว่าหากตัวสุดท้ายเป็น D,H,S,C ให้เขียนเงื่อนไขย่อยว่าหาก len(card) = 3 ให้แสดงผลเป็น 10 และชื่อกลุ่มไพ่
4. วิธีสุดท้ายที่ใช้จริง
step 1: รับ input และใช้ .upper เพื่อแปลงให้เป็นตัวพิมพ์ใหญ่
step 2: ใช้ strinh slicing กำหนดเงื่อนไขว่าหากตัวแรกเป็นตัวอักษร A,J,Q,K ให้กำหนดเงื่อนไขย่อยอีกว่าถ้าตำแหน่งถัดไปเป็น D,H,S,C จะแสดงผลเป็นชื่อไพ่ตามเงื่อนไข
step 3 : กำหนดเงื่อนไขว่าหากตัวสุดท้ายเป็น D,H,S,C ให้เขียนเงื่อนไขย่อยว่าหาก len(card) = 3 ให้แสดงผลเป็น 10 และชื่อกลุ่มไพ่A
step 3 : แสดงผล people
5. การทดสอบของฉัน
Test Case 1
ทำไมเลือก case นี้: ทดสอบว่าแสดง output ที่ถูกต้องหรือไม่
Input: 10H
Expected output: 10 of hearts
Actual output: 10 of hearts
Result: Pass
Test Case 2
ทำไมเลือก case นี้: ทดสอบว่าแสดง output ที่ถูกต้องหรือไม่
Input: AC
Expected output: ace of clubs
Actual output: ace of clubs
Result: Pass
Test Case 3
ทำไมเลือก case นี้: ทดสอบว่าแสดง output ที่ถูกต้องหรือไม่
Input: AH
Expected output: ace of hearts
Actual output: ace of hearts
Result: Pass
6. การใช้ AI
No
7. ความช่วยเหลือจากคน / การร่วมมือ
No
8. คำรับรองของนักศึกษา
Statement	Yes/No
I wrote this submission in my own words. Yes	
I understand my final code.	Yes
I recorded the real OJ status.	Yes
I did not copy AI-generated text directly into this file. Yes
I did not copy code from another person. Yes
If I received human help, I disclosed it in this file.	Yes
I submitted the final code to the OJ by myself.	Yes