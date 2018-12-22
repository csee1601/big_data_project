import sys

data_list = []
result_dict = {}
for line in sys.stdin:
    data = line.strip().split(',')
    data_list.append(data)

#print(data_list)

for item in data_list:
    prov = item[0]
    sales = item[1]
    if prov in result_dict.keys():
        result_dict[prov] += sales
    else:
        result_dict[prov] = sales

final_list = sorted(result_dict.items(), key=lambda item:item[1], reverse=True)
for item in final_list:
    print(item[0] + ',' + str(item[1]))
