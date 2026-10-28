import multiprocessing

import time

def sqaure_numbers():
    for i in range(5):
        time.sleep(1)
        print(f'Square:{i*i}')

def cube_numbers():
    for i in range(5):
        time.sleep(1)
        print(f'Cube:{i*i*i}')

# t = time.time()
# sqaure_numbers()
# cube_numbers()
# finished_time = time.time() -t
# print(finished_time)

if __name__ == "__main__":
#create process
    p1 = multiprocessing.Process(target=sqaure_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)
#start the process
    t=time.time()
    p1.start()
    p2.start()
#wait for the process to end 
    p1.join()
    p1.join()
    finished_time = time.time() - t
    print(finished_time)
    