1. ข้อมูล OJ
หมายเลข/ชื่อโจทย์ OJ: สลากกินแบ่ง 3233
OJ submission ID ถ้ามีการส่งแล้ว: 
สถานะ OJ: pass
เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง: 15-30 นาที
2. ความเข้าใจโจทย์ของฉัน
รับ input เลขสลากของกระต่ายและของรัฐบาลแล้วดูว่าตรงกันตามแต่ละเงื่อนไขจะได้เงินเท่าไหร่
3. แผนแรกของฉัน
step 1: รับ input เลขสลากของกระต่ายและเลขสลากของรัฐบาล
step 2: กำหนดเงื่อนไขหากตรงหับหมายเลขที่ออกแสดวผล 1000000 หากเลขท้ายสองตัวตรงและอักษรตรงได้ 1000 หากไม่ตรงได้ 100 หากเลขท้ายสามตัวตรงและอักษรตรงได้ 2000 หากไม่ตรงได้ 200 หากไม่ตรงเลยจะได้ 0 
4. วิธีสุดท้ายที่ใช้จริง
step 1: รับ input เลขสลากของกระต่ายและเลขสลากของรัฐบาลและใช้ string slicing เก็บไว้ในตัวแปรใหม่
step 2: กำหนดเงื่อนไขหากตรงหับหมายเลขที่ออกแสดวผล 1000000 หากเลขท้ายสองตัวตรงและอักษรตรงได้ 1000 หากไม่ตรงได้ 100 หากเลขท้ายสามตัวตรงและอักษรตรงได้ 2000 หากไม่ตรงได้ 200 หากไม่ตรงเลยจะได้ 0
5. การทดสอบของฉัน
Test Case 1
ทำไมเลือก case นี้: ทดสอบว่าแสดง output ที่ถูกต้องหรือไม่
Input: E 12345
J 12345
Expected output: 100000
Actual output: 100000
Result: Pass
Test Case 2
ทำไมเลือก case นี้: ทดสอบว่าแสดง output ที่ถูกต้องหรือไม่
Input: P 06051
Z 67676
Expected output: 0
Actual output: 0
Result: Pass
Test Case 3
ทำไมเลือก case นี้: ทดสอบว่าแสดง output ที่ถูกต้องหรือไม่
Input: N 69696
N 69696
Expected output: 1000000
Actual output: 1000000
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