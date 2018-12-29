import sys
import time

data_list = []
result_dict = {}

def add_and_sort():
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

    final_list = sorted(result_dict.items(), key=lambda item:item[1], reverse=True)
    for item in final_list:
        print(item[0] + ',' + str(round(item[1],2)))

if __name__ == '__main__':
    time_start = time.time()
    add_and_sort()
    time_end = time.time()
    print("Totally cost {0}s".format(round(time_end-time_start,5)))
