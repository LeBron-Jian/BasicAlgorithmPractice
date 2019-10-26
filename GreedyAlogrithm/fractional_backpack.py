#_*_coding:utf-8_*_

# 每个商品元组表示（价格，重量）
goods = [(60, 10), (100, 20), (120, 30)]
# 我们需要对商品首先进行排序，当然这里是排好序的
goods.sort(key=lambda x: x[0]/x[1], reverse=True)

# w 表示背包的容量
def fractional_backpack(goods, w):
    # m 表示每个商品拿走多少个
    total_v = 0
    m = [0 for _ in range(len(goods))]
    for i, (prize, weight) in enumerate(goods):
        if w >= weight:
            m[i] = 1
            total_v += prize
            w -= weight
        # m[i] = 1 if w>= weight else weight / w
        else:
            m[i] = w / weight
            total_v += m[i]*prize
            w = 0
            break
    return m, total_v

res1, res2 = fractional_backpack(goods, 50)
print(res1, res2)  # [1, 1, 0.6666666666666666]