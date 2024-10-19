# YOUR CODE HERE
def sumation(numm, operation) :
    lst1 = []
    lst2 = []
    cal_list = []
    for i in range(numm) :
        a = int(input())
        lst1.append(a)

    for l in range(numm) :
        b = int(input())
        lst2.append(b)

    for c in range(numm) :
        c = lst1[c] + lst2[c]
        cal_list.append(c)

    print(cal_list)

    updated_list = operation(cal_list)

    return updated_list

# print(result)

def find_min_max(updated_list) :

    many = min(updated_list)
    much = max(updated_list)

    return many , much


num = int(input())
# result1 = sumation(num)
result2 = sumation(num, find_min_max)
# print(result1)
print(result2)
