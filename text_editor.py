Q = int(input())
S = "" 
history = []
ops = []

while True:
    op = input()

    if not op:
        break
    else:
        ops.append(op)

if Q > len(ops):
    quotient, remainder = divmod(Q, len(ops))
    ops = ops * quotient
    rem = ops[:remainder]
    ops.extend(rem)

for op in ops:
    op = op.split()
    if op[0] == '3':
        print(S[int(op[1])-1])
    elif op[0] == '4':
        history.pop()
        S = history[-1]
    elif op[0] == '1':
        S += op[1]
    else:
        S = S[:-int(op[1])]

    if op[0] not in ('4', '3'):
        history.append(S)




