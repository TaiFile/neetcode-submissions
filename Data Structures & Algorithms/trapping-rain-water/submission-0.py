class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        areas = []
        
        for i in range(size):
            # Maior altura à esquerda (incluindo i)
            max_esq = max(height[:i+1])
            # Maior altura à direita (incluindo i)
            max_dir = max(height[i:])
            
            # Água nessa posição
            agua = min(max_esq, max_dir) - height[i]
            areas.append(agua)
        
        return sum(areas)