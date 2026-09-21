class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #time -> target - position[i] / speed[i]
        fleet = []
        pairs = sorted(zip(position, speed), reverse=True)

        for position, speed in pairs:
            time = (target - position) / speed
            
            if not fleet:
                fleet.append(time)
            elif fleet and time > fleet[-1]:
                fleet.append(time)

        
        return len(fleet)

        
