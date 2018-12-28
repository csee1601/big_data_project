import sys
import random

data_list = []
iter_time = 1
centroids = []

def phrase_input():
    for line in sys.stdin:
        data = line.strip().split(',')
        data.append(0)
        data[1] = int(data[1])
        data[2] = float(data[2])
        data_list.append(data)

def K_means(cluster_num = 3, iteration_time = 10):
    global iter_time
    global data_list
    global centroids
    random_centroids_number = [0] * cluster_num
    if (len(data_list) < 10) or (len(data_list) < cluster_num):
        print("Bad data!")
        return
    if cluster_num == 1:
        return
    if iter_time == 1:
        for i in range(0, cluster_num):
            temp = random.randint(0, len(data_list) - 1)
            while temp in centroids:
                temp = random.randint(0, len(data_list - 1))
            random_centroids_number[i] = temp
            centroids.append([data_list[temp][1], data_list[temp][2]])
        # print(centroids)
        tag_items(cluster_num)
        iter_time = iter_time + 1
        return K_means(cluster_num, iteration_time)

    elif iter_time == iteration_time:
        return
    else:
        calculate_centroids(cluster_num)
        # print(centroids)
        tag_items(cluster_num)
        iter_time = iter_time + 1
        return K_means(cluster_num, iteration_time)


def tag_items(cluster_num = 3):
    global data_list
    global centroids
    distance_square = [0] * cluster_num
    for item in data_list:
        for i in range(cluster_num):
            distance_square[i] = (abs(item[1] - centroids[i][0]) ** 2) + (abs(item[2] - centroids[i][1]) ** 2)
        min = distance_square[0]
        min_pos = 0
        for i in range(cluster_num):
            if distance_square[i] < min:
                min_pos = i
                min = distance_square[i]
        item[-1] = min_pos

def calculate_centroids(cluster_num = 3):
    global data_list
    global centroids
    sum_x = [0] * cluster_num
    sum_y = [0] * cluster_num
    points_num = [0] * cluster_num
    for item in data_list:
        sum_x[item[-1]] += item[1]
        sum_y[item[-1]] += item[2]
        points_num[item[-1]] += 1
    for i in range(cluster_num):
        centroids[i][0] = sum_x[i] / points_num[i]
        centroids[i][1] = sum_y[i] / points_num[i]

def print_result():
    for item in data_list:
        print(str(item[0]) + "," + str(item[1]) + "," + str(item[2]) + "," + str(item[-1]))
    return

if __name__ == '__main__':
    phrase_input()
    K_means(3,10)
    print_result()
