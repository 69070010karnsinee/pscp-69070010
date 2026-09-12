1. ข้อมูล OJ
หมายเลข/ชื่อโจทย์ OJ: กบน้อยกระโดด 3232
OJ submission ID ถ้ามีการส่งแล้ว: 
สถานะ OJ: pass
เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง: 15-30 นาที
2. ความเข้าใจโจทย์ของฉัน
กบจะกระโดดได้ x เมตรต่อครั้งและครั้งต่อๆมาจะลดลงทีละ 2 ให้แสดงผลว่ากบกระโดดกี่ครั้งจึงจะถึงเป้าหมาย
3. แผนแรกของฉัน
step 1: รับ input ระยะที่กบกระโดดได้และระยะเป้าหมายโดยใช้ string slicing เก็บตัวแปรแยกเป็นจำนวนเต็ม
step 2: สร้าง while loop ระหว่างที่ระยะที่กระโดดน้อยกว่า 0 ให้บวกจำนวนระยะไปเรื่อยเก็บไว้ในตัวแปรdistanceและเก็บตัวแปรจำนวนครั้งที่กระโดดโดยให้ +1 ทุกครั้งที่วนลูป ลูปจะหยุดต่อเมื่อdistance >= ระยะเป้าหมายและให้ระยะที่กบกระโดด-2
step 3 : กำหนดเงื่อนไขหาก distance >= ระยะเป้าหมายให้แสดงผลจำนวนครั้งที่กระโดด นอกเหนือจากนั้นให้แสดงผล -1
4. วิธีสุดท้ายที่ใช้จริง
step 1: รับ input ระยะที่กบกระโดดได้และระยะเป้าหมายโดยใช้ string slicing เก็บตัวแปรแยกเป็นจำนวนเต็ม
step 2: สร้าง while loop ระหว่างที่ระยะที่กระโดดน้อยกว่า 0 ให้บวกจำนวนระยะไปเรื่อยเก็บไว้ในตัวแปรdistanceและเก็บตัวแปรจำนวนครั้งที่กระโดดโดยให้ +1 ทุกครั้งที่วนลูป ลูปจะหยุดต่อเมื่อdistance >= ระยะเป้าหมายและให้ระยะที่กบกระโดด-2
step 3 : กำหนดเงื่อนไขหาก distance >= ระยะเป้าหมายให้แสดงผลจำนวนครั้งที่กระโดด นอกเหนือจากนั้นให้แสดงผล -1
5. การทดสอบของฉัน
Test Case 1
ทำไมเลือก case นี้: ทดสอบว่าแสดง output ที่ถูกต้องหรือไม่
Input: 2 10
Expected output: -1
Actual output: -1
Result: Pass
Test Case 2
ทำไมเลือก case นี้: ทดสอบว่าแสดง output ที่ถูกต้องหรือไม่
Input: 25 80
Expected output: 4
Actual output: 4
Result: Pass
Test Case 3
ทำไมเลือก case นี้: ทดสอบว่าแสดง output ที่ถูกต้องหรือไม่
Input: 0 0
Expected output: 0
Actual output: 0
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