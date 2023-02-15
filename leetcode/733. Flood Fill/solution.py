class Solution(object):
    def floodFill(self, image, sr, sc, newcolor):
        color = image[sr][sc]
        R, C = len(image), len(image[0])
        if color == newcolor:
            return image

        def some(r, c):
            if image[r][c] == color:
                image[r][c] = newcolor
                if r - 1 >= 0: some(r - 1, c)
                if r + 1 < R: some(r + 1, c)
                if c - 1 >= 0: some(r, c - 1)
                if c + 1 < C: some(r, c + 1)

        some(sr, sc)
        return image
