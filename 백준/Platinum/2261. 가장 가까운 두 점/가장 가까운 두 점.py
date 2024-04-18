import math
import sys

input = sys.stdin.readline


def closest_point(plane: list[list[int, int]]) -> tuple[float, float]:
    X, Y = 0, 1
    # 점이 3개 이하인 경우 최저 거리 계산
    if len(plane) <= 3:
        return find_close_dist(plane)  # 최소거리, 최소거리**2 반환

    # 정렬된 점들을 x축을 기준으로 반반 나눔
    mid = len(plane) // 2
    left_plane = plane[:mid]
    right_plane = plane[mid:]

    left_d, left_d_squared = closest_point(left_plane)
    right_d, right_d_squared = closest_point(right_plane)
    d = min(left_d, right_d)
    d_squared = min(left_d_squared, right_d_squared)

    # 2D범위 이내의 있는 점들의 거리
    points_in_2d = [p for p in plane if abs(p[X] - plane[mid][X]) < d]
    points_in_2d.sort(key=lambda point: point[Y])  # Y좌표 기준 정렬

    # closest_distance, closest_distance_squared = min(find_close_dist(points_in_2d), (d, d_squared))
    # Y축으로 정렬한 이후 Y축 방향으로만! d이상이 경우는 더이상 계산하지 않기 위한 로직
    closest_distance_squared = d_squared  # 중간을 포함하지 않은 L,R에서 구한 최솟값의 제곱
    for i in range(len(points_in_2d) - 1):
        for j in range(i + 1, len(points_in_2d)):
            if points_in_2d[j][Y] - points_in_2d[i][Y] >= d:  # Y축 방향으로 d이상 떨어져있으면 더이상 탐색 X
                break
            # Y축 방향으로 d이상 떨어져 있지 않은경우 (계산)
            d_squared = (points_in_2d[j][X] - points_in_2d[i][X]) ** 2 + (points_in_2d[j][Y] - points_in_2d[i][Y]) ** 2
            # 거리가 이전에 구한 최솟값보다 더 작은경우 최솟값 갱신
            if d_squared < closest_distance_squared:
                closest_distance_squared = d_squared
    closest_distance = math.sqrt(closest_distance_squared)
    return closest_distance, closest_distance_squared


# brute force
def find_close_dist(arr: list[list[int, int]]) -> tuple[float, float]:
    X, Y = 0, 1
    min_d_squared = float("inf")
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            squared_d = (arr[i][X] - arr[j][X]) ** 2 + (arr[i][Y] - arr[j][Y]) ** 2
            if squared_d < min_d_squared:
                min_d_squared = squared_d
    if min_d_squared == float("inf"):
        min_d = float("inf")
    else:
        min_d = math.sqrt(min_d_squared)

    return min_d, min_d_squared


plane = []

n = int(input())
for i in range(n):
    plane.append(list(map(int, input().split())))

plane.sort(key=lambda plane: plane[0])  # X좌표를 기준으로 오름차순 정렬
closest_distance, closest_distance_squared = closest_point(plane)
# print(closest_distance, closest_distance_squared)
print(closest_distance_squared)
