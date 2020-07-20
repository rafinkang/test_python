# ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC5x+ncn8T98ourNvH2x0dCiKSzWM1FFVA6DZb7ixMKQLVpAeNQIGW+RyqtikJKHjoT5B4g8WO4wEj3XFMfhQwy9kUR8iZA+Yg6kINVKWZh3lbB68eVUnRir/WaF61emzsgjHO6EBjoIFOX6Ei+3H+B5z7Gckv81yNoKFRRpgEfkrJ4LxxiYvYjWw/0lc+J27mQBR/4q14so6nvFnFv14lw5L514f1cn2tvWC7ttjQ4x8kDaVUHNDOWOxziLR+aSXVv7Ahx9wNi0Yd5RcHxbQulWz9T26zemBuFHMJKBcxO5FfA5/Nh8B2SG2HSc1Xn+9d1Kce4cfka3Nb/L7Is84txFkYh+Olssv9K0c627QfSLiLj9RrLmWBwChxuIRwlIgr1/Ko+vS0KE1uJyjItgxWVjmeQL0HptOrn4v9iYdjTR6oBYTbcp9A8O85diaZpLOHo/yeJU8Gykaf9mmztBFDHJCM4jzKyjSFN1QfdK97RaCmdtYD8mTzjCerTrfvmKck= rkdxodnr07@gmail.com

# 사용자로부터 글자를 입력받아 이 문자가 대문자인지 소문자인지 판단

# 1. 사용자의 입력값을 받아오기
data = input("입력해라 : ")
# print(data)

# 2. 이 값의 ascii 코드 값을 구한다.
# ord() ascii코드 구하는 함수
code = ord(data)

# 3. A: 65    a:97
# 4. 대문자 : 65~90    소문자 :97~122
# 5. 판단 후 출력
if code >= 97 and code <= 122:
    print(data + "는 소문자 입니다.", code)
elif code >= 65 and code <= 90:
    print(data + "는 대문자 입니다.", code)
else:
    print(data + "는 기타문자 입니다.", code)