def decode_message( s: str, p: str) -> bool:

# write your code here
        countStar = 0
        countQuestion = 0
        for i in range(len(p)-1,-1,-1):
            
            if p[i] == '*':
                countStar+=1
            elif p[i] == '?':
                countQuestion+=1
            elif p[i] == s[i]:
                continue
            else:
                return False
            
        
        return True

def isMatch(message, pattern):
    m, n = len(message), len(pattern)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    # Initialize dp for patterns with leading *
    for j in range(1, n + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif pattern[j - 1] == '?' or pattern[j - 1] == message[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]

    return dp[m][n]