products = []
while True:
    name = input("請輸入商品名字:")
    if name == 'q':
        break
    price = input("請輸入商品價格:")
    products.append([name,price])
print(products)
for p in products:
    print(p[0],'的價格:',p[1])