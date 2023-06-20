N = int(input())

words = []
for i in range(N):
    word = input()
    words.append(word)

poem = []
for i in range(N-1):
    poem.append(input())
    
ans = list(set(words).difference(set(poem)))
print(ans[0])

"""
5
big
good
sky
blue
mouse
sky
good
mouse
big
"""