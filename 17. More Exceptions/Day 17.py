#Write your code here

class e(Exception):
    "n and p should be non-negative"


class Calculator():
    def power(self, n, p):
        try:
            if n | p < 0:
                raise e

            else:
                return (n ** p)
        except e:
            return ("n and p should be non-negative")



myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   
        