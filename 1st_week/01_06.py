input = 20


def find_prime_list_under_number(number):
    #소수의 정의: 1과 자신만으로 나눠지는 수, 2,3,5,7로는 안나눠짐
    #배열을 돌아보면서 2,3,5,7로 나눴을때 나머지가 하나라도 0이라면 넣지말기
    sosu_array = []
    for i in range(2, number+1):
        if(i==2 or i==3 or i==5 or i==7):
            sosu_array.append(i)

        if i%2==0 or i%3==0 or i%5==0 or i%7==0:
            continue
        else:
            sosu_array.append(i)

    return sosu_array


result = find_prime_list_under_number(input)
print(result)

def find_prime_list_under_number2(number):
    #소수의 정의: 1과 자신만으로 나눠지는 수, 2,3,5,7로는 안나눠짐
    #배열을 돌아보면서 2,3,5,7로 나눴을때 나머지가 하나라도 0이라면 넣지말기
    sosu_array = []
    for n in range(2, number+1):
        for i in sosu_array:
            if i*i >= n and n % i == 0:
                break
        else:
            sosu_array.append(i)

    return sosu_array


result = find_prime_list_under_number2(input)
print(result)