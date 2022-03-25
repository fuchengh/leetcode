class Solution:
    def compress(self, chars: List[str]) -> int:
        current = chars[0]
        ptr = 1
        count = 1
        
        while ptr < len(chars):
            if chars[ptr] == current:
                count += 1
                del chars[ptr]
            else:
                # insert counter if counter > 1
                if count > 1:
                    to_insert = list(str(count))
                    
                    for c in to_insert:
                        chars.insert(ptr, c)
                        ptr += 1
                    # reset counter and set current char
                    current = chars[ptr]
                    count = 1
                    ptr += 1
                else:
                    # move to next char
                    current = chars[ptr]
                    ptr += 1
                
        # append last counter to char
        if count > 1:
            to_insert = list(str(count))
            chars.extend(to_insert)
            
        return len(chars)