def decode_message( s: str, p: str) -> bool:

# write your code here
        for i in range(len(s)):
            if p[i] != s[i]:
                if p[i] == "*":
                     continue
                if p[i] == "?":
                    continue
                return False
            else:
                continue
  
        return True