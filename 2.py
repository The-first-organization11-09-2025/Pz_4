import time
import logging

logging.basicConfig(level=logging.INFO, filename="PZ_4.log", filemode="w", format="%(asctime)s %(levelname)s %(message)s", encoding='utf-8')
def iter_fibonachi (n):
    list_fib = [0] * (n+1)
    list_fib[0] = 0
    list_fib[1] = 1
    for i in range(2, n+1):
        list_fib[i] = list_fib[i-2] + list_fib[i-1]
    return list_fib[n]
def rec_fibonachi(n):
    if n <= 1:
        return n
    return rec_fibonachi(n-1) + rec_fibonachi(n-2)

if __name__ == "__main__":
    n = 50

    start_time = time.time()
    print(iter_fibonachi(n))
    end_time = time.time()
    execution_time = end_time - start_time
    logging.info(f"Время нахождения 50-го эллемента Фибоначчи с помощью итеративной функции: {execution_time:.6f} секунд")

    start_time = time.time()
    print(rec_fibonachi(n))
    end_time = time.time()
    execution_time = end_time - start_time
    logging.info(f"Время нахождения 50-го эллемента Фибоначчи с помощью рукурсивной функции: {execution_time:.6f} секунд")
