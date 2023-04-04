package main.algorithm;

import java.util.Arrays;

public class LC0912排序数组 {

    public int[] sortArray(int[] nums) {
        // 内置排序
        Arrays.sort(nums);
        return nums;
    }

    // 快排
    public void quickSort(int[] nums, int i, int j) {
        if (i >= j)
            return;

        int tmp = nums[i];
        int l = i;
        int r = j;
        while (l < r) {
            for (; l < r && nums[r] >= tmp; r--)
                ;
            if (l < r)
                nums[l++] = nums[r];

            for (; l < r && nums[l] <= tmp; l++)
                ;
            if (l < r)
                nums[r--] = nums[l];
        }
        nums[l] = tmp;
        quickSort(nums, i, l - 1);
        quickSort(nums, l + 1, j);
    }

    // 归并排序
    public int[] mergeSOrt(int[] nums, int i, int j) {
        if (i == j)
            return new int[] { nums[i] };

        int mid = i + ((j - i) >> 1);
        int[] l_a = mergeSOrt(nums, i, mid);
        int[] r_a = mergeSOrt(nums, mid + 1, j);

        int[] res = new int[j - i + 1];
        int m = 0, n = 0, k = 0;

        while (m < l_a.length && n < r_a.length) {
            if (l_a[m] < r_a[n])
                res[k++] = l_a[m++];
            else
                res[k++] = r_a[n++];

        }

        for (; m < l_a.length; m++)
            res[k++] = l_a[m];
        for (; n < r_a.length; n++)
            res[k++] = r_a[n];

        return res;
    }

    // 堆排序
    // 1 将乱序数组建堆（从最后一个子树开始建堆）
    // 2 交换根节点与最后的堆节点，并将堆数组长度减一后重新建堆
    // 3 重复n次后堆数组有序，大根堆则是升序排列，小根堆是降序排列
    public void heapSOrt(int[] nums) {
        int len = nums.length - 1;
        int bgn_idx = (len - 1) >> 1;

        for (int i = bgn_idx; i >= 0; i++) {
            maxHeapify(nums, i, len);
        }

    }

    // 将某个子树建堆
    private void maxHeapify(int[] nums, int root, int len) {

        if (root > len)
            return;
        int l = (root >> 1) + 1;
        int r = l + 1;
        if (l > len)
            return;
        int max_idx;
        if (r > len)
            max_idx = l;
        else
            max_idx = nums[l] > nums[r] ? l : r;

        if (nums[max_idx] > nums[root]) {
            nums[max_idx] ^= nums[root];
            nums[root] ^= nums[max_idx];
            nums[max_idx] ^= nums[root];

            maxHeapify(nums, max_idx, len);
        }
    }

}
