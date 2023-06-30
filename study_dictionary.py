# 딕셔너리{Dictionary}는 중괄호 사용
# 딕셔너리는 키와 값을 사용한다



# 딕셔너리 정의 및 선언
# student = {
#     "student_no": "202010958",
#     "major": "English",
#     "grade": 1
# }

# print(student["student_no"])

# student["student_no"] = "202010959"

# print(student)
# print(student["student_no"])



# 딕셔너리 데이터 조작
# student = {
#     "student_no": "202010958",
#     "major": "English",
#     "grade": 1
# }

# # 추가
# student["gpa"] = 4.5
# print(student)

# # 수정
# student["gpa"] = 3.0
# print(student)

# # 삭제
# del student["gpa"]
# print(student)


# 딕셔너리 데이터 접근 함수
# student = {
#     "student_no": "202010958",
#     "major": "English",
#     "grade": 1
# }

# print(student.get("gpa", "해당 키 -값 쌍이 없습니다."))

# # 딕셔너리 키를 반환
# print(list(student.keys()))

# # 딕셔너리의 값을 반환
# print(list(student.values()))



# 딕셔너리의 반복문
# tech = {
#     "HTML" : "Advanced",
#     "JavaScript": "Intermedia",
#     "Python": "Expert",
#     "Go": "Novice"
# }

# for key, value in tech.items():
#     print(f'{key} - {value}')

# for key in tech.keys():
#     print(key)
    
# for value in tech.values():
#     print(value)


# 중첩(Nesting)

# student_1 = {
#     "student_no": "1",
#     "gpa": "4.3"
# }

# student_2 = {
#     "student_no": "2",
#     "gpa": "3.8"
# }

# students = [student_1, student_2]


# for student in students:
#     student['graduated'] = False
#     print(student)


# student = {
#     "subjects" : ["소개론", "자바"]
# }

# print(student["subjects"])

# subjects_list = student["subjects"]

# for subject in subjects_list:
#     print(subject)


student = {
    "scholarship" : {
        "name": "국가장학금",
        "amount": "1000000" 
    }
}

# print(student)

# for key in student.keys():
#     print(key)
    
for value in student.values():
    for value_2 in value.values():
        print(value_2)