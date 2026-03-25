# leet code count primes
class Solution:
    def countPrimes(self, n: int) -> int:
        c=1
        if n<=2:
            return 0
        pri=[True]*n
        pri[0]=pri[1]=False
        for  i in range(2,int(n**0.5)+1):
            if pri[i]:
                for j in range(i*i,n,i):
                    pri[j]=False
            
        return sum(pri)




        # for i in range(3,n,2):
        #     p=True
        #     for j in range (2,int(i**0.5)+1):
        #         if i %j==0:
        #             p= False
        #             break
        #     if p:
        #         c+=1
        
        # return c
