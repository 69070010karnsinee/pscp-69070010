1. ข้อมูล OJ
หมายเลข/ชื่อโจทย์ OJ: Season 3025
OJ submission ID ถ้ามีการส่งแล้ว: 548028
สถานะ OJ: pass
เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง: 0-15 นาที
2. ความเข้าใจโจทย์ของฉัน
ฤดูกาลทุกสามเดือนและทุกวันที่ 21 จะเปลี่ยนเริ่มจาก winter ไป spring ไป summer ไป fall เขียนเงื่อนไขว่าฤดูกาลเปลี่ยนทุกๆสามเดือนและเงื่อไขย่อยว่าเปลี่ยนวันที่ 21
3. แผนแรกของฉัน
step 1: รับ input เดือนและวันที่เป็นจำนวนเต็ม
step 2: กำหนดเงื่อนไขฤดูกาลแต่ละเดือน เช่น หากเป็นเดือนที่ 1-3 ฤดูกาลคือ winter
step 3: กำหนดเงื่อนไขซ้อนว่าหากหลังจากวันที่ 21 ของเดือนที่ 3,6,9,12 จะเปลี่ยนฤดูกาล
4. วิธีสุดท้ายที่ใช้จริง
step 1: รับ input เดือนและวันที่เป็นจำนวนเต็ม
step 2: กำหนดเงื่อนไขฤดูกาลแต่ละเดือน เช่น หากเป็นเดือนที่ 1-3 ฤดูกาลคือ winter
step 3: กำหนดเงื่อนไขซ้อนว่าหากหลังจากวันที่ 21 ของเดือนที่ 3,6,9,12 จะเปลี่ยนฤดูกาล
5. การทดสอบของฉัน
Test Case 1
ทำไมเลือก case นี้: ตรวจสอบว่า output ถูกต้องหรือไม่
Input: 3
13
Expected output: winter
Actual output: winter
Result: Pass
Test Case 2
ทำไมเลือก case นี้: ทดสอบเงื่อนไขฤดูกาลเปลี่ยนวันที่ >= 21
Input: 6
21
Expected output: summer
Actual output: summer
Result: Pass
Test Case 3
ทำไมเลือก case นี้: ทดสอบว่าแสดง output ที่ถูกต้องหรือไม่
Input: 12
12
Expected output: fall
Actual output: fall
Result: Pass
6. การใช้ AI
No
7. ความช่วยเหลือจากคน / การร่วมมือ
์No
8. คำรับรองของนักศึกษา
Statement	Yes/No
I wrote this submission in my own words. Yes	
I understand my final code.	Yes
I recorded the real OJ status.	Yes
I did not copy AI-generated text directly into this file. Yes
I did not copy code from another person. Yes
If I received human help, I disclosed it in this file.	Yes
I submitted the final code to the OJ by myself.	Yes