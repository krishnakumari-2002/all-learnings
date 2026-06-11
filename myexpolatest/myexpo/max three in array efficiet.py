class Solution():
    def max(self, s):
        length = len(s)
        if length < 3:
            print("Should have at least three elements")
            return

        s_sorted = sorted(s, reverse=True)
        elements = (s_sorted[0], s_sorted[1], s_sorted[2])
        max_sum = sum(elements)

        return max_sum, elements

obj = Solution()
s = [2, 8, 9, 12, 6, 1, 3]
max_sum, elements = obj.max(s)
print("elements", elements)
print("max", max_sum)
