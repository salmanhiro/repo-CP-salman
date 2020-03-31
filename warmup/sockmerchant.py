def sockMerchant(n, ar):
    count = 0
    ar.sort()
    i = 0
    while i<n-1:
        if ar[i]==ar[i+1]:
            count = count+1
            i+=2
        else:
            i+=1
    return count


n = int(input())
ar = list(map(int, input().rstrip().split()))
result = sockMerchant(n, ar)
print(result)