import os   #operation system

#讀取檔案
def read_file(filename):
    products = []
    with open(filename,'r',encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue   #下面不執行，換下一回
            name, price = line.strip().split(',')
            products.append([name,price])
    return products
      
#增加資料
def add_file(products):
    while True:
        name = input("請輸入商品名字:")
        if name == 'q':
            break
        price = input("請輸入商品價格:")
        products.append([name,price])
    print(products)
    return products

#印出檔案
def print_file(products):
    for p in products:
        print(p[0],'的價格:',p[1])

#寫入檔案
def write_file(filename, products):
    with open(filename,'w',encoding = 'utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n') #逗點區隔是為了寫入csv檔
                                              #換行也是必要的

#主程式
def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('found it !!!')
        products = read_file(filename)
    else:
        print('cant found it.... ')
    products = add_file(products)
    print_file(products)
    write_file('products.csv', products) 


main()