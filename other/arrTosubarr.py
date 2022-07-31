list = [ 110,3,3,3,3,110,8,9,100]
n = '/n'
count = 0
for i in range(int(len(list)/3)):
    l = []
    for j in range(len(list)):
        if list[j] != n:
            if list[j] not in l:
                l.append(list[j])
                list[j] = n
        if len(l) == 3:
            count = count+1
            break;
    print(l)
print(count)
print(list)