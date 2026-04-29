# caluclated based on weight of people
# people = [1, 2, 3, 5, 6],  limit = 6

# Sort → [1, 2, 3, 5, 6]
#         L           R

# Step 1: 1+6=7 > 6  → 6 goes alone          boats=1  [_, 2, 3, 5, _]
# Step 2: 1+5=6 ≤ 6  → 1 and 5 pair          boats=2  [_, 2, 3, _, _]
# Step 3: 2+3=5 ≤ 6  → 2 and 3 pair          boats=3  [_, _, _, _, _]

# Answer: 3 boats 

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left=0
        right=len(people)-1

        boats=0
        people.sort()
        while left<=right:
            if people[left] + people[right] <= limit:
                left+=1 # lightest person pairs with heaviest
            right-=1 # heaviest always gets a boat
            boats+=1
        return boats

        