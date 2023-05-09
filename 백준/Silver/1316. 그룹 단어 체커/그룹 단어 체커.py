n = int(input())
for i in range(n):
    word = list(input())
    word_set = set(word)
    for j in word_set:
        if j in word[word.index(j) + word.count(j):]:
            # print(j)

            n -= 1
            break
print(n)
