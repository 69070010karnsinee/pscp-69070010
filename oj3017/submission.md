1. ข้อมูล OJ
หมายเลข/ชื่อโจทย์ OJ: Bill 3017
OJ submission ID ถ้ามีการส่งแล้ว: 543848
สถานะ OJ: pass
เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง: 0-15 นาที
2. ความเข้าใจโจทย์ของฉัน
รับ input เป็นจำนวนเต็มและคำนวนหาค่าบริการจากนั้นกำหนดเงื่อนไขว่าหากค่าบริการน้อยกว่า 50 จะเท่ากับ 50 และถ้ามากกว่า 1000 ให้เท่ากับ 1000 จากนั้นจึงคำนวนค่า vat และแสดง output เป็นทศนิยม2ตำแหน่ง
3. แผนแรกของฉัน
step 1: รับ input จำนวนเงินรวมเป็นจำนวนเต็ม
step 2: หาค่าบริการ 10% ของจำนวนเงินรวม
step 3: กำหนดเงื่อนไขว่าหากค่าบริการน้อยกว่า 50 จะเท่ากับ 50 และหากมากกว่า 1000 จะเท่ากับ 1000
step 4: กำหนดค่า จำนวนเงินรวม+ค่าบริการ เพื่อนำไปหาค่า vat
step 5: แสดงค่า vat+จำนวนเงินรวม+ค่าบริการ เป็นทศนิยม2ตำแหน่ง
4. วิธีสุดท้ายที่ใช้จริง
step 1: รับ input จำนวนเงินรวมเป็นจำนวนเต็ม
step 2: หาค่าบริการ 10% ของจำนวนเงินรวม
step 3: กำหนดเงื่อนไขว่าหากค่าบริการน้อยกว่า 50 จะเท่ากับ 50 และหากมากกว่า 1000 จะเท่ากับ 1000
step 4: กำหนดค่า จำนวนเงินรวม+ค่าบริการ เพื่อนำไปหาค่า vat
step 5: แสดงค่า vat+จำนวนเงินรวม+ค่าบริการ เป็นทศนิยม2ตำแหน่ง
5. การทดสอบของฉัน
Test Case 1
ทำไมเลือก case นี้: ทดสอบเงื่อนไขค่าบริการน้อยกว่า 50
Input: 50
Expected output: 107.00
Actual output: 107.00
Result: Pass
Test Case 2
ทำไมเลือก case นี้: ทดสอบเงื่อนไขค่าบริการมากกว่า 1000
Input: 12345
Expected output: 14279.15
Actual output: 14279.15
Result: Pass
Test Case 3
ทำไมเลือก case นี้: ทดสอบว่าแสดง output ที่ถูกต้องหรือไม่
Input: 100
Expected output: 160.50
Actual output: 160.50
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