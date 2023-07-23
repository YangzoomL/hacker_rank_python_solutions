if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    arr = sorted(arr,reverse=True)
    max=arr[0]
    for i in arr:
        if i!=max:
            print(i)
            break
    