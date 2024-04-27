import math

def euclideanDistance():
    x1 = int(input("Enter the x value for the first point: "))
    y1 = int(input("Enter the y value for the first point: "))
    x2 = int(input("Enter the x value for the second point: "))
    y2 = int(input("Enter the y value for the second point: "))

    return print("Euclidian distance:", math.sqrt(((x2-x1)**2) + ((y2-y1)**2)))


points = [(10,5), (6,12), (20,4), (7,15), (9,11), (2,18), (14,9), (11,6), (5,17)]

distances = []

for i in range(len(points)):
    for j in range(len(points)):
        if(i != j):
            x1, y1 = points[i]
            x2, y2 = points[j]

            dist = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
            distances.append(dist)

min = distances[0]

for i in distances:
    if(i < min):
        min = i

print("Minimum distance between the points in the 'points' tuple: ", min)
