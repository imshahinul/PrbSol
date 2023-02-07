class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        ctr = Counter(arr)  # obtain the number of instances of each number
        out, i, n = 0, 0, len(arr)
        while i < n:  # in replacement of the for-loop, so that we can increment i by more than 1
            j, k = i, n-1  # j should be the leftmost index, hence j=i instead of j=i+1
            while j < k:  # i <= j < k; arr[i] <= arr[j] <= arr[k]
                if arr[i]+arr[j]+arr[k] < target:
                    j += ctr[arr[j]]
                elif arr[i]+arr[j]+arr[k] > target:
                    k -= ctr[arr[k]]
                else:  # arr[i]+arr[j]+arr[k] == target
                    if arr[i] != arr[j] != arr[k]:  # Case 1: All the numbers are different
                        out += ctr[arr[i]]*ctr[arr[j]]*ctr[arr[k]]
                    elif arr[i] == arr[j] != arr[k]:  # Case 2: The smaller two numbers are the same
                        out += ctr[arr[i]]*(ctr[arr[i]]-1)*ctr[arr[k]]//2  # math.comb(ctr[arr[i]], 2)*ctr[arr[k]]
                    elif arr[i] != arr[j] == arr[k]:  # Case 3: The larger two numbers are the same
                        out += ctr[arr[i]]*ctr[arr[j]]*(ctr[arr[j]]-1)//2  # math.comb(ctr[arr[j]], 2)*ctr[arr[i]]
                    else:  # Case 4: All the numbers are the same
                        out += ctr[arr[i]]*(ctr[arr[i]]-1)*(ctr[arr[i]]-2)//6  # math.comb(ctr[arr[i]], 3)
					# Shift pointers by the number of instances of the number
                    j += ctr[arr[j]]
                    k -= ctr[arr[k]]
            i += ctr[arr[i]]  # Shift pointer by the number of instances of the number
        return out%1000000007