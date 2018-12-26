import sys

data_list = []

def phrase_input():
    for line in sys.stdin:
        data = line.strip().split(',')
        if data[1] != '2016':
            data.append(0)
        else:
            data.append(1)
        data_list.append(data)
def output_result():
    for item in data_list:
        if item[-1] == 1:
            print(item[0] + "," + item[2] + "," + item[3])

if __name__ == '__main__':
    phrase_input()
    output_result()