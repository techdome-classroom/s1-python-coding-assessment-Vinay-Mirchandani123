def decode_message( s: str, p: str) -> bool:

# write your code here
        for i in range(len(p)):
            
            if p[i] == '*':
                continue
            else if p[i] == '?':
                continue
            else if p[i] != s[i]:
                return False
            
  
        return True