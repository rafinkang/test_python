# 임포트하는 방법 3가지

# 1. import 모듈명 - 모듈 채 가져오기
import random
print(dir())

# import random
# import math

# 2. form 모듈명 import 함수명 - 모듈내 함수 한개만 꺼내기
# 이 경우 다른모듈에 동일한 함수가 있을 경우 충돌날 우려가 있음.
from random import randint  # random 모듈 중 randint 만 불러다 쓴다.
n = randint(100,200)
print(n)
print(dir())

# 3. from 모듈명 import * - 모듈내 함수 전체 가져오기
# 이름 충돌 날 경우가 많을껴
from random import *
print(dir())
