"""
bubbleSort.py
버블 정렬 프로그램
버블 정렬에 대한 이해를 도와줄 사이트
        https://gmlwjd9405.github.io/2018/05/06/algorithm-bubble-sort.html

10,000개의 랜덤 정수를 정렬하는데 약 9~10초 소요
"""
import time
import random

def bubbleSort(list_):
    for trial in range(len(list_)):
        for idx in range(len(list_) - trial - 1):
            if list_[idx] > list_[idx + 1] :
                list_[idx], list_[idx+1] = list_[idx+1], list_[idx]
    return list_

if __name__ == "__main__":
    target = []
    for i in range(10000):
        target.append(random.randrange(10000))
    
    start = time.time()
    sorted = bubbleSort(target)
    end = time.time()
    duration = end - start

    print(sorted[-3:])
    print(f"Time taken during sort: {duration}sec.")

