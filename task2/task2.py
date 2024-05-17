import math
import sys


def point_position(center, radius, point):
    distance = math.sqrt((point[0] - center[0])**2 + (point[1] - center[1])**2)
    
    if math.isclose(distance, radius):
        return "0"  # Точка находится на окружности
    elif distance < radius:
        return "1"  # Точка внутри окружности
    else:
        return "2"  # Точка снаружи окружности

def read_circle_info(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        center = tuple(map(float, lines[0].strip().split()))
        radius = float(lines[1].strip())
    
    return center, radius

def read_points(filename):
    with open(filename, 'r') as file:
        points = []
        for line in file:
            point = tuple(map(float, line.strip().split()))
            points.append(point)
    
    return points

def main():
    if len(sys.argv) != 3:
        print("Wrong params!")
        return
    
    circle_filename = sys.argv[1]
    points_filename = sys.argv[2]
    
    # Чтение информации об окружности из файла
    center, radius = read_circle_info(circle_filename)

    # Чтение информации о точках из файла
    points = read_points(points_filename)

    # Рассчитываем положение каждой точки относительно окружности
    for point in points:
        position = point_position(center, radius, point)
        print(position)


if __name__ == "__main__":
    main()
