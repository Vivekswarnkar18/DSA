class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        st=set()
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]==".":
                    continue
                row=board[i][j]+"row"+str(i)
                column=board[i][j]+"column"+str(j)
                box=board[i][j]+"box"+str(i//3)+str(j//3)
                if row in st or column in st or box in st:
                    return False
                st.add(row)
                st.add(column)
                st.add(box)
        return True
        