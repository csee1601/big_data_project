import sys

data_list = []
result_dict = {}
for line in sys.stdin:
    data = line.strip().split(',')
    data_list.append(data)

for item in data_list:
    if item[1] == '2017':
        prov = item[0]
        sales = float(item[2]) * float(item[3])
        if prov in result_dict.keys():
            result_dict[prov] += sales
        else:
            result_dict[prov] = sales

for item in result_dict:
    print(item + "," + str(round(result_dict[item],2)))
