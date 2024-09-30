def decode_message( s: str, p: str) -> bool:

# write your code here
        countStar = 0
        countQues
        for i in range(len(p)-1,-1,-1):
            
            if p[i] == '*':
                countStar+=1
            elif p[i] == '?':
                continue
            elif p[i] == s[i]:
                continue
            else:
                return False
            
        
        return True