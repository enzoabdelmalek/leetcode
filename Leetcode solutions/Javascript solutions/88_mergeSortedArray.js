/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    let j = 0
    for(i = m; i<nums1.length; i++) {
        nums1[i] = nums2[j]
        j++
    }

    for(i = 0; i<nums1.length - 1; i++) {
        for(j = i; j<nums1.length; j++){
            if(nums1[i] > nums1[j]) {
                [nums1[i], nums1[j]] = [nums1[j], nums1[i]]
            }
        }
    }
};