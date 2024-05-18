import math


def euclideanDistance(n1, n2):
    r = n1[1] - n2[1]
    q = n1[0] - n2[0]
    if r < 0:
        r *= -1
    if q < 0:
        r *= -1
    p = math.sqrt(q ** 2 + r ** 2)
    return p


def euclideanDistanceWithoutLib(n1, n2):
    r = n1[1] - n2[1]
    q = n1[0] - n2[0]
    if r < 0:
        r *= -1
    if q < 0:
        r *= -1
    p = (q ** 2 + r ** 2) ** 0.5
    return p


node1 = (3, 4)
node2 = (-1, 10)
node3 = (7, 2)
node4 = (4, -8)
node5 = (-7, 20)
points = [node1, node2, node3, node4, node5]
length = len(points)
distances = [euclideanDistance(points[0], points[1])]
distances2 = [euclideanDistanceWithoutLib(points[0], points[1])]
for i in range(1, length - 1):
    for j in range(i + 1, length):
        distances.append(euclideanDistance(points[i], points[j]))
        distances2.append(euclideanDistanceWithoutLib(points[i], points[j]))

print("Minimum distance is: " + str(min(distances)))
print("Minimum distance is: " + str(min(distances2)) + " (Calculated without library usage)")
