from collections import deque

prices = [1, 2, 3, 2, 3]

def get_price_not_fall_periods(prices):
    prices_queue = deque(prices)

    while prices_queue:
        result = [0]*len(prices)
        current = prices_queue.popleft()
        count = 0
        for i in range(prices_queue):
            if current >  i:
                count+=1
            else:
                count+=1
                break
        result.append(count)




    return answer

    return



print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))