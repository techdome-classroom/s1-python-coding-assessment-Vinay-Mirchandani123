def decode_message( s: str, p: str) -> bool:

# write your code here
        for i in range(len(p)-1,-1,-1):
            
            if p[i] == '*':
                count
            elif p[i] == '?':
                continue
            elif p[i] == s[i]:
                continue
            else:
                return False
            
        
        return True