import sys
import time
import threading

data_list = []
result_dict = {}
thread_num = 8
threadLock = threading.Lock()
cleanThreads = []

def phrase_input():
    for line in sys.stdin:
        data = line.strip().split(',')
        data_list.append(data)

class cleanData(threading.Thread):
    def __init__(self, threadID, name, d_list):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.d_list = d_list

    def run(self):
        for item in self.d_list:
            if item[1] == '2017':
                prov = item[0]
                sales = float(item[2]) * float(item[3])
                threadLock.acquire()
                if prov in result_dict.keys():
                    result_dict[prov] += sales
                else:
                    result_dict[prov] = sales
                threadLock.release()

def print_dict():
    for item in result_dict:
        print(item + "," + str(round(result_dict[item], 2)))
    return

if __name__ == '__main__':
    time_start = time.time()
    phrase_input()
    groups = int((len(data_list) + 5) / 8)

    for i in range(0, 8):
        if (((i+1)*groups) > len(data_list)):
            threadi = cleanData(i, "thread", data_list[i*groups : len(data_list)])
        else:
            threadi = cleanData(i, "thread", data_list[i*groups : (i+1)*groups])
        cleanThreads.append(threadi)

    for th in cleanThreads:
        th.start()
    for th in cleanThreads:
        th.join()

    final_list = sorted(result_dict.items(), key=lambda item: item[1], reverse=True)
    for item in final_list:
        print(item[0] + ',' + str(round(item[1], 2)))

    time_end = time.time()
    print("Totally cost {0}s".format(round(time_end-time_start,5)))

