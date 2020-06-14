###合并两个有序数组
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        i = m+n-1
        a = m-1
        b = n-1
        while(a>=0 and b>=0):
            if nums1[a]>nums2[b]:
                nums1[i]=nums1[a]
                i-=1
                a -=1
            else:
                print(i,b)
                nums1[i]=nums2[b]
                i-=1
                b -=1
        nums1[:b+1]=nums2[:b+1]
