class Solution:

    key = "#1"

    def encode(self, strs: List[str]) -> str:
        k = self.key
        resp = ""
        for s in strs:
            resp += f"{k}{s}{k}"
        return resp

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        k = self.key
        ptr = len(k)
        s = s[ptr:-ptr]
        return s.split(f"{k}{k}")
