import sys
import time

# def print_memory_usage():
#     data = []
#
#     for i in range(0, 128):
#         size_bytes = sys.getsizeof(data)
#         size_count = len(data)
#         print(f'Length {size_count:3d}, size {size_bytes:5d} bytes')
#         data.append(None)
#
#
# print_memory_usage()


# def print_time_consuming():
#     for i in range(1, 10000, 100):
#         data = []
#         start = time.time()
#         for j in range(i):
#             data.append(None)
#         spend = time.time() - start
#         average = spend/i * 1000*1000
#         print(f'Length {i:5d}, spend {average:0.8f} us per append')
#
# print_time_consuming()

# Efficiency
# Operation      - Time
# Len(data)      - O(1)
# data[j]        - O(1)
# data.count(el) - O(n)
# data.index(el) - O(k)
# value in data  - O(k)
# data == data   - O(k)
# data[i:j]      - O(j-i+1)
# data[i]=el     - O(1)
# data.append(el) - O(1)
# data.remove(el) - O(n)
# Удаление элементов из масиива в один проход
# def remove_from_array(array, el):
#     j = 0
#     array_len = len(array)
#     for i in range(array_len):
#         array[j] = array[i]
#         if array[i] != el:
#             j += 1
#
#     while len(array) > j:
#         array.pop()
#     return array
#
#
# print(remove_from_array([1, 2, 3, 4, 5, 4], 2))

def insert_sort(array):
    for i in range(1, len(array)):
        el = array[i]
        j = i
        while j > 0 and array[j-1] > el:
            array[j] = array[j-1]
            j -= 1
        array[j] = el
    return array


print(insert_sort([1, 3, 4, 5, -2]))

