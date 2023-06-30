# 함수(Functions)
# 매개변수(파라미터), 인자(인수)

# 'name' => 파라미터 [파라미터는 정의하는곳에 쓰이는 변수같은 개념]
# def print_name(name):
#     print(f'이름은 {name}입니다')

# # "Juwon" = > 인자 [실제로 할당되는 값은 인자(인수)임]  
# print_name("Juwon")
# print_name("Minjae")



# def print_ex_string():
#     print('예시 문자열 입니다.')
    
# print_ex_string()

# def print_name_age(name, age):
#     print(f'이름은 {name}이고, {age}살 입니다.')
    
# print_name_age("황주원", "23")
# print_name_age()


# 이런식으로 파라미터에 default값을 넣고싶은 경우에는 맨뒤로 넣을것
# def order_coffee(qty, option = 'hot'):
#     print(f'{qty}잔 / {option}')
    
    
# order_coffee(3)
# order_coffee('iced', 3)
# order_coffee(option = 'iced', qty = 3)


# def get_id(email): 
    
#     if email.endswith('@test.com'):
    
#         email_id = email.removesuffix("@test.com")
#         print(email_id)
        
#         return email_id

#     else:
#         print('처리할 수 없는 이메일 주소입니다.')
        
        
# user_id = get_id('user@naver.com')
# print(user_id)

# user_id = get_id('user@test.com')
# print(user_id)

from study_module import *

user_id = get_id('user@tedt.com')
print(user_id)




