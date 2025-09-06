class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        result = [[1],[1,1]]
        for i in range(2,numRows):
            prev_row = result[i-1]
            result.append([1] +[prev_row[j]+prev_row[j-1] for j in range(1,i)] +[1])
        return result