from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f'Number :{number}'

numbers = [1,2,3,4,5,6,7,8,9,0,1,2,3,4]
################################################################
# t = time.time() 
# results = []
# for number in numbers:
#     results.append(print_number(number))

# for result in results:
#     print(result)

# finished_time = time.time() - t
# print("Time taken:",finished_time)
#########################################################
## All this code above took about 14 seconds
############################################################

#####this code below took only 5 seconds to execute
t = time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number,numbers)

for result in results:
    print(result)

finished_time = time.time() - t
print("finishded time:",finished_time)