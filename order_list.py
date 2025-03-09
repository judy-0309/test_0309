order_list = ['礦泉水', '蘋果', '衛生紙']
del order_list[2]
order_list.append('雞肉')
print(order_list)
print(order_list[1])
print("-" * 50)

score_list = {'小明': 70, '小華' : 60, '小王' : 80}
print(score_list)
print(score_list["小華"])
score_list['小美'] = 90
print(score_list)
print(len(score_list))
print(type(len(score_list))) # type查資料型態
print(type("成績單共有"))
# a = "成績單共有"
# print(int(a))
print("成績單共有" + str(len(score_list)) + "位學生")
print("-" * 50)

