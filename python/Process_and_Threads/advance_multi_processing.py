from concurrent.futures import ProcessPoolExecutor

import time

def square_number(number):
    time.sleep(2)
    return f'Sqaure numbers:{number * number}'

numbers = [1,2,3,4,5,6,7,8,9,10]

## this whole code below took about 20.00477 seconds 
# start_time= time.time()
# results =[]

# for number in numbers:
#     results.append(square_number(number))

# for result in results:
#     print(result)

# finished_time = time.time() - start_time
# print("Finished_time",finished_time)

########################################################
## ----------------now with process pool -------------------------------------------------------
## THIS WHOLE CODE TOOK ABOUT 8.293 SECONDS TO EXECUTE

start_time= time.time()

if __name__ =="__main__":
    start_time= time.time()
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number,numbers)

    for result in results:
        print(result)
    end_time = time.time() - start_time
    print("Finished time:",end_time)

    