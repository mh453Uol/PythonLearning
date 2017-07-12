# fifo queue implementation

# 1,2,3,4,5,
queue = []

def get_queue():
    return queue

def push(element):
    queue.append(element)

def pop():
    shift_index = 1

    while shift_index < get_queue_size(queue):
            queue[shift_index-1] = queue[shift_index]
            shift_index += 1
    del queue[-1]

def get_queue_size(lists:[]):
    return len(lists)

push(1)
push(2)
print(queue)
push(3)
print(queue)
push(4)
print(queue)
push(5)
print(queue)
pop()
print(queue)
pop()
print(queue)