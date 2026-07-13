class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        heights = [0] * cols
        max_area = 0

        for row in matrix:

            # Update histogram heights
            for j in range(cols):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            max_area = max(max_area, self.largestRectangle(heights))

        return max_area

    def largestRectangle(self, heights):
        stack = []
        max_area = 0

        heights.append(0)

        for i in range(len(heights)):

            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                max_area = max(max_area, h * width)

            stack.append(i)

        heights.pop()

        return max_area