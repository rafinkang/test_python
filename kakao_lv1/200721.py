'''
https://programmers.co.kr/learn/courses/30/lessons/64061
크레인 인형뽑기 게임

게임 화면의 격자의 상태가 담긴 2차원 배열 board
인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves
크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return
'''
def solution(board, moves):
    print("============================================================")
    answer = 0
    baguni = []

    for i in moves:        
        for j in range(len(board[i-1]), 0, -1):
            if board[i-1][j-1] != 0:
                if len(baguni) and baguni[-1] == board[i-1][j-1]:
                    answer += 2
                    baguni.pop()
                else:
                    baguni.append(board[i-1][j-1])

                board[i-1][j-1] = 0
                break
        print(answer, baguni, board)
    return answer

b = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
m = [1,5,3,5,1,2,1,4]
print(solution(b, m))
