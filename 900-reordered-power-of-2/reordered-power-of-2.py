class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        temp = 1
        arr = []
        while temp<10**9:
            tmp = temp
            text = ""
            while tmp>0:
                text+=str(tmp%10)
                tmp= tmp//10
            arr.append(sorted("".join(text)))
            temp*=2
        n = str(n)
        n = sorted(n)
        if n in arr:
            return True
        else:
            return False
