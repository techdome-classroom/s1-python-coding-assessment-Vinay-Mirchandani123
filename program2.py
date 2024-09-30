def decode_message( s: str, p: str) -> bool:

# write your code here
        count* = 0
        count
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