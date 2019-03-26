class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        '''
        Use dp method to solve this problem
        '''
        m,n=len(s),len(p)
        dp = [[False for _ in range(m+1)] for _ in range(n+1)] # don't use dp=[[False]*m]*n 
        dp[0][0] = True
        for j in range(n):
            tmp = dp[j][0] and p[j]=='*'
            dp[j+1][0] = tmp
        for j in range(n):
            for i in range(m):
                if p[j] == '?' or p[j] == s[i]:
                    dp[j+1][i+1] = dp[j][i]
                elif p[j] == '*':
                    dp[j+1][i+1] = dp[j+1][i] or dp[j][i+1]
                else:
                    dp[j+1][i+1] = False
        return dp[n][m]





if __name__ == '__main__':
    s="adceb"
    p="*a*b"
    sol = Solution()
    res = sol.isMatch(s,p)
    print(res)






