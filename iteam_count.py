import csv
import time
from functools import reduce
import os
# with open("",'rt',encoding='utf-8_sig') as f:
#     reder = csv.DictReader(f)
#

count = []
worry_list = []

filepath = 'C:/Users/ENeS/Desktop/datasets/Deduplication/Amazon/ValveIndex'
id_list = os.listdir(filepath)
print(id_list)
print(len(id_list))
id_count = 1
for id in id_list:
    try:
        #filename = 'C:/Users/Admi/Desktop/oculus/go/iteam_reviews/' + str(id) + '.csv'
        filename = 'C:/Users/ENeS/Desktop/datasets/Deduplication/Amazon/ValveIndex/'+id
        first = 0
        with open(filename, 'r', encoding='UTF-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    first += 1
        count.append(first-1)
        print('这个', id, '有', first-1)
    except:
        print('这个id没有评论', id)
        worry_list.append(id)
    id_count = id_count+1
print(id_count)
print(worry_list)
print(len(worry_list))
print(reduce(lambda x, y: x + y, count))
