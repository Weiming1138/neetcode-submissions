class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []
        pairs = sorted(zip(position, speed), reverse=True) #Arrange it in descending order since only forms fleet with car in front

        for pos, spd in pairs:
            time = (target - pos) / spd #Calculate the time using position and speed
            
            if not fleet: #If the fleet is empty, add the new time
                fleet.append(time)
            elif fleet and time > fleet[-1]: #If its not empty and the current time is greater than the top of the stack (slower than front), form a fleet
                fleet.append(time)
        
        return len(fleet)
            
            


