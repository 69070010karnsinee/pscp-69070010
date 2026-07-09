1. ข้อมูล OJ
หมายเลข/ชื่อโจทย์ OJ: สลับตัวอักษร 2996
OJ submission ID ถ้ามีการส่งแล้ว: 541904
สถานะ OJ: pass
เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง: 0-15
2. ความเข้าใจโจทย์ของฉัน
input คือ ชื่อคน output คือ ชื่อคนนั้นสะกดกลับหลัง ผลลัพธ์ต้องเป็นตัวพิมพ์เล็กจึงใช้ .lower() ที่ input ตัวที่่รับมาจะได้เป็นตัวพิมพ์เล็ก ใช้ [start:stop:step] ในการสะกด input กลับหลังโดย step = -1 
3. แผนแรกของฉัน
step 1: รับชื่อคนเป็น input string
step 2: เปลี่ยน input ให้เป็นตัวพิมพ์เล็กทั้งหมด
step 3: สะกดชื่อคนกลับหลัง
step 4: print output
4. วิธีสุดท้ายที่ใช้จริง
step 1: รับชื่อคนเป็น input string
step 2: เปลี่ยน input ให้เป็นตัวพิมพ์เล็กทั้งหมด
step 3: สะกดชื่อคนกลับหลังโดยใช้ [start:stop:step]
step 4: print output
5. การทดสอบของฉัน
Test Case 1
ทำไมเลือก case นี้: ทดสอบว่าได้ output เป็นตัวพิมพ์เล็กหรือไม่
Input: GRACE
Expected output: ecarg
Actual output: ecarg
Result: Pass
Test Case 2
ทำไมเลือก case นี้: ทดสอบว่าได้ output ถูกต้องหรือไม่
Input: Jasmine
Expected output: enimsaj
Actual output: enimsaj
Result: Pass
Test Case 3
ทำไมเลือก case นี้: ทดสอบว่าได้ output ถูกต้องหรือไม่
Input: yagami
Expected output: imagay
Actual output: imagay
Result: Pass
6. การใช้ AI
No
7. ความช่วยเหลือจากคน / การร่วมมือ
Yes
ใครช่วยคุณ: เพื่อน
เขาช่วยอะไร: วิธีการ [start:stop:step]
คุณยังทำอะไรด้วยตนเอง: เขียนโค้ดที่เหลือ
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