import sys
import random

data_list = []  #数据列表
iter_time = 1   #总递归次数
centroids = []  #


'''
读取mapper筛选后输出的数据至data_list
列表的每一项是包含有省份、年份、销售额、销售量等元素的子列表
同时子列表中还包含一个标志元素，表示所属簇的中心点编号
'''
def phrase_input():
    for line in sys.stdin:
        data = line.strip().split(',')
        data.append(0)
        data[1] = int(data[1])
        data[2] = float(data[2])
        data_list.append(data)


'''
K-means算法
输入为data_list

'''
def K_means(cluster_num = 3, iteration_time = 10):
    global iter_time
    global data_list
    global centroids
    random_centroids_number = [0] * cluster_num
    if (len(data_list) < 10) or (len(data_list) < cluster_num):
        #数据量太小或数据量小于期望簇数，中止本次迭代
        print("Bad data!")
        return
    if cluster_num == 1:
        #期望簇数为1，中止本次迭代
        return
    if iter_time == 1:
        #第一次迭代需要随机选取数据点作为簇的形心
        for i in range(0, cluster_num):
            temp = random.randint(0, len(data_list) - 1)
            while temp in centroids:
                #随机选取的形心必须互不相同
                temp = random.randint(0, len(data_list - 1))
            random_centroids_number[i] = temp   #形心编号
            centroids.append([data_list[temp][1], data_list[temp][2]])  #形心在二维平面上的坐标
        tag_items(cluster_num)  #按照选取的形心进行聚类
        iter_time = iter_time + 1
        return K_means(cluster_num, iteration_time)

    elif iter_time == iteration_time:
        #达到最大迭代次数
        return
    else:
        calculate_centroids(cluster_num)    #计算新形心
        tag_items(cluster_num)  #从新把数据划分到新形心代表的各个簇
        iter_time = iter_time + 1   #迭代次数加1
        return K_means(cluster_num, iteration_time) #递归进行迭代

'''
计算所有数据距离最近的簇的中心点
记录每个数据距离最近的簇的中心点的编号和坐标
'''
def tag_items(cluster_num = 3):
    global data_list
    global centroids
    distance_square = [0] * cluster_num
    for item in data_list:
        for i in range(cluster_num):
            #计算到每个形心点之间的欧氏距离
            distance_square[i] = (abs(item[1] - centroids[i][0]) ** 2) + (abs(item[2] - centroids[i][1]) ** 2)
        min = distance_square[0]
        min_pos = 0
        for i in range(cluster_num):
            #选取距离最小的形心点，记录编号与坐标
            if distance_square[i] < min:
                min_pos = i
                min = distance_square[i]
        #数据子列表的最后一项标志所述簇的中心点编号
        item[-1] = min_pos



'''
计算新的簇的中心点
更新中心点标号列表与坐标列表
'''
def calculate_centroids(cluster_num = 3):
    global data_list
    global centroids
    sum_x = [0] * cluster_num
    sum_y = [0] * cluster_num
    points_num = [0] * cluster_num
    for item in data_list:
        #计算一个簇中所有元素的x，y的坐标之和
        sum_x[item[-1]] += item[1]
        sum_y[item[-1]] += item[2]
        points_num[item[-1]] += 1
    for i in range(cluster_num):
        #计算一个簇中所有元素的x，y的坐标平均值，即为新的形心坐标
        centroids[i][0] = sum_x[i] / points_num[i]
        centroids[i][1] = sum_y[i] / points_num[i]


'''
输出K-means得出的聚类结果
'''
def print_result():
    for item in data_list:
        print(str(item[0]) + "," + str(item[1]) + "," + str(item[2]) + "," + str(item[-1]))
    return


if __name__ == '__main__':
    phrase_input()
    K_means(3,10)
    print_result()
