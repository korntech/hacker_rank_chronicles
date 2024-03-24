def separateNumbers(s):
    if len(s) == 1 or s[0] == '0':
        print("NO")
        return

    s_len = len(s)
    max_digits = s_len // 2 
    first = ''
    found = False
    bumped = False
    for i in range(1, max_digits+1):
        c = i
        sliceStart = 0 
        sliceEnd = i

        v2_sliceStart = sliceEnd
        v2_sliceEnd = v2_sliceStart + v2_sliceStart
        if found:
            break
        while v2_sliceEnd <= len(s):
            first_val = s[sliceStart:sliceEnd]
            sec_val = s[v2_sliceStart:v2_sliceEnd]

            if s[v2_sliceEnd:] and not len(str(int(first_val) + 1)) > len(str(first_val)):
                if int(sec_val) > int(s[v2_sliceEnd:]):
                    found = False
                    break

            if not first:
                first = first_val

            if len(str(int(first_val) + 1)) > len(str(first_val)):
                bumped = True
                v2_sliceEnd += 1
                sec_val = s[v2_sliceStart:v2_sliceEnd]
                c = len(s[v2_sliceStart:v2_sliceEnd])
                sliceStart += c -1
                sliceEnd += c
                v2_sliceStart = sliceEnd
                v2_sliceEnd += c
            else:
                sliceStart += c 
                sliceEnd += c
                v2_sliceStart = sliceEnd
                v2_sliceEnd += c

            if int(sec_val) - int(first_val) != 1 or sec_val[0] == '0' or first_val[0] == '0':
                found = False
                first = ''
                break
            else:
                found = True

    if found:
        print(f"YES {first}")
    else:
        print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()
        separateNumbers(s)
