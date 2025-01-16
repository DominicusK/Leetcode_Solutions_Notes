
'''
This solution uses histogram and Stack based appproach
'''

class Solution_1:
    def maximalRectangle(self, matrix):
        rec=[]

        # If matrix is empty return 0
        if not matrix:
            return 0
        
        # Creating height list with len of matrix row
        height=[0]*len(matrix[0])
        

        # Iterating over each row and a column
        for i in range(len(matrix)):
            for j in range(len(height)):
                 
                 # This creates an histogram of heights for each row in matrix used to calculate area
                 if matrix[i][j] =='1':
                     height[j]+=1 
                 else:
                     height[j]=0
            
            # calling cal_max_area. returns max height for height histogram row
            max_area=self.cal_max_area(height)
            # Appends the max height for each row and then return the max height
            rec.append(max_area)
        return max(rec) 
        
    
    def cal_max_area(self, hist_h):
     # Ensures while loop condition remains to calculate areas
     hist_h = hist_h + [0]

     # Using Stack Based approach which stores histogram indices 
     stack = []
     max_area = 0  

     # iterate through heights
     for i in range(len(hist_h)):
         # While stack not empty & height is less than the height stored at he last index in stack.
         while stack and hist_h[i] < hist_h[stack[-1]]:
             #Pop height of the top of the stack
             h = hist_h[stack.pop()]  
             # Width between current index & top of stack e.g 7-3 = 4 --> -1 to get index width 3 
             w = i if not stack else i - stack[-1] - 1  
             max_area = max(max_area, h * w)  

         stack.append(i)

     return max_area  

"""
Cases Below with extremes
"""
#matrix_test = [["1","0","1","1"],
#               ["1","1","1","1"],
#               ["0","1","1","0"]]

#matrix_test=[["1","1"]]

#matrix_test=[["0"]]

# heights_=[0,3,4,6,0,4,5,0,0,3]

#s=Solution_1()
#max_Rec=s.maximalRectangle(matrix=matrix_test)
#print(max_Rec)