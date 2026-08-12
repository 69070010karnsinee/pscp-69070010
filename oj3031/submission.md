1. ข้อมูล OJ
หมายเลข/ชื่อโจทย์ OJ: Ink 3031
OJ submission ID ถ้ามีการส่งแล้ว: 598440
สถานะ OJ: pass
เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง: 30-45 นาที
2. ความเข้าใจโจทย์ของฉัน
รับ input พื้นที่ที่น้ำหมึกแผ่ขยายต่อหนึ่งวินาทีและจำนวนคำร้องจากผู้คนและพิกัดบ้านในบรรทัดต่อๆมา หาว่าน้ำหมึกจะถึงพิกัดนั้นในวินาทีที่เท่าไหร่
3. แผนแรกของฉัน
step 1: รับ input เลขจำนวนเต็มสอวจำนวนในบรรทัดเดียว
step 2: ใช้ for loop รับพิกัดบ้านโดย range เป็น n
step 3 : ใน loop คำนวนหาวินาทีที่น้ำหมึกจะถึงบ้านโดยหาระยะห่างระหว่างจุดพิกัดบ้านกับจุด 0,0 คูณ pi และหาร area และใช้ math.ceil เพื่อให้แสดงจำนวนเต็มเป็นวินาทีถัดไป
step 4: นำวินาทีที่หาได้ใส่ list และใข้ for loop แสดงผล list ออกมาทีละบรรทัด
4. วิธีสุดท้ายที่ใช้จริง
step 1: รับ input เลขจำนวนเต็มสอวจำนวนในบรรทัดเดียว
step 2: ใช้ for loop รับพิกัดบ้านโดย range เป็น n
step 3 : ใน loop คำนวนหาวินาทีที่น้ำหมึกจะถึงบ้านโดยหาระยะห่างระหว่างจุดพิกัดบ้านกับจุด 0,0 คูณ pi และหาร area และใช้ math.ceil เพื่อให้แสดงจำนวนเต็มเป็นวินาทีถัดไป
step 4: นำวินาทีที่หาได้ใส่ list และใข้ for loop แสดงผล list ออกมาทีละบรรทัด
5. การทดสอบของฉัน
Test Case 1
ทำไมเลือก case นี้: ทดสอบว่าแสดง output ที่ถูกต้องหรือไม่
Input: 60 3
5 5
10 10
2 2
Expected output: 3
11
1
Actual output: 3
11
1
Result: Pass
Test Case 2
ทำไมเลือก case นี้: ทดสอบว่าแสดง output ที่ถูกต้องหรือไม่
Input: 30 5
0 0
80 80
2 2 
10 100
40 40 
Expected output: 0
1341
1
1058
336
Actual output: 0
1341
1
1058
336
Result: Pass
Test Case 3
ทำไมเลือก case นี้: ทดสอบว่าแสดง output ที่ถูกต้องหรือไม่
Input: 5 2
50 50
10 12
Expected output: 3142
154
Actual output: 3142
154
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