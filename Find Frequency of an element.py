arr = list(map(int, input("Enter elements separated by space: ").split()))

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("\nFrequency of elements:")
for key, value in freq.items():
    print(key, ":", value)