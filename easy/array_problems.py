#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : ZhaoYY
#pylint: disable=invalid-name

"""
    problems about array.
"""


class ArrayProblem:
    """
    array problems
    """

    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp_dict = {}
        for i, num in enumerate(nums):
            temp_dict[num] = i
            if target - num in temp_dict:
                return [temp_dict[target - num], i]

    @classmethod
    def reverse(cls, num):
        """
        :type x: int
        :rtype: int
        """
        flag = False
        if num < 0:
            flag = True
            num = -num
        result = 0
        while num > 0:
            result = result * 10 + num % 10
            num = num // 10
        if result > 2**31:
            result = 0

        return -result if flag else result

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or l2 and l1.val > l2.val:
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1
    def removeElement(self, nums, val):
        """
        https://leetcode.com/problems/remove-element/description/
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[r] == val:
                r -= 1
                continue
            if nums[l] != val:
                l += 1
                continue
            nums[l], nums[r] = nums[r], nums[l]
            r -= 1
            l += 1
        return l + 1

    def removeDuplicatesBetter(self, nums, val):
        '''
        :type nums: List[int]
        :type val: int
        :rtype: int
        '''
        pre = -1
        for _, n in enumerate(nums):
            if n != val:
                pre += 1
                nums[pre] = n
        return pre + 1

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        for i, n in enumerate(nums):
            if n >= target:
                return i
        return i + 1

    def searchInsertBetter(self, nums, target):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l + 1 if nums[l] < target else l

    def isToeplitzMatrix(self, matrix):
        """
        https://leetcode.com/problems/toeplitz-matrix/description/
        
        :type matrix: List[List[int]]
        :rtype: bool
        """
        m, n = len(matrix) - 1, len(matrix[0]) - 1
        for i in range(n):
            a, b = 0, i
            while a < m and b < n:
                if matrix[a][b] != matrix[a + 1][b + 1]:
                    return False
                a += 1
                b += 1
        
        for i in range(1, m):
            a, b = i, 0
            while a < m and b < n:
                print([a, b, n, m])
                if matrix[a][b] != matrix[a + 1][b + 1]:
                    return False
                a += 1
                b += 1
        return True


    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        t = [x * 100 + i for i, x in enumerate(nums)]
        t.sort()
        m = t[-1] // 100
        n = t[-2] // 100 
        if n == 0 or m // n >= 2:
            return t[-1] % 100
        else:
            return -1

    # def findMedianSortedArrays(self, nums1, nums2):
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: float
    #     """
    #     step = (len(nums1) + len(nums2)) // 2
    #     r1, r2 =len(nums1) - 1, len(nums2) - 1
    #     for _ in range(step):
    #         if r1 >=0 and r2 >= 0:
    #             if nums1[r1] > nums2[r2]:
    #                 r1 -= 1
    #             else:
    #                 r2 -= 1
    #         elif r2 >= 0:
    #             r2 -= 1
    #         else:
    #             r1 -= 1
    #     if (len(nums1) + len(nums2)) % 2 == 0:
    #         return 

if __name__ == '__main__':
    ARRAY_PROBLEM = ArrayProblem()
    # print(ARRAY_PROBLEM.isToeplitzMatrix([[11,74,0,93],[40,11,74,7]]))
    print(ARRAY_PROBLEM.dominantIndex([1,0]))
