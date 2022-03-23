class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        # if counter > numRows, it is a middle char
        middle = numRows - 2
        counter = 0
        mid_count = 0
        
        # seperate s into columns
        cols = []
        
        for c in s:
            counter += 1
            if counter > numRows:
                if mid_count < middle:
                    # this is a middle char
                    this_col = [-1 for _ in range(middle - mid_count)]
                    this_col.append(c)
                    this_col.extend([-1 for _ in range(numRows - middle + mid_count - 1)])
                    cols.append(this_col)
                    mid_count += 1
                elif mid_count == middle: # return to normal cols
                    cols.append([c])
                    counter = 1
                    mid_count = 0
            else: #counter < numRows
                # append to last col
                if len(cols) > 0:
                    cols[-1].append(c)
                else:
                    cols.append([c])
            
        # put placeholders in the last col
        cols[-1].extend([-1 for _ in range(numRows - len(cols[-1]))])
        
        # print res
        res = ""
        for i in range(len(cols[0])):
            for j in range(len(cols)):
                if cols[j][i] != -1:
                    res += cols[j][i]
        return res
        
        