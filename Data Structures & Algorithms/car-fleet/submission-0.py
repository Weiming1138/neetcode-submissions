class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []
        pairs = sorted(zip(position, speed), reverse=True)

        for pos, spd in pairs:
            time = (target - pos) / spd
            
            if not fleet:
                fleet.append(time)
            elif fleet and time > fleet[-1]:
                fleet.append(time)
        
        return len(fleet)
            
            


