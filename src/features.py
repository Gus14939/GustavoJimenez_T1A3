# Features and moks

# from alive_progress import alive_it
from alive_progress import alive_bar
from time import sleep

'''
items = [1,2,3,4,5,6,7,8,9,0]

for item in alive_it(items):   # <<-- wrapped items
    print(item)                # process each item
'''
'''
itemsX = [1,2,3,4,5,6,7,8,9,10]
items = []
for i in range(10):
    for j in itemsX:
        items.append(j)

def compute():
    with alive_bar(100) as bar:  # your expected total
        for item in items:        # the original loop
            print(item)xw
            sleep(0.01)           # your actual processing here
                                    # your actual processing here
            bar()                 # call `bar()` at the end


compute()
'''

def compute(TIME):
    with alive_bar(TIME) as bar:  # your expected total
        for i in range(TIME):     # the original loop
            # sleep(0.6)           # your actual processing here
            sleep(0.01)           # Fake for quick test
            bar()                 # call `bar()` at the end

# compute(100)


