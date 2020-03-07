# process and thread
import threading
import time


def actions(i0):
    print('this is thread %d: start' % i0)
    time.sleep(5)
    print('this is thread %d: end' % i0)


# create thread using thread class
T = []
for num in range(0, 4):
    T.append(threading.Thread(target=actions, args=(num,)))
for num in range(0, len(T)):
    T[num].start()
# join
for num in range(0, len(T)):
    T[num].join()

print('END')

# local data
md = threading.local()
md.x = 0
md.y = 0


def modify(x, y):
    md.x = x
    md.y = y
    print(md.x, md.y)


t0 = threading.Thread(target=modify, args=(1, 1))
t1 = threading.Thread(target=modify, args=(2, 2))
t0.start()
t1.start()
t0.join()
t1.join()
print(md.x, md.y)

# synchronization: Lock & RLock
l0 = threading.Lock()


def activity1(num):
    l0.acquire()
    print('thread {} {}'.format(num, 1))
    time.sleep(5)
    print('thread {} {}'.format(num, 2))
    l0.release()


def activity2(num):
    print('thread {} {}'.format(num, 1))
    time.sleep(5)
    print('thread {} {}'.format(num, 2))


TT = []
for k in range(0, 6):
    TT.append(threading.Thread(target=activity1, args=(k,)))
for k in range(0, 6):
    TT[k].start()

