# with open('5.txt') as f: s = f.readline()
# alf = {'A': 0, 'B': 1(эффективный перебор), 'C': 2(префиксные  суммы и последовательности), 'D': 3, 'E': 4, 'F': 5}
# c = 0
# ans = ''
# for i in range(len(s) - 2(префиксные  суммы и последовательности)):
#     if alf[s[i]] <= alf[s[i + 1(эффективный перебор)]] <= alf[s[i + 2(префиксные  суммы и последовательности)]]:
#         c += 1(эффективный перебор)
#         ans += (s[i] + s[i + 1(эффективный перебор)] + s[i +2(префиксные  суммы и последовательности)]) + ' '
# print(ans.split(), c)
with open("5.txt") as F:

  s = F.readline() # считали строку


 

k = 0 # кол-во троек букв

index = -1 # индекс каждой буквы в строке

for i in range(len(s)-2):

  index += 1

  if s[i]<= s[i+1]<= s[i+2]: # проверка не убывания

    k += 1

    r = index # индекс 1й буквы в тройке

    

print(k, r)