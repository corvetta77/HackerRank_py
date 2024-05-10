if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])

    arr.sort(key=lambda x: (x[1], x[0]))
    arr.pop(0)

    print(arr[0][0])
    for i in range(len(arr)):
        if i + 1 < len(arr):
            if arr[i][1] == arr[i + 1][1]:
                print(arr[i+1][0])
