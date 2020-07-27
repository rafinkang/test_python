# 연관된 함수들의 모음 :  모듈 - 모듈의 이름은 파일의 이름을 따른다.
author = "홍길동"

def raise_sal(sal):
    '''
    입력한 급여를 전달하면 10% 인상된 급여를 리턴
    '''
    return int(sal * 1.1)


def reduce_sal(sal):
    return int(sal*0.8)

# __main__일때만(현재 페이지 일때만) 실행
# __name__ == 모듈의 이름을 가진 변수
# test code

if __name__ == "__main__":
    print(raise_sal(3000))
    print(reduce_sal(1000)) # 20% 감소
    print("잘나오나?", author)
    print(__name__) # __m^.^m__




