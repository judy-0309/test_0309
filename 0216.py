'''
a = 2
b = 3
print("加法", a + b)
print("減法", a - b)
print("乘法", a * b)
print("整數除法", a // b)
print("餘數", a % b)
print("-" * 50)

storename = '魚初見'
message = 'Welcome to ' + storename + '\n' + 'This is a Japanese resturant.'
print(storename + "\n" + message)
print("-" * 50)

voc = storename[2]
print(voc)
print("-" * 50)

food_list = ['Apple', 'Banana', 'Guava']
print(food_list)
food_list.append('Strawberry')
print(food_list)
print(food_list[0:2])
print("-" * 50)

food_menu = {'Apple': 25, 'Banana': 35, 'Guava': 45, 'Strawberry': 55}
print(food_menu["Apple"])
print("-" * 50)

food_menu = {'Apple': 25, 'Banana': 35, 'Guava': 45, 'Strawberry': 55}
food_menu['Banana'] = 26
print(food_menu)
print("-" * 50)

meal = input('請輸入餐點內容:')
print(meal)
print("-" * 50)

name = input('請輸入姓名:')
age = input('請輸入年齡:')
occ = input('請輸入職業:')
print("你好，我是" + name + "，我今年" + age + "歲，職業是" + occ)
print("五年後我是" + str(int(age) + 5) + "歲")
print("-" * 50)



nametag = {}
nametag['name'] = input('請輸入姓名:')
nametag['age'] = input('請輸入年齡:')
print("名片資料：", nametag)
print("-" * 50)

shopping_list = []
shopping_list.append(input('購物清單:'))
shopping_list.append(input('購物清單:'))
shopping_list.append(input('購物清單:'))
print(shopping_list)
print("購物清單有" + str(len(shopping_list)) + "幾個樣品要買!")
print("-" * 50)
'''

fruit_list = {'蘋果': 30, '草莓': 26, '鳳梨':50}
shopping_list = []
shopping_list = input('購物清單:')
print(shopping_list)
total_price = fruit_list[shopping_list]
print("你購買的水果是:" + shopping_list + "，總共的價格為" + str(total_price) + "元")
print("今天水果攤周年慶打九折" + "你購買的水果是:" + shopping_list + "，原本是:"
       + str(total_price) + "，打折後的價格為" + str(round(total_price * 0.9, 2)) + "元")