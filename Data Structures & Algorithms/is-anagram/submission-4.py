class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = {}
        td = {}

        for char in s:
            if char not in sd:
                sd[char] = 1
            else:
                sd[char] += 1
        
        for char in t:
            if char not in td:
                td[char] = 1
            else:
                td[char] += 1

        # print(sd, td)
        
        if sd == td:
            return True
        else:
            return False