class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def Array_Partition( arr, lowest, highest ):
            i = ( lowest-1 )
            pivot_element = arr[ highest ]
            for j in range( lowest, highest ):
                if arr[ j ] <= pivot_element:

                    i = i+1
                    arr[ i ], arr[ j ] = arr[ j ], arr[ i ]

            arr[ i+1 ], arr[ highest ] = arr[ highest ], arr[ i+1 ]
            return ( i+1 )

        def QuickSort( arr, lowest, highest ):
            if len( arr ) == 1:
                return arr
            if lowest < highest:
                pi = Array_Partition( arr, lowest, highest )
                QuickSort( arr, lowest, pi-1 )
                QuickSort( arr, pi+1, highest )
        nums = QuickSort( nums, 0, len(nums)-1 )