info = {
    '小明': {
        'fruits': ['苹果', '草莓', '香蕉'],
        'money': 89
    },
    '小刚': {
        'fruits': ['葡萄', '橘子', '樱桃'],
        'money': 87
    }
}

ming_dic = info.get('小明')
gang_dic = info.get('小刚')
print("小明：")
print("水果", ming_dic["fruits"], "花了", ming_dic["money"])
print("小gang：")
print("水果", gang_dic["fruits"], "花了", gang_dic["money"])