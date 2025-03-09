'''
a = 1 == 1
b = 2 < 1
print(a)
print(b)
print("-" * 50)

a = 10 > 5
b = 3 == 5
c = 'Python' != 'python'
d = len('apple') > 3
print(a, "\n", b, "\n", c, "\n", d)
print("-" * 50)

money = input('請輸入金額')
if int(money) > 100:
    print("True")

else:
    print("請重新輸入金額")
print("-" * 50)

age = 26
if age < 18:
    print("未成年")

else:
    print("成年")
print("-" * 50)

menu = ['餛飩湯', '蛋炒飯', '水餃', '牛肉麵']
order = input('請輸入餐點')
if order in menu:
    print("點餐完成")
    
else:
    print("未在菜單裡")
print("-" * 50)

price = input('消費金額:')
if int(price) <= 500:
    price = int(price) * 0.9
    print("折扣後的金額:", price)

elif 500 < int(price) <= 1000:
    price = int(price) * 0.8
    print("折扣後的價格:", price)

else:
    price = int(price) * 0.7
    print("折扣後的價格:", price)


score = input('考試成績:')
if 90 <= int(score) <= 100:
    print("A")

elif 80 <= int(score) < 90:
       print("B")

elif 70 <= int(score) < 80:
       print("C")

elif 60 <= int(score) < 70:
     print("D")   

elif 100 <= int(score) or int(score) <= 0:
     print("不合理")  
    
else:
      print("Failed")    
print("-" * 50)

menu = {'滷肉飯': '飯類', '雞肉飯': '飯類', '牛肉麵': '麵類', '咖哩飯': '飯類', '餛飩麵': '麵類', '漢堡': '炸類'}
order = input('請輸入餐點')
if order in menu:
      print(menu[order])
      
else:
      print("未知分類")
print("-" * 50)

age = int(input('請輸入年齡:'))
if age < 13:
    if age < 6:
        print("票價：免費入場")
    else:
        print("票價：半價入場")

elif age <= 64:
      print("票價：原價入場")

else:
      print("票價：敬老票")
print("-" * 50)
    
price = input('消費金額:')
if int(price) <= 500:
    print("未達優惠門檻:", price)

elif 500 < int(price) <= 699:
    price = int(price) * 0.9
    print("折扣後的價格:", price)

elif 700 < int(price) <= 999:
    price = int(price) * 0.85
    print("折扣後的價格:", price)

else:
    price = int(price) * 0.8
    print(f'折扣後的價格: {price:.2f}')

print("-" * 50)


num = 0
for i in range(1,9):
    num += i
    print(num)

print("-" * 50)

menu = ['滷肉飯', '雞肉飯', '牛肉麵', '咖哩飯', '餛飩麵', '漢堡']
for i in menu:
    print(i)

print("-" * 50)

menu_price = {'滷肉飯': 50, '雞肉飯': 55, '牛肉麵': 70, '咖哩飯': 45, '餛飩麵': 35, '漢堡': 65}
for i in menu_price:
    print("品項:", i, "價格:", menu_price[i])

print("-" * 50)


for i in range(1,11):
    print(i)
    if i % 2 == 0:
        print("偶數", i)

print("-" * 50)

num = [5, 12, 8, 3, 15, 7, 20]
sum = 0
for i in num:
    if i > 10:
        sum += i
print(f"總和:{sum}")


正確數字 = 7 
猜數字 = int(input("請輸入一個數字"))

while 猜數字 != 正確數字 :
    print("猜錯了，請再試一次!")
    猜數字 = int(input("請輸入一個數字"))

print("恭喜猜對!")

print("-" * 50)


count = 0
i = 1
while i < 101: 
    count = count + i
    i = i + 1
print(count)

print("-" * 50)

shopping_list = []
wish_list = input('輸入願望清單')

while wish_list != '結束':
    shopping_list.append(wish_list)
    wish_list = input('輸入願望清單')
print(shopping_list)

print("-" * 50)

num = int(input('請輸入1到100之間數字'))
while num not in range (1,101):
    print("請重新輸入數字")
    num = int(input('請重新輸入數字'))

print("-" * 50)

password = "123"
num = input("請輸入密碼")
次數 = 1

if num != password:
    while True:
        if 次數 < 3 :
            次數 += 1
            print("輸入錯誤，請重新再試")
            num = input("請輸入密碼")
        elif 次數 >= 3 :
            print("錯誤太多次，請稍後再試")
            break
        else :
            print("登入成功")
else :
    print("登入成功")

print("-" * 50)
'''

def 計算(a, b):
    sum = a + b
    print(sum)

計算(1, 2)

print("-" * 50)

def 長度(變數):
    a = len(變數)
    print(a)
長度('apple')