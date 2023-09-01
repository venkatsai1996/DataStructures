

def reverseStringWordWise(string):
    
    #Your code goes here
    arr = string.split(' ')
    #print(arr)
    b = ''
    arr.reverse()
    for i in arr:
        b = b + i + ' '
    return b





string = input()
ans = reverseStringWordWise(string)
print(ans)
        
