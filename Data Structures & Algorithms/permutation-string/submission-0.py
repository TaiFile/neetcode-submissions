class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        tamanho = len(s1)
        s1_ordenada = sorted(s1)

        for i in range(len(s2) - tamanho + 1):
            substring = s2[i:i+tamanho]

            if sorted(substring) == s1_ordenada:
                return True

        return False


            
