class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        length = len(s)
        setSize = 2 * numRows - 2
        numSets = length // setSize
        numRemainingLetters = length % setSize
        numLastDiagonal = numRemainingLetters - numRows

        resultChars = list()
        numCols = (numSets + 1) * 2
        for row in range(numRows):
            for col in range(numCols):
                # Skip if row limit exceeded
                if numLastDiagonal <= 0 and col == numCols - 2 and row >= numRemainingLetters:
                    # Ends with vertical, last col reached and exceeded last row
                    continue
                if numLastDiagonal > 0 and col == numCols - 1 and row < numRows - numLastDiagonal - 1:
                    # Ends with diagonal, last col reached and before last row
                    continue

                i = None
                # First and last row only have numSets + 1 cols
                if (row == 0 or row == numRows - 1) and col % 2 == 0:
                    i = col // 2 * setSize + row
                # Other rows have 2 * (numSets + 1) cols
                elif not row == 0 and not row == numRows - 1 and col % 2 == 0:
                    # Verticals
                    i = col // 2 * setSize + row
                elif not row == 0 and not row == numRows - 1 and col % 2 == 1:
                    # Diagonals
                    i = (col // 2 + 1) * setSize - row

                if i is not None and i < length:
                    resultChars.append(s[i])

        return ''.join(resultChars)
