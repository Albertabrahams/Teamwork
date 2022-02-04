def fibonacci(n):
    fibo = [1,1]
    for i in range(1,n):
        fibo.append(fibo[i-1]+fibo[i])

    print(fibo[n])

fibonacci(12)
    