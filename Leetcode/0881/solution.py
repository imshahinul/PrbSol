class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lb = 0
        ub = len(people) - 1
        no_of_boats = 0
        while lb <= ub:
            if people[lb] + people[ub] <= limit:
                lb += 1
            ub -= 1
            no_of_boats += 1
        return no_of_boats