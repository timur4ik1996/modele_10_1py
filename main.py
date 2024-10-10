import time
from time import sleep
from threading import Thread
from datetime import datetime

time_start = datetime.now()


def write_words(word_count, file_name):
    file = open(file_name, 'w')
    for count in range(1, word_count + 1):
        file.write(f"Какое то слово №{count}"'\n')
        sleep(0.1)

    return f'Завершилась запись в файл {file_name}'


print(write_words(10, "example.txt"))
print(write_words(20, "example2.txt"))
print(write_words(200, "example3.txt"))
print(write_words(100, "example4.txt"))
time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа потоков {time_res}')
one = Thread(target=write_words, args=(10, "exmple5.txt"))
second = Thread(target=write_words, args=(20, "example6.txt"))
free = Thread(target=write_words, args=(200, "example7.txt"))
forr = Thread(target=write_words, args=(100, "example8.txt"))
one.start()
second.start()
free.start()
forr.start()

one.join()
print("Завершилась запись в файл exmple5.txt")
second.join()
print("Завершилась запись в файл exmple6.txt")
free.join()
print("Завершилась запись в файл exmple7.txt")
forr.join()
print("Завершилась запись в файл exmple7.txt")
time_finish = datetime.now()
time_resss = time_finish - time_end
print(f'Работа потоков {time_resss}')
