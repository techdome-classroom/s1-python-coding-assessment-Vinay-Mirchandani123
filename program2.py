def decode_message( s: str, p: str) -> bool:

# write your code here
        for i in range(len(s)):
            if p[i] != s[i]:
                if p[i] == "*":
                    return True
                if p[i] == "?":
                    if i == len(s)-1:
                        return False
                    continue
                return False
            if p[i] == "*":
                return True
            if p[i] == "?":
                if i == len(s)-1:
                    return False
                continue
            
                return False
  
        return False