#lifo queue

# remove element from end of list

queue = []

def push(element,*args):
    queue.append(element)
    for arg in args:
        queue.append(arg)

def pop():
    del queue[len(queue)-1]

push(1,2,3,4,5,6,7,8,10)
print(queue)
pop()
print(queue)
pop()
print(queue)
pop()