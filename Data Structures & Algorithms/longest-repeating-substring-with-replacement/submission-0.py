class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        size = len(s)
        result = 0
        for i in range(size):
            janela = ""
            for j in range(i, size):
                janela += s[j]  # vai acumulando a janela
                mais_frequente = max(Counter(janela).values())
                trocas = len(janela) - mais_frequente
                if trocas <= k:
                    result = max(result, len(janela))
                else:
                    break  # janela inválida, para de expandir
        return result