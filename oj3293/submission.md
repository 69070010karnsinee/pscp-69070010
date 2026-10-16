1. ข้อมูล OJ
หมายเลข/ชื่อโจทย์ OJ: BigFrame 32
OJ submission ID ถ้ามีการส่งแล้ว: 653806
สถานะ OJ: pass
เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง: 30-45 นาที
2. ความเข้าใจโจทย์ของฉัน
ให้ input ข้อความมาจำนวน 5 บรรทัดและให้ล้อมข้อความนั้นด้วย * เป็นรูปสี่เหลี่ยมโดยมีเว้นวรรคระหว่างข้อความและกรอบ
3. แผนแรกของฉัน
step 1: ใช้ for loop เพื่อรับ input ข้อความและความยาวของข้อความนั้นโดยใข้ strip() เพื่อลบช่องว่างออก จากนั้นเก็บเข้าในลิสต์แยก
step 2: หาข้อความที่ยาวที่สุดโดยใช้ max
step 3 : แสดงผล * คูณความยาวของข้อความที่ยาวที่สุด+4 (ช่องว่างและกรอบ*)
step 4: สร้าง loop for แสดงผล ดอกจัน ข้อความ ช่องว่างหาจากการเอาความยาวข้อความที่ยาวที่สุดลบกับความยาวข้อความ ดอกจัน
step 5: แสดงผล * คูณความยาวของข้อความที่ยาวที่สุด+4 (ช่องว่างและกรอบ*) อีกรอบ
4. วิธีสุดท้ายที่ใช้จริง
step 1: ใช้ for loop เพื่อรับ input ข้อความและความยาวของข้อความนั้นโดยใข้ strip() เพื่อลบช่องว่างออก จากนั้นเก็บเข้าในลิสต์แยก
step 2: หาข้อความที่ยาวที่สุดโดยใช้ max
step 3 : แสดงผล * คูณความยาวของข้อความที่ยาวที่สุด+4 (ช่องว่างและกรอบ*)
step 4: สร้าง loop for แสดงผล ดอกจัน ข้อความ ช่องว่างหาจากการเอาความยาวข้อความที่ยาวที่สุดลบกับความยาวข้อความ ดอกจัน
step 5: แสดงผล * คูณความยาวของข้อความที่ยาวที่สุด+4 (ช่องว่างและกรอบ*) อีกรอบ
5. การทดสอบของฉัน
Test Case 1
ทำไมเลือก case นี้: ทดสอบว่าแสดง output ที่ถูกต้องหรือไม่
Input: sixseven
boyfriend
sad 
queen
pony
Expected output: *************
* sixseven  *
* boyfriend *
* sad       *
* queen     *
* pony      *
*************
Actual output: *************
* sixseven  *
* boyfriend *
* sad       *
* queen     *
* pony      *
*************
Result: Pass
Test Case 2
ทำไมเลือก case นี้: ทดสอบว่าแสดง output ที่ถูกต้องหรือไม่
Input: hello world
world hello
titanic
gojo
mix
Expected output: ***************
* hello world *
* world hello *
* titanic     *
* gojo        *
* mix         *
***************
Actual output: ***************
* hello world *
* world hello *
* titanic     *
* gojo        *
* mix         *
***************
Result: Pass
Test Case 3
ทำไมเลือก case นี้: ทดสอบว่าแสดง output ที่ถูกต้องหรือไม่
Input: nerine
is
very
very
beautiful
Expected output: *************
* nerine    *
* is        *
* very      *
* very      *
* beautiful *
*************
Actual output: *************
* nerine    *
* is        *
* very      *
* very      *
* beautiful *
*************
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