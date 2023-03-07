from collections import deque
import sys
input = sys.stdin.readline


def game():
    direct = 'R'
    x, y = (0, 0)
    graph[x][y] = 'O'
    result = 0
    move = move_list.popleft()[0]
    # tail =
    while 1:
        dx, dy = x + direct_dict[direct][0], y + direct_dict[direct][1]
        if graph[dx][dy] == 'O' or dx >= N or dy >= N or dx < 0 or dy < 0:
            print(result)
            break
        graph[dx][dy] = 'O'
        if graph[dx][dy] == '*':
            pass
        else:
            graph[x][y] = 'X'
        x, y = dx, dy
        result += 1
        if move == result:
            move = move_list.popleft()
    return


N = int(input())
K = int(input())
graph = [['X' for _ in range(N)] for _ in range(N)]
for i in range(K):
    x, y = map(int, input().split())
    graph[x][y] = '*'

L = int(input())
for i in range(L):
    X, C = map(str, input().split().rstrip())
    X = int(X)
    move_list = deque((X, C))

direct_dict = {'R': (0, 1), 'D': (-1, 0), 'L': (0, -1), 'U': (1, 0)}
