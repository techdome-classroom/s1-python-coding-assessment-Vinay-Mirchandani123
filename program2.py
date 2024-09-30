def decode_message( s: str, p: str) -> bool:

# write your code here
        for i in range(len(s)):
            if p[i] == "*":
                
            if p[i] == "?":
                if i == len(s)-1:
                    return False
                continue
            if p[i] != s[i]:
                return False
  
        return False