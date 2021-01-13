import cmath
import time
import os
import threading
import queue
from multiprocessing import Process
import string
import logging
import json
import csv


'''
a =9
list1 = [1,2,3,10]


if (a in list1):
    print('a is in list')
elif (a not in list1):
    print('a is not in list')

else:
    print("end")


numbers = [1,2,3,4,5,6]
even =[]
odd = []

while len(numbers)>0:
    number = numbers.pop()
    if ((number % 2) ==0):
        even.append(number)
    else:
        break

print(even)
print(odd)

fruits = ['app', 'orange', 'kiwi']

for fruit in fruits:
    print(fruit*2)

for index in range(len(fruits)):
    print('this fruit is%s and in th enumber of %d'% ((fruits[index]), 1))

str='zhang sicai is the best'
print(str.split(' ', len(str)))
print(str.upper())


tub=(1)
print(tub)

dict = {'name': 'sicai', 'age': 30}
for value in dict.values():
    print(value)
for k,v in dict.items():
    print(k,v)

isinstance(dict,Iterable)


fo = open('/Users/zhangsicai/Desktop/bb.txt', 'r+')
str=fo.read()
print(str)
fo.close()

path = '/Users/zhangsicai/Desktop/aa/'
files = os.listdir(path)
print(files)
num=0
for file in files:
    oldname = path + file
    print(oldname)
    newname = oldname + "dd"

    os.rename(oldname, newname)
    num+=1



class Employee:
    empcount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empcount += 1

    def displayEmploy (self):
        print(self.name, self.salary)

    def displayCount(self):
        print(Employee.empcount)

    def __del__(self):
        print('deling')

Emp1 = Employee ('sicai', 8000)
Emp2 = Employee ('linlin', 7000)

print(Employee.empcount)
Emp1.displayEmploy()
Emp1.displayCount()

del Emp1

class Employee2 (Employee):
    def childMethod(self):
        print('this is child method')

Emp3 = Employee2 ('vivi', 9000)
Emp3.childMethod()
Emp3.displayEmploy()



//Thread

exitFlag = 0


class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print('starting' + self.name)

        lock.acquire() #lock
        print_time(self.name, self.counter, 5)
        print('exiting'+ self.name)
        lock.release()


def print_time(threadName, delay, counter):
    while counter:

        time.sleep(delay)
        print(threadName, time.ctime(time.time()))
        counter -= 1


lock = threading.Lock() # get lock

thread1 = myThread(1, '1stThread', 1)
thread2 = myThread(2, '2stThread', 1)

thread1.start()
thread2.start()

threadList =[]
threadList.append(thread1)
threadList.append(thread2)

for t in threadList:
    t.join()

print('exit main thread')


#Queue
q=queue.LifoQueue()

for i in range(5):
    q.put(i)

while not q.empty():
    print (q.get())


#THREAD
def loopthread():
    print('thread %s is running' % threading.current_thread().name)
    n=0
    while n<5:
        n+=1
        print('thread %s>>> %d' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s end' % threading.current_thread().name)

print('thread %s is running ' % threading.current_thread().name)
t=threading.Thread(target=loopthread, name='this is loop thread')
t.start()
t.join()
print('thread %s end' % threading.current_thread().name)

multi process
def run_proc(name):
    print('now print child process %s %s'% (name, os.getpid()))

print('parent process start %s' % os.getpid())

p = Process(target=run_proc, args=('aa',))
print('child process now start')
p.start()
p.join()
print('child process end')

#try exception
try:
    fh = open("testfile", 'r')
    fh.write('write content')
except IOError:
    print('write error')
else:
    print('write success')

finally:
    print('end')

s1=[1,1,2,3,4,4,5]
s= tuple(s1)
print(s[:4:3])
print(s[-3:])

L1=list(range((10)))
L2=list(range(11,20))

L3=[a+b for a in L1 for b in L2 if (a+b)%2 == 0]
print(L3)

L4=[x if x%2==0 else -x for x in range(10)]
print(L4)

def digui(n):
    if n==1:
        return 1
    return n*digui(n-1)

print(digui(10))
if (isinstance(1, int)):
    print('good')

##shell command

fn = os.popen('ls -l')
files=fn.read()
print(files)


sh.pwd()

sh.touch('file.txt')
sh.whoami()
sh.echo('great')

##json

json_filename = '/Users/zhangsicai/Desktop/jsn.json'
txt_filename = '/Users/zhangsicai/Desktop/txt.txt'
file = open(txt_filename, 'w+')

with open(json_filename, 'r+') as f:
    pop_datas = json.load(f)

    print(pop_datas)
    for pop_data in pop_datas:
        print(pop_data)

        label_idtxt = pop_data['label_id']
        image_idtxt = pop_data['image_id']

        tempstring = str(label_idtxt) + ':' + str(image_idtxt)

        print(tempstring)
        file.write(tempstring + '\n')

    file.close()

#dump

temp_dict = {
    'name': 'sicai',
    'age': 12
}

with open('/Users/zhangsicai/Desktop/jsn1.json', "w+") as fdata:
    json.dump(temp_dict, fdata)

print(temp_dict)

#lambda
sum = lambda a, b: a+b
print(sum(1,2))

#csv
row = ['4', 'mm', '19']
with open('/Users/zhangsicai/Desktop/csv.csv', 'a+') as f:
    
    reader = csv.DictWriter(f)
    for row in reader:  
        print(row['sage'])
    

    csv_writer = csv.writer(f,'excel')
    csv_writer.writerow(row)

outputfile ='/Users/zhangsicai/Desktop/outputfile.txt'
with open(outputfile, 'w+') as f:
    f.write(str(s))
'''

### __slots__

class Student(object):
   # __slots__ = ('name', 'age')
   score = '90'

   def set_name(self, name):
       self.name = name

   def get_name(self):
       print(self.name)
       return self.name

s1 = Student()
s1.set_name('vivi')
s1.get_name()
s1.score = 20
print(s1.score)


