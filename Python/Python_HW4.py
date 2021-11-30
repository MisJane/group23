# from https://docs.google.com/document/d/12F9M_ple__cxDtHUYA7szHL-UkqgORNCrt1fE3YL2oI/
# made small changes for the convenience of verification

# While
import time

count = 0
range_count = 10
for_count = 0
rub = True

while True:
    print('Hello, Cycle')
    time.sleep(.300)
    break

while True:
    print('Step =', count)
    count += 1
    time.sleep(.300)
    break

while count < range_count:
    print('Step next =', count)
    count += 1
    time.sleep(.300)

while count < 15:
    print('Step again =', count)
    count += 1
    time.sleep(.500)
    if count == range_count + 1:
        print('STOP', count)

# For
for item in range(for_count, range_count):
    print('step = ', item)

for item in range(0, 30):
    print('step = ', item)
    if item == 5:
        print('item = ', item)
    elif item == 10:
        print('item = ', item)
    elif item < 4:
        print('item < ', item)
    elif item >= 27:
        print('item >= ', item)

for item in range(0, range_count + 1):
    print('step = ', item)
    if item == 7:
        inner_count = 0
        print('--inner_count = ', inner_count)
        for inner_item in range(0, item):
            print('-------- Inner_Step = ', inner_item)
            if inner_item == 5:
                inner_count = inner_item
        print('-- inner_count = ', inner_count)

for item in range(0, 20):
    print('step = ', item)
    if item > 7 and item < 12:
        print('if_item = ', item)
        continue
print('End_iteration = ', item)
