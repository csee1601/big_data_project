import sys

data_list = []
result_list = {}

def phrase_input_and_output():
    for line in sys.stdin:
        data = line.strip().split(',')
        data_list.append(data)

    for item in data_list:
        print(item[0] + "," + item[2])

if __name__ == '__main__':
    phrase_input_and_output()

