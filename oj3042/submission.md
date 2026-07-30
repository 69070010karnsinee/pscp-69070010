1. ข้อมูล OJ
หมายเลข/ชื่อโจทย์ OJ: หาร 10 3042
OJ submission ID ถ้ามีการส่งแล้ว: 557750
สถานะ OJ: pass
เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง: 15-30 นาที
2. ความเข้าใจโจทย์ของฉัน
ให้รับ input เป็นเลขจำนวนเต็มจากนั้นทำให้เลขนั้นลงท้ายด้วย 0 จากนั้นแสดงผลเลขที่หารด้วย 10 ลงตัวโดยการใช้ for loop โดย range จะนับลงจากเลข input และ step ทีละ -10
3. แผนแรกของฉัน
step 1: รับ input เลขจำนวนเต็มบวก N
step 2: ใช้ % หาจำนวนที่นำไปลบออกเพื่อให้เลข input ลงท้ายด้วย 0
step 3 : ใช้ for loop ใน range เลข input ลดลงเรื่อยๆทีละ 10
step 4: แสดงผลโดยใช้ end"" เพื่อให้แสดงเลขเว้นวรรค
4. วิธีสุดท้ายที่ใช้จริง
step 1: รับ input เลขจำนวนเต็มบวก N
step 2: ใช้ % หาจำนวนที่นำไปลบออกเพื่อให้เลข input ลงท้ายด้วย 0
step 3 : ใช้ for loop ใน range เลข input ลดลงเรื่อยๆทีละ 10
step 4: แสดงผลโดยใช้ end"" เพื่อให้แสดงเลขเว้นวรรค
5. การทดสอบของฉัน
Test Case 1
ทำไมเลือก case นี้: ทดสอบว่าแสดง output ที่ถูกต้องหรือไม่
Input: 100,000
Expected output: 631
Actual output: 631
Result: Pass
Test Case 2
ทำไมเลือก case นี้: ทดสอบว่าแสดง output ที่ถูกต้องหรือไม่
Input: 30
Expected output: 30 20 10 0
Actual output: 30 20 10 0
Result: Pass
Test Case 3
ทำไมเลือก case นี้: ทดสอบว่าแสดง output ที่ถูกต้องหรือไม่
Input: 100
Expected output: 100 90 80 70 60 50 40 30 20 10 0
Actual output: 100 90 80 70 60 50 40 30 20 10 0
Result: Pass
6. การใช้ AI
No
7. ความช่วยเหลือจากคน / การร่วมมือ
Yes
ใครช่วยคุณ: พี่ TA
เขาช่วยอะไร: พี่บอกให้ลองใช้ % เพื่อทำให้เลขลงท้ายด้วย 0
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