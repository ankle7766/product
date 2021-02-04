import os   #operation system


products = []
#檢查檔案室存在
if os.path.isfile('product.csv'):
    print('found it !!!')
    # 讀取檔案
    with open('product.csv','r',encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue   #下面不執行，換下一回
            name, price = line.strip().split(',')
            products.append([name,price])

    print(products)
else:
    print('cant found it.... ')

while True:
    name = input("請輸入商品名字:")
    if name == 'q':
        break
    price = input("請輸入商品價格:")
    products.append([name,price])
print(products)
for p in products:
    print(p[0],'的價格:',p[1])

with open('product.csv','w',encoding = 'utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n') #逗點區隔是為了寫入csv檔
                                          #換行也是必要的