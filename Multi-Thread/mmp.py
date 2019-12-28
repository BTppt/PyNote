# process and thread
import threading
import time


def SubTask(i0):
    print('this is thread %d: start' % i0)
    time.sleep(5)
    print('this is thread %d: end' % i0)


# create thread using thread class
T = []
for num in range(0, 4):
    T.append(threading.Thread(target=SubTask, args=(num,)))
for num in range(0, len(T)):
    T[num].start()
# join
for num in range(0, len(T)):
    T[num].join()

print('END')

# synchronization lock
