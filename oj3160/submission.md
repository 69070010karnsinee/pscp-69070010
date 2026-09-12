1. ข้อมูล OJ
หมายเลข/ชื่อโจทย์ OJ: หาจำนวนเฉพาะ 3160
OJ submission ID ถ้ามีการส่งแล้ว: 
สถานะ OJ: pass
เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง: 15-30 นาที
2. ความเข้าใจโจทย์ของฉัน
ให้แสดงจำนวนเฉพาะภายใน range ที่ใส่ input มาในบรรทัดเดียวและแสดงผลรวมว่ามีจำนวนเฉพาะกี่ตัวด้วย
3. แผนแรกของฉัน
step 1: รับ input start stop โดยการใช้ map
step 2: สร้าง for loop range start ถึง stop+1 และกำหนดให้ i มากกว่า 0 ถึงจะเข้าเงื่อนไขต่อไป
step 3 : สร้าง for loop ซ้อนอีกโดยมี range 2 ถึงรูท i+1 เนื่องจากตัวที่นำไปหารจะไม่เกินเลขนั้นอยู่แล้ว
step 4: กำหนดเงื่อนไขในลูปว่าถ้า j หาร i ลงตัวให้หยุด นอกเหนือจากนั้นให้เพิ่มเข้าไปในลิสต์ num
step 5: กำหนดเงื่อนไขว่าหาก num ไม่มีตัวเลขในลืสต์ ไม่ต้องแสดงผลออกมาและให้แสดงแค่จำนวนเลขใน num 
4. วิธีสุดท้ายที่ใช้จริง
step 1: รับ input start stop โดยการใช้ map
step 2: สร้าง for loop range start ถึง stop+1 และกำหนดให้ i มากกว่า 0 ถึงจะเข้าเงื่อนไขต่อไป
step 3 : สร้าง for loop ซ้อนอีกโดยมี range 2 ถึงรูท i+1 เนื่องจากตัวที่นำไปหารจะไม่เกินเลขนั้นอยู่แล้ว
step 4: กำหนดเงื่อนไขในลูปว่าถ้า j หาร i ลงตัวให้หยุด นอกเหนือจากนั้นให้เพิ่มเข้าไปในลิสต์ num
step 5: กำหนดเงื่อนไขว่าหาก num ไม่มีตัวเลขในลืสต์ ไม่ต้องแสดงผลออกมาและให้แสดงแค่จำนวนเลขใน num 
Test Case 1
ทำไมเลือก case นี้: ทดสอบว่าแสดง output ที่ถูกต้องหรือไม่
Input: 30 60
Expected output: 31 37 41 43 47 53 59
Total primes: 7
Actual output: 31 37 41 43 47 53 59
Total primes: 7
Result: Pass
Test Case 2
ทำไมเลือก case นี้: ทดสอบว่าแสดง output ที่ถูกต้องหรือไม่
Input: 1 7
Expected output: 2 3 5 7
Total primes: 4
Actual output: 2 3 5 7
Total primes: 4
Result: Pass
Test Case 3
ทำไมเลือก case นี้: ทดสอบว่าแสดง output ที่ถูกต้องหรือไม่
Input: 13 20
Expected output: 3 17 19
Total primes: 3
Actual output: 3 17 19
Total primes: 3
Result: Pass
6. การใช้ AI
No
7. ความช่วยเหลือจากคน / การร่วมมือ
Yes
ใครช่วยคุณ: เพื่อน
เขาช่วยอะไร: แนะนำให้ใช้ loop ซ้อน loop
คุณยังทำอะไรด้วยตนเอง: เขียนโค้ดเอง
คุณคัดลอก code จากคนอื่นหรือไม่: No
8. คำรับรองของนักศึกษา
Statement	Yes/No
I wrote this submission in my own words. Yes	
I understand my final code.	Yes
I recorded the real OJ status.	Yes
I did not copy AI-generated text directly into this file. Yes
I did not copy code from another person. Yes
If I received human help, I disclosed it in this file.	Yes
I submitted the final code to the OJ by myself.	Yes