# 1
# n = int(input("Nhap n: "))
# print("KQ: ",(n * 3) + 1)
# 2
# n = float(input("Nhap n: "))
# print("KQ: ",(n ** 2) / 3)
# 3
# n = float(input("Nhap do c: "))
# print("Do F: ",(n * (9/5)) + 32)
# 4
# a = float(input("Nhap a: "))
# print(a%2==0)
# 5
# a = float(input("Nhap a: "))
# print(a%3==0 and a<=100 and a>=50)
# 6 Nhập vào số nguyên a, nếu a là số chia hết cho 5 nhưng KHÔNG nằm trong khoảng từ 20 - 70 thì in ra True, ngược lại in ra False
# a = float(input("Nhap a: "))
# print(a%5==0 and not( a<=20 and a>=70))
# 7 Nhập vào nguyên a và b, nếu 1 trong 2 số a và b chia hết cho 2 thì in ra True, ngược lại in ra False
# a = float(input("Nhap a: "))
# b = float(input("Nhap b: "))
# print(a%2==0 or b%2==0)
# 8 Nhập vào số thực a, kiểm tra xem a có phải là số nguyên hay không, nếu có thì in ra True, ngược lại in ra False
# a = float(input("Nhap a: "))
# print(a==round(a))
# 9 Nhập vào số nguyên a, kiểm tra xem a có phải là số chính phương hay không, nếu có thì in ra True, ngược lại in ra False
# a = int(input("Nhap a: "))
# cana = a**0.5
# print(cana == round(cana))
# 10 Nhập vào lương tháng này nhận được, ta phải đưa cho vợ 90% số tiền lương đó. Hãy in ra lương ta giữ lại
# luong = float(input("Nhap luong: "))
# print("Luong con lai: ", luong*0.1)
# 11 Nhập vào 3 số a, b, c. In ra kết quả là tổng của ba số đó
# a = float(input("Nhap a: "))
# b = float(input("Nhap b: "))
# c = float(input("Nhap c: "))
# print("Tong: ", a+b+c)
# 12 Nhập vào 3 số a, b, c. Tính và in ra d = (a + b)^c Nếu d là số trong khoảng từ 100 - 200 thì in ra True, ngược lại in ra False
# a = float(input("Nhap a: "))
# b = float(input("Nhap b: "))
# c = float(input("Nhap c: "))
# d = (a+b)**c
# print(100<= d <= 200)
# 13 Nhập vào số nguyên dương a, nếu a lớn hơn 10 thì ta in ra đây là số lớn hơn 10
# a = int(input("Nhap a: "))
# if a>10:
#     print(a, "la so lon hon 10")
# 14 Nhập vào số nguyên dương a, nếu a là số chẵn thì in ra đây là số chẵn, ngược lại in ra đây là số lẻ
# a = int(input("Nhap a: "))
# if a%2==0:
#     print(a, "la so chan")
# else:
#     print(a, "la so le")
# 15 Nhập vào 3 số thực dương a, b, c. Kiểm tra xem a, b, c có cấu thành độ dài của 1 tam giác được không
# a = float(input("Nhap a: "))
# b = float(input("Nhap b: "))
# c = float(input("Nhap c: "))
# if a+b>c and a+c>b and b+c>a:
#     print("day la mot tam giac")
# else:
#     print("day khong phai la mot tam giac")
# 16 Từ bài số 15, nếu a, b, c cấu tạo thành được một tam giác, kiểm tra xem đó là tam giác gì (tam giác đều, tam giác vuông cân, tam giác vuông, tam giác cân hay tam giác thường)
# 17 Nhập vào 3 số a, b, c. Hãy sắp xếp 3 số a, b, c theo thứ tự tăng dần rồi in ra lại
# a = int(input("Nhap a: "))
# b = int(input("Nhap b: "))
# c = int(input("Nhap c: "))
# if a>b and a>c:
#     if b>c:
#         a,b,c = c,b,a
#     else:
#         a,b,c = b,c,a
# elif b>a and b>c:
#     if a>c:
#         a,b,c = c,a,b
#     else:
#         a,b,c = a,c,b
# print(a,b,c)
# 23 In 10 lần chữ hello ra màn hình
# for i in range(10):
#     print("Hello")
# 24 In các số lẻ dương bé hơn 100
# for i in range(0,100):
#     if i %2!=0:
#         print(i)
# 25 In các số chẵn chia hết cho 3 bé hơn 100
# for i in range(0,100):
#     if i%2==0 and i%3==0:
#         print(i)
# 26 Nhập vào số nguyên dương a, in ra bảng cửu chương của a
# a = int(input("Nhap a: "))
# for i in range(1, 10+1):
#     print (a, "x", i ,"=", a*i)
# 27 Viết chương trình in ra hình tam giác có độ cao h được nhập từ bàn phím
a = int(input("Nhap a: "))
khoangtrangngoai = a -1
khoangtrangtrong = 0
for i in range(a):
    if i == 0:
        print(" " * khoangtrangngoai + "*")
    elif i < a-1:
        print(" " * (khoangtrangngoai - 1) + "*" + " " * (khoangtrangtrong +1) + "*")
        khoangtrangngoai -=1
        khoangtrangtrong +=2
    else:
        
        print("*" * (a*2-1))