def check_if_stack_decrease(stack):
    
  
    new_pile = []

    while len(stack) > 0:
        if stack[0] > stack[-1]:
            new_pile.append(stack[0])
            del stack[0]
        else:
            new_pile.append(stack[-1])
            del stack[-1]

    
    for i in range(len(new_pile)-1):
        if new_pile[i] < new_pile[i+1]:
            return "No"
        
    return "Yes"

    

for i in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    print(check_if_stack_decrease(arr))
