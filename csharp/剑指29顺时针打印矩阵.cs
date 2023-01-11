public partial class Solution
{
    public int[] SpiralOrder(int[][] matrix)
    {
        if (matrix.Length == 0)
        {
            return new int[0];
        }
        int[] res = new int[matrix[0].Length * matrix.Length];
        int l = 0, b = matrix.Length - 1, r = matrix[0].Length - 1, t = 0;
        int num = matrix[0].Length * matrix.Length;
        int k = 0;
        while (k < num)
        {
            for (int i = l; i <= r & k < num; i++)
                res[k++] = matrix[t][i];
            t++;
            
            for (int i = t; i <= b & k < num; i++)
                res[k++] = (matrix[i][r]);
            r--;
            
            for (int i = r; i >= l & k < num; i--)
                res[k++] = (matrix[b][i]);
            b--;
            
            for (int i = b; i >= t & k < num; i--)
                res[k++] = (matrix[i][l]); 
            l++;
        }
        return res;
    }

}