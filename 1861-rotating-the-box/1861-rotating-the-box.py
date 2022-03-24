class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        modified_box = []
        
        for row in range(len(box)):
            modified_row = []
            this_row = "".join(box[row])
            row_sep_by_wall = this_row.split("*")
            # for each seperated subarray, move space in front of stones
            for elem in row_sep_by_wall:
                num_space = Counter(elem)["."]
                num_stones = len(elem) - num_space
                new_elem = "".join(["." for _ in range(num_space)] + ["#" for _ in range(num_stones)])
                modified_row.append(new_elem)
            modified_row = "*".join(modified_row)
            modified_box.append(list(modified_row))
        
        row = len(modified_box)
        col = len(modified_box[0])
        res = []
        for j in range(col):
            new_row = []
            for i in range(row):
                new_row.append(modified_box[i][j])
            res.append(new_row[::-1])
        
        return res