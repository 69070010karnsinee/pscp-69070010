1. ข้อมูล OJ
หมายเลข/ชื่อโจทย์ OJ: Colors 3011
OJ submission ID ถ้ามีการส่งแล้ว: 543865
สถานะ OJ: pass
เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง: 30-45 นาที
2. ความเข้าใจโจทย์ของฉัน
input จะมีสองอย่างคือสีที่ 1 และสีที่ 2 ใช้ if-else ในการกำหนดเงื่อนไขว่าสีไหนผสมได้สีอะไรและ else ให้ input นอกเหนือจากแม่สีแสดง output เป็น Error
3. แผนแรกของฉัน
step 1: รับ input สีที่ 1 และสีที่ 2
step 2: กำหนดเงื่อนไขว่าสีอะไรผสมกันได้สีอะไรโดยลำดับสีสลับกันได้
step 3: กำหนดเงื่อนไขว่าหากมี input นอกเหนือจากแม่สีให้แสดง Error
4. วิธีสุดท้ายที่ใช้จริง
step 1: รับ input สีที่ 1 และสีที่ 2
step 2: ใช้ .lower() เพื่อให้ input เป็นตัวพิพม์เล็กทั้งหมด
step 2: กำหนดเงื่อนไขว่าสีอะไรผสมกันได้สีอะไรโดยลำดับสีสลับกันได้
step 3: กำหนดเงื่อนไข input สีที่ 1 และ 2 เหมือนกัน
step 4: กำหนดเงื่อนไขว่าหากมี input นอกเหนือจากแม่สีให้แสดง Error
5. การทดสอบของฉัน
Test Case 1
ทำไมเลือก case นี้: ทดสอบว่า input ที่เป็นตัวพิมพ์เล็กแสดง output ที่ถูกต้องหรือไม่
Input: red
yellow
Expected output: Orange
Actual output: Orange
Result: Pass
Test Case 2
ทำไมเลือก case นี้: ทดสอบว่าหากสี่ที่ 1 และ 2 เหมือนกันจะได้ output ถูกต้องหรือไม่
Input: Red
Red
Expected output: Red
Actual output: Red
Result: Pass
Test Case 3
ทำไมเลือก case นี้: ทดสอบว่าหาก input ไม่ใช่แม่สีจะแสดง Error หรือไม่
Input: Yellow
H
Expected output: Error
Actual output: Error
Result: Pass
6. การใช้ AI
No
7. ความช่วยเหลือจากคน / การร่วมมือ
Yes
ใครช่วยคุณ: เพื่อน
เขาช่วยอะไร: แนะนำว่ายังมีกรณีที่สสีที่ 1 และ 2 เหมือนกัน
คุณยังทำอะไรด้วยตนเอง: เขียนโค้ดกรณีที่สีที่1 และ 2 เหมือนกัน
คุณคัดลอก code จากคนอื่นหรือไม่: No
ใครช่วยคุณ: อาจาร์ย
เขาช่วยอะไร: แนะนำว่าโค้ดบรรทัดไหนยังมีส่วนที่ผิด
คุณยังทำอะไรด้วยตนเอง: แก้โค้ดในส่วนที่ผิด
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