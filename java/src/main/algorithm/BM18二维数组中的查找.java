package main.algorithm;

public class BM18二维数组中的查找 {
    public boolean Find(int target, int[][] array) {
        int m = array.length;
        if(m==0)
            return false;
        int n = array[0].length;
        if(n==0)
            return false;
        
        int i = 0, j = n-1;
        while(0<=i&&i<m&&0<=j&&j<n)
        {
            if (target == array[i][j])
                return true;
            else if(target<array[i][j])
                j -= 1;
            else
                i += 1;
        }
        
        return false;
    }
}
