import sys
import matplotlib.pyplot as plt

data_list = []
x_list = []
y_list = []
c_list = []

def phrase_input():
    for line in sys.stdin:
        data = line.strip().split(',')
        color_list = ['r', 'y', 'k', 'g', 'm']
        data[0] = int(data[0])
        data[1] = float(data[1])
        data[-1] = int(data[-1])
        x_list.append(data[0])
        y_list.append(data[1])
        c_list.append(color_list[data[-1] % 5])
        data_list.append(data)

def visualization(x_min = 0, x_max = 8000, y_min = 0, y_max = 30, cluster_num = 3):
    global data_list
    global x_list
    global y_list
    global c_list
    plt.xlim(x_max, x_min)
    plt.ylim(y_max, y_min)
    plt.title("Clustering Result")
    plt.scatter(x_list, y_list, c = c_list)
    plt.show()

if __name__ == '__main__':
    phrase_input()
    visualization(cluster_num = 3)
