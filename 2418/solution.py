class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [h for _, h in sorted(zip(heights,names),reverse=True)]