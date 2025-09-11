def find_alphabet_occurred_alphabet(string):
    alphabet_array = [0]*26
    for i in string:
        if(i.isalpha()): # 알파벳인지 검사해서 알파벳이면
            arr_index = ord(i) - ord("a") #해당 문자를 인덱스로 치환
            alphabet_array[arr_index] +=1 #빈도수 배열에 인뎃그로 찾아가서 해당 값을 추가함

    max_occurrence = 0
    max_alphabet_index = 0

    for index in range(len(alphabet_array)):
        occurrence = alphabet_array[index]
        if occurrence > max_occurrence:
            max_occurrence = occurrence
            max_alphabet_index = index

    #index를 다시 아스키코드로 만들고 알파벳으로 만들어야함


    return chr(max_occurrence + ord("a"))

def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t", "u", "v", "x", "y", "z"]

    max_occurrence = 0
    max_alphabet = alphabet_array[0]


    for alphabet in alphabet_array:
        occurrence = 0
        for char in string:
            if char == alphabet:
                occurrence+=1
        if occurrence > max_occurrence:
            max_alphabet = char
            max_occurrence = occurrence

# 2. [0 * 26] 각 알파벳의 빈도수를 저장한 배열을 만든다
# 그리고 문자열을 돌면서 해당 문자가 알파벳이면, 알파벳을 인덱스화 시켜서 알파벳의 빈도수를 업데이트한다
# a-> 0번째 인덱스 값을 올리고, z가 나왔다면 가장 마지막인 25번쨰 인덱스의 값을 추가해라


    return max_alphabet


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))