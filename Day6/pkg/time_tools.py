from time import sleep,time

TOTAL_ITERATION_TIME = 0
TOTAL_ITERATIONS = 0

def timer_reset():
    global TOTAL_ITERATION_TIME,TOTAL_ITERATIONS
    TOTAL_ITERATION_TIME = 0
    TOTAL_ITERATIONS = 0

def myiterator(n):
    num = 1
    global TOTAL_ITERATION_TIME,TOTAL_ITERATIONS
    while num<n+1:
        t0 = time()
        yield num
        num += 1
        TOTAL_ITERATION_TIME += time()-t0
        TOTAL_ITERATIONS += 1

def show_timer():
    global TOTAL_ITERATION_TIME,TOTAL_ITERATIONS
    print('each iteration takes:',TOTAL_ITERATION_TIME/TOTAL_ITERATIONS)
