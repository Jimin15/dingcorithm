def is_number_exist(number, array):
    #1.배열을 하나씩 탐색해서 number랑 같은게 있는지 찾기
    #2.같은게 있으면 true를 반환 아니면 False를 반환
    for i in array:
        if number == i:
            return True
        else:
            return False



result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3, [3,5,6,1,2,4]))
print("정답 = Flase 현재 풀이 값 =", result(7, [6,6,6]))
print("정답 = True 현재 풀이 값 =", result(2, [6,9,2,7,1888]))