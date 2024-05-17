import sys


def find_path(n, m):
    arr = [i for i in range(1, n+1)]
    path = [] 
    current_index = 0
    path.append(arr[current_index])
    while True:
        next_index = (current_index + m) % len(arr)  - 1
        if next_index == 0:
            break 
        path.append(arr[next_index])
        current_index = next_index  
    return ''.join(map(str, path))


if __name__ == '__main__':
    try:
        array_length = int(sys.argv[1]) 
        interval = int(sys.argv[2])
    except ValueError:
        print("Wrong params")
        sys.exit(1)
        
    print(find_path(array_length, interval))
