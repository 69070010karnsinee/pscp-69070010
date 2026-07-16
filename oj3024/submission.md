1. ข้อมูล OJ
หมายเลข/ชื่อโจทย์ OJ: SurprisingVote 3024
OJ submission ID ถ้ามีการส่งแล้ว: 552887
สถานะ OJ: pass
เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง: 15-30 นาที
2. ความเข้าใจโจทย์ของฉัน
ให้หาว่าคะแนนสูงสุดและคะแนนต่ำสุดของทั้งสามคนนี้ห่างกันเกินสองคะแนนหรือไม่หากห่างเกินสองคะแนนจะแสดง "Surprising" หากไม่ใช่จะแสดง "Not Surprising"
3. แผนแรกของฉัน
step 1: รับ input คะแนนรวมของทั้งสามคนและคะแนนสูงสุด
step 2: หาคะแนนต่ำสุดโดยนำคะแนนรวมมาลบกับคะแนนสูงสุดคูณสอง
step 3: เขียนเงื่อนไขว่าหากคะแนนต่ำสุดน้อยกว่า 0 ให้เท่ากับ 0
step 4: เขียนเงื่อนไขว่าหากคะแนนสูงสุดลบคะแนนต่ำสุดมากกว่า 2 ให้แสดงผลเป็น Surprising และหากไม่ใช่ให้แสดงผล Not surprising
4. วิธีสุดท้ายที่ใช้จริง
step 1: รับ input คะแนนรวมของทั้งสามคนและคะแนนสูงสุด
step 2: หาคะแนนต่ำสุดโดยนำคะแนนรวมมาลบกับคะแนนสูงสุดคูณสอง
step 3: เขียนเงื่อนไขว่าหากคะแนนต่ำสุดน้อยกว่า 0 ให้เท่ากับ 0
step 4: เขียนเงื่อนไขว่าหากคะแนนสูงสุดลบคะแนนต่ำสุดมากกว่า 2 ให้แสดงผลเป็น Surprising และหากไม่ใช่ให้แสดงผล Not surprising
5. การทดสอบของฉัน
Test Case 1
ทำไมเลือก case นี้: ทดสอบว่า input ที่เป็นตัวพิมพ์เล็กแสดง output ที่ถูกต้องหรือไม่
Input: 10
5
Expected output: Surprising
Actual output: Surprising
Result: Pass
Test Case 2
ทำไมเลือก case นี้: ทดสอบว่า input ที่เป็นตัวพิมพ์เล็กแสดง output ที่ถูกต้องหรือไม่
Input: 50
5
Expected output: 
Expected output: Not surprising
Actual output: Not surprising
Result: Pass
Test Case 3
ทำไมเลือก case นี้: ทดสอบว่า input ที่เป็นตัวพิมพ์เล็กแสดง output ที่ถูกต้องหรือไม่
Input: 20
8
Expected output: Surprising
Actual output: Surprising
Result: Pass
6. การใช้ AI
No
7. ความช่วยเหลือจากคน / การร่วมมือ
Yes
ใครช่วยคุณ: พี่ TA
เขาช่วยอะไร: ช่วยทำความเข้าใจโจทย์
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