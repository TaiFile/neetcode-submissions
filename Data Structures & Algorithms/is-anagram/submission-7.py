class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Primeira tentativa
        # hashset = set()
        # for i,j in zip(s,t):
        #     hashset.add(i)
        #     hashset.add(j)


        # Fazer primeiro por força bruta
        # Converter t em lista para poder marcar/remover elementos
        # t_list = list(t)

        # for charS in s:
        #     found = False
        #     for i, charT in enumerate(t_list):
        #         if charS == charT:
        #             t_list.pop(i)   # remove esse caractere de t
        #             found = True
        #             break
        #     if not found:
        #         return False

        # return True

        # Tentando fazer por sort
        # listaS = sorted(list(s))
        # listaT = sorted(list(t))
        # if(listaS == listaT):
        #     return True
        # else:
        #     return False

        if Counter(s) == Counter(t):
            return True
        else:
            return False

