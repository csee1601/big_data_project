import sys

data_list = []

for line in sys.stdin:
    data = line.strip().split(',')
    data[0] = int(data[0])
    data[1] = float(data[1])
    data[-1] = int(data[-1])
    data_list.append(data)

if __name__ == '__main__':
    print(data_list)