# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())
for i in range(t):
    s = str(input())
    print(s[::2], s[1::2])
    