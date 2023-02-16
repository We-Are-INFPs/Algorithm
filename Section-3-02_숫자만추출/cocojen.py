random_str = input()

digits = []
for char in random_str:
    if char.isdigit():
        digits.append(char)

answer = int(''.join(digits))
yaksu_gaesu = 0

for i in range(1, answer + 1):
    if answer % i == 0:
        yaksu_gaesu += 1
        
print(answer)
print(yaksu_gaesu)
    
    
    