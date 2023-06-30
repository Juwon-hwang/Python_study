# 리스트[List]는 대괄호 사용

#colors = ['red', 'blue', 'black']

# 추가 1 (뒤에 추가)
#colors.append('purple')
#print(colors)

# 추가 2 (원하는 위치 추가)
# colors.insert(1, 'yellow')
# print(colors)W

# 제거 1 (갚을 지울 수 있지만 데이터 활용 x)
# del colors[0]
# print(colors)

# 제거 2 (제거와 동시에 이 데이터를 활용할 수 있음)
# color = colors.pop(0)
# print(colors)
# print(color)

# 제거 3 (원하는 것을 찾아 삭제)
# colors.remove('blue')
# print(colors)


# 정렬 1
# colors.sort()
# print(colors)

# colors.sort(reverse=True)
# print(colors)

# 정렬 2
# print(sorted(colors))



# 길이 - 요소의 갯수
# print(len(colors))


# 가장 끝에있는 인덱스 값 출력
# print(colors[-1])



# 리스트 슬라이싱

# colors = ['blue', 'red', 'gray', 'black']
# colors_2 = colors # 최초에 할당된 메모리 공간을 참조함
# colors_2.pop()

# print(colors)
# print(colors_2)


# colors_2 = colors[:] #새로운 메모리 공간을 할당받아 사용함
# colors_2.pop()

# print(colors)
# print(colors_2)

# print(colors_2)
# print(colors[1:3])
# print(colors[:3])
# print(colors[2:])

# print(colors[-3:])




# 리시트와 흐름제어
# scores = [88, 100, 96, 43, 65, 78]
# scores.sort(reverse = True)
# print(scores)

# for score in scores:
#     if score >= 80: 
#         print(score)
#     else:
#         print("Fail")
        



        
# 리스트 최댓값 최솟값 총합
# scores = [88, 100, 96, 43, 65, 78]

# max_val = max(scores)
# min_val = max(scores)
# sum_val = sum(scores)
# avg_val = sum(scores) / len(scores)
# print(avg_val)
# sum_values = 0

# for score in scores:
#     sum_values = sum_values + score
# print(sum_values)
        
        