

#Threading is a technique in programing can run multiple operations (tasks) concurrently (at the same time using threads)

#  A thread is the smallest unit of a program that can be ececuted independently.
#  python has a built-in modile called threading to work with threads.
#  A thread shares the same space as other threads in the sane process.
#  multithreading is the process of running  multiple threads at the same time within the same program.





from ntpath import join
import threading
import time
def squres(numbers):
    print(f"square of numbers:")
    for i in numbers:
        time.sleep(0.2)
        print(f"square: {i**2}")
def cubes(numbers):
    print(f"cubes of numbers:")
    for i in numbers:
        time.sleep(0.2)
        print(f"cubes: {i**3}")
initial_time=time.time()
list_1=[1,2,3,4,5]
t1=threading.Thread(target=squres,args=(list_1,))#args , take tuple as input so we give (list_1,) comma is important
t2=threading.Thread(target=cubes,args=(list_1,))
t1.start()
t2.start()
t1.join()
t2.join()
print(f"time taken{time.time()-initial_time}")


















