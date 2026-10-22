class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []
        pair = sorted(zip(position, speed), reverse=True)

        for position, speed in pair:
            time = (target - position) / speed

            if not fleet:
                fleet.append(time)
            elif fleet and time > fleet[-1]:
                fleet.append(time)
        
        return len(fleet)