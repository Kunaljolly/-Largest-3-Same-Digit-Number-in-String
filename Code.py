class Solution:
    def largestGoodInteger(self, num: str) -> str:
        t = []
        for x in range(len(num)-2):
            if num[x] == num[x+1] and num[x+1] == num[x+2]:
                t.append(int(num[x:x+3]))
        if t == []:
            return ""
        if max(t) == 0:
            return "000"
        return str(max(t))

