class Solution:
  def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    out = []
    bucket = [0] * 1001

    for elm in arr1:
      bucket[elm] += 1

    for elm in arr2:
      while bucket[elm] > 0:
        out.append(elm)
        bucket[elm] -= 1

    for num in range(1001):
      for _ in range(bucket[num]):
        out.append(num)

    return out