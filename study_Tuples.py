# 튜플(Tuples)은 소괄호 사용
# 튜플은 각각의 요소의 값을 변경 X
# 튜플을 통째로 다시 할당하는것은 가능


# tup = (1, 20, 40)
# print(tup)

# tup = (100, 30, 40)
# print(tup)

# for x in tup:
#     print(x)

# 튜플을 리스트로 처리하는 방법
tup = (1, 20, 40)

list_1 = list(tup)
list_2 = [x for x in tup]

print(list_1)
print(list_2)

# 리스트 변환의 원시적인 방법
list_3 = []

for x in tup:
    list_3.append(x)

print(list_3)