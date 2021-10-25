class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        rows = len(matrix)
        if rows == 0:
            return False
        cols = len(matrix[0])
        
        ansRow = 0
        ansCol = cols - 1        
        
        while ansRow < rows and ansCol >=0:
            if ansCol == 0 and matrix[ansRow][0] > target:
                return False
            # check col
            left = 0
            right = ansCol
            while right > left:
                mid = left + (right - left + 1) // 2
                if matrix[ansRow][mid] <= target:
                    left = mid
                else:
                    right = mid - 1
            ansCol = left
            
            if ansRow == rows - 1 and matrix[rows - 1][ansCol] < target:
                return False

            # check row
            top = ansRow
            down = rows - 1
            while down > top:
                mid = top + (down - top) // 2
                if matrix[mid][ansCol] >= target:
                    down = mid
                else:
                    top = mid + 1
            ansRow = top
            
            if matrix[ansRow][ansCol] == target:
                return True
            
        return False

    
if __name__ == '__main__':
        colors = "AAAABBBB"
        colors + " "
        Alice = 0
        Bob = 0
        first_idx = 0
        end_idx = 0
        color_len = len(colors)
        for idx in range(color_len):
            if idx == 0:
                continue
            if colors[idx] != colors[idx-1] or idx == color_len - 1:
                end_idx = idx
                if end_idx - first_idx > 2:
                    if colors[end_idx - 1] == 'A':
                        Alice += len(colors[first_idx:end_idx]) - 2
                    else:
                        Bob += len(colors[first_idx:end_idx]) - 2
                first_idx = end_idx
        print("1")