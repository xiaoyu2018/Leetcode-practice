package main.algorithm;

public class LC1004最大连续1的个数Ⅲ {
    public int longestOnes(int[] nums, int k) {
            int ones_count=0;
            int i=0;
            int res=0;

            for(int j=0;j<nums.length;j++){
                ones_count+=nums[j];

                if(j-i+1>ones_count+k){
                    ones_count-=nums[i++];
                }
                res=Math.max(res,j-i+1);
            }

            return res;
        }

    }
}
