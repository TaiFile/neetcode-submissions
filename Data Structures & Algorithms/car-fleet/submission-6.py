class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # distance = position[:]
        # size = len(position)
        # while target not in distance or max(distance) < target:
        #     for i in range(size):
        #         distance[i] += speed[i]
        # contador = Counter(distance)
        # return len(contador)

        cars = sorted(zip(position, speed), reverse=True)
        result = []
        for p,s in cars:
            time = (target - p) / s
            if not result or time > result[-1]:
                result.append(time)
        return len(result)