import salary as s
import random
print(s.raise_sal(5000))
print(s.reduce_sal(3000))

print('------------------------------------------')
import lottosalary as ls

# 50% 확률로 급여가 20%인상
print(ls.raise_rnd_salary(5000))
# 50% 확률로 급여가 20% 감소
print(ls.reduce_rnd_salary(5000))
