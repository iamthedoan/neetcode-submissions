class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "0#"
        else:
            sep = str(len(strs)) + "#"
            return sep + sep.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "0#":
            return []
        
        i = 0
        while s[i] != "#":
            i = i+1
        
        sep = s[0:i+1]

        s = s[len(sep):]
        if s == "":
            return [s]
        else:
            return s.split(sep)