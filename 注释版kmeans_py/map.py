import sys

data_list = []

'''
将数据存放至列表data_list
列表的每一项是包含有省份、年份、销售额、销售量等元素的子列表
同时子列表中还包含一个标志元素，当标志元素为“1”时表示数据的年份为“2016”，反之标志元素为“0”
'''
def phrase_input():
    for line in sys.stdin:
        data = line.strip().split(',')  #读取CSV文件中每一列数据至列表
        if data[1] != '2016':
            #当年份不为“2016”，标志元素置0
            data.append(0)
        else:
            #否则标志元素置1
            data.append(1)
        data_list.append(data)  #子列表加入列表中

'''
输入列表中标志元素为1的元素项
reducer只接收标志元素为1的元素项
'''       
def output_result():
    for item in data_list:
        if item[-1] == 1:
            #标志元素为1则输出
            print(item[0] + "," + item[2] + "," + item[3])


if __name__ == '__main__':
    phrase_input()
    output_result()