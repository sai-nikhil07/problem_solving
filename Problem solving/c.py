# https://codeforces.com/contest/2184/problem/A

n=int(input("test cases: "))
for _ in range(n):
    s=int(input("number: "))
    if s % 3 == 0:
        print(0)
    elif s % 2==1:
        print(1)
    else:
        print(2)