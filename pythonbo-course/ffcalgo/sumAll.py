#https://www.freecodecamp.org/challenges/sum-all-numbers-in-a-range

def smallest(l):
    current = l[0]
    for n in l:
        if n < current:
            current = n
    return current

def biggest(l):
    current = l[0]
    for n in l:
        if n > current:
            current = n;
    return current;

# rather than using smallest and biggest 
# we scan through array twice we can reduce 
# computations by compairing first and last 
def sum(f, t):
    count = 0
    # range(start, stop) we want to include the last element
    for f in range(f,t+1):
        count += f

    return count

def sumAll(l):
    # first is bigger so we count down and sum all numbers
    if l[0] > l[1]:
        return sum(l[1],l[0])
    
    if l[0] < l[1]:
        return sum(l[0],l[1])

    if l[0] == l[1]:
        return l[0] + l[1]

print(sumAll([1,4]))
print(sumAll([4,1]))
print(sumAll([1,-2]))  
print(sumAll([-1,-1]))
#print(smallest([1,2,3,4,5,0]))
#print(biggest([1,2,3,4,100,0,-2]))