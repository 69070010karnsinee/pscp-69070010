1. ข้อมูล OJ
หมายเลข/ชื่อโจทย์ OJ: ของขวัญและขโมย 3135
OJ submission ID ถ้ามีการส่งแล้ว: 
สถานะ OJ: pass
เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง: 15-30 นาที
2. ความเข้าใจโจทย์ของฉัน
ให้แสดงว่ามีคนที่ได้พิจารณาของขวัญกี่คน เมื่อเริ่มที่คนแรกและบวก k คนที่ต่อๆไป จะหยุดต่อเมื่อวนกลับไปถึงคนแรกหรือถึงมือโจร
3. แผนแรกของฉัน
step 1: ใช้ map รับ input n,k,t
step 2: สร้าง while loop และกำหนดให้เพิ่มจำนวนคนที่พิจารณาของขวัญไปเรื่อยๆจนกว่า current จะเท่ากับตำแหน่งโจร หรือ คำนวนตำแหน่งการวนโดย เอาตำแหน่งบวก k-1 เศษของการที่เอา n+1 ไปหารจะได้ตำแหน่งนั้น และจะหยุดเมื่อ current เท่ากับ 1
step 3 : แสดงผล people
4. วิธีสุดท้ายที่ใช้จริง
step 1: ใช้ map รับ input n,k,t
step 2: สร้าง while loop และกำหนดให้เพิ่มจำนวนคนที่พิจารณาของขวัญไปเรื่อยๆจนกว่า current จะเท่ากับตำแหน่งโจร หรือ คำนวนตำแหน่งการวนโดย เอาตำแหน่งบวก k-1 เศษของการที่เอา n+1 ไปหารจะได้ตำแหน่งนั้น และจะหยุดเมื่อ current เท่ากับ 1
step 3 : แสดงผล people
5. การทดสอบของฉัน
Test Case 1
ทำไมเลือก case นี้: ทดสอบว่าแสดง output ที่ถูกต้องหรือไม่
Input: 18 9 2
Expected output: 2
Actual output: 2
Result: Pass
Test Case 2
ทำไมเลือก case นี้: ทดสอบว่าแสดง output ที่ถูกต้องหรือไม่
Input: 20 6 7
Expected output: 2
Actual output: 2
Result: Pass
Test Case 3
ทำไมเลือก case นี้: ทดสอบว่าแสดง output ที่ถูกต้องหรือไม่
Input: 24 2 4
Expected output: 12
Actual output: 12
Result: Pass
6. การใช้ AI
No
7. ความช่วยเหลือจากคน / การร่วมมือ
Yes
ใครช่วยคุณ: พี่ TA
เขาช่วยอะไร: ช่วยแนะนำตรงการหาตำแหน่งวนใหม่
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