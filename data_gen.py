# -*- coding: UTF-8 -*-
import random

directory_name = "./"
file_name = "data.csv"
data_lines = 1000
prov = ['beijing','shanghai','tianjin','chongqing','liaoning','heilongjiang','jilin','hebei',
        'henan','shanxi','shandong','hubei','hunan','jiangsu','zhejiang','guangdong','guangxi',
        'fujian','hainan','sichuan']

def generate_data(num):
    prov_num = len(prov)
    fo = open(directory_name + file_name, "w")
    print("write to " + directory_name + file_name)
    for i in range(0, data_lines):
        index = random.randint(0,prov_num - 1)
        item_prov = prov[index]
        item_year = random.randint(2016,2018)
        item_sales = random.randint(1000,3000)
        item_price = round(random.uniform(5,10) ,2)
        fo.writelines(str(item_prov) + ',' + str(item_year) + ',' + str(item_sales) + ',' + str(item_price) + "\n")
    fo.close()

if __name__ == '__main__':
    generate_data(data_lines)
