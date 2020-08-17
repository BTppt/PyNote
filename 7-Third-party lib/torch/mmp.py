import torch.multiprocessing
import time
import torch


def main_process(rank, event, q):
    print('process: ', rank)
    q.put(torch.zeros(1000, 1000))
    event.wait()
    print('end ; ', rank)


if __name__ == '__main__':
    qq = torch.multiprocessing.Queue()
    e = torch.multiprocessing.Event()
    for rank in [0, 1, 2, 3]:
        torch.multiprocessing.Process(target=main_process, args=(rank, e, qq)).start()
    n = 0
    while True:
        y = qq.get()
        n = n + 1
        print(y[0, 0])
        if n == 4:
            break
    e.set()
    print(y[0, 0])
