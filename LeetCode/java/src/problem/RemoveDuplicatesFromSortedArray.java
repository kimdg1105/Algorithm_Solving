package problem;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/*
 * Problem Number: 26
 * https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
 */
public class RemoveDuplicatesFromSortedArray {
    public static void main(String[] args) {
        RemoveDuplicatesFromSortedArray solution = new RemoveDuplicatesFromSortedArray();
        int[] arr = {1, 1, 2};
        System.out.println(solution.removeDuplicates(arr));
        Arrays.stream(arr).forEach(System.out::print);
    }

    public int removeDuplicates(int[] nums) {
        int givenCount = nums.length;
        Set<Integer> set = new HashSet<>();
        Arrays.stream(nums).forEach(set::add);
        int uniqueCount = set.size();

        int[] ans = set.stream().sorted()
                .mapToInt(Integer::intValue)
                .toArray();

        for (int i = 0; i < ans.length; i++) {
            nums[i] = ans[i];
        }

        return uniqueCount;
    }

}
