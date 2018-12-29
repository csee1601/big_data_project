import sys

data_list = []

def getSecond(item):
   return item[1]

def phrase_input():
    for line in sys.stdin:
        data = line.strip().split(',')
        data_list.append(data)

def sort_all():
    data_list.sort(key = getSecond, reverse=True)


if __name__ == '__main__':
    phrase_input()
    sort_all()
    for item in data_list:
        print(item[0] + "," + item[1])
