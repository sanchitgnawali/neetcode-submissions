class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # create a pair of position of speed of each car
        pair = [[p,s] for p, s in zip(position, speed)]
        stack = []

        # loop through reverse order in a sorted pair
        for p, s in sorted(pair)[::-1]:
            # calculate the time it takes for that car to reach the destination
            # store that value in stack
            stack.append((target - p) / s)
            
            # If the current car takes less time to
            # reach the destination then, remove the 
            # top car from the stack
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
                
        # length of the stack would be the total number of car fleets
        return len(stack)