class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []
        pairs = sorted(zip(position, speed), reverse=True)

        for position, speed in pairs:
            time = (target - position) / speed

            if not fleet:
                fleet.append(time)
            elif fleet and fleet[-1] < time:
                fleet.append(time)
        
        return len(fleet)
            
            
