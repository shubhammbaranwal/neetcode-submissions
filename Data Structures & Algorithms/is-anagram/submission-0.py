class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        else:
            characters = list(t)
            for char in s:
                if char not in characters:
                    return False
                characters.remove(char)
            return True