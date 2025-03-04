def min_coins_greedy(coins, N):
    i = len(coins)
    result = []
    for i in range(i-1,-1,-1):
        while N >= coins[i]:
            N -= coins[i]
            result.append(coins[i])
        if N == 0:
            break
    return result

def min_coins_dynamic(coins,N):
    K = [float("inf")] * (N + 1)
    K[0] = 0

    for i in range(1,N+1):
        for j in range(len(coins)):
            if coins[j] <= i:
                K[i] = min(K[i],1 + K[i-coins[j]])

    return K

coins = [1, 5, 11]
N = 15
greedy = min_coins_greedy(coins,N)
dynamic = min_coins_dynamic(coins,N)

print(greedy)
print(len(greedy))

print("------------------------------------------------------>")

print(dynamic)
print(dynamic[N])
