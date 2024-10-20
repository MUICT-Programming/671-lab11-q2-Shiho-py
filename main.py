# YOUR CODE HERE
def sumation(lst1,lst2, operation) :
    
    cal_list = []

    for c in range(len(lst1)) :
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

lst1 = []
lst2 = []

for i in range(num) :
        a = int(input())
        lst1.append(a)

for l in range(num) :
    b = int(input())
    lst2.append(b)

result2 = sumation(lst1,lst2, find_min_max)
print(result2)
