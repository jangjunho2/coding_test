# 백준 1018

def checkBoard(board, n, m):
    count = 0
    for i in range(n, n+8):
        for j in range(m, m+8):
            # 보드의 색깔과 실제 체스판의 색깔과 일치하면 count+=1
            if board[i][j] == checkColor(i, j):
                count += 1

    resultArray.append(count)


def checkColor(n, m):
    if (n+m) % 2 == 0:  # 짝수면 흰
        return 'W'
    else:  # 홀수면 검
        return "B"


def checkMinCase():
    # min case == min or 64-max
    a, b = min(resultArray), (64-max(resultArray))
    print(a if a < b else b)


n, m = map(int, input().split())
board = [input() for _ in range(n)]  # 보드 입력

maxRow = n-8
maxCol = m-8  # [maxRow][maxCol]까지 읽을수있음
resultArray = []

for i in range(maxRow+1):
    for j in range(maxCol+1):
        pass
        # board[i][j]  # 여기를 체스판 왼쪽위(검정일지 흰색일지 모르니 흰으로 가정하고)로 잡고 검사 #검정색일 경우 대부분칠하니까
        # 반대로 생각해서 64-max인 경우 하면됨
        checkBoard(board, i, j)

checkMinCase()
