def summarize_string(input_str):
    alphabet = [0]*26
    for ch in input_str:
        alphabet[ord(ch)-ord('a')] += 1

    for i in range(26):
        if alphabet[i] != 0:
            print("{}{}".format(chr(i+ord('a')), alphabet[i]))



input_str = "acccdeee"

print(summarize_string(input_str))