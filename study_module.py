# 모듈(연관이 있는 함수의 집합)
def get_id(email): 
    
    if email.endswith('@test.com'):
    
        email_id = email.removesuffix("@test.com")
        return email_id

    else:
        print('처리할 수 없는 이메일 주소입니다.')
        return('처리불가능')