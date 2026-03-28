class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols= set()
        diag = set()
        antidiag = set()
        res = []
        def dfs(i,j,result):
            if i==n:
                return
            cols.add(j)
            diag.add(i-j)
            antidiag.add(j+i)
            row = ""
            for idx in range(n):
                if idx == j:
                    row+="Q"
                else:
                    row+="."
            result.append(row)
            if i==n-1 and len(result)==n:
                res.append(result[:])
            for itr in range(n):
                if  itr not in cols and (itr+i+1) not in antidiag and (i+1-itr) not in diag:
                    dfs(i+1,itr,result)
            cols.remove(j)
            diag.remove(i-j)
            antidiag.remove(i+j)
            result.pop()
            
       
        for i in range(n):
            dfs(0,i,[])

        return res