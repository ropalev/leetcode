class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        prev_row = [1,1]
        for i in range(2, rowIndex+2):
            curr_row = [1]+ [prev_row[j] + prev_row[j-1] for j in range(1,i-1)] +[1]
            prev_row = curr_row
        return curr_row