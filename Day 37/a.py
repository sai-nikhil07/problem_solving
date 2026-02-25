https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits

# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # a=[]
        # for i in arr:
            
        #     a.append(bin(i)[2:].count('1'))
            
        # # print(a)

        # d= dict(zip(arr,a))

        # sorted_d = dict(sorted(d.items(), key=lambda item: item[1]))

        # result = sorted(d, key=lambda x: (d[x], x)) this is not working for all the test cases
        
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))
