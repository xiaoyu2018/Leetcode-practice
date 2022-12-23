
public partial class Solution
{
    public int MinArray(int[] numbers)
    {
        int l, r, m;
        (l, r, m) = (0, numbers.Length - 1, 0);

        while (l <= r)
        {
            m = l + ((r - l) >> 1);

            if(numbers[m]>numbers[r]) //m前部分数组有序，分界点在m右侧
                l = m + 1;
            else if(numbers[m]<numbers[r]) //m后部分数组有序，分界点在m左侧
                r = m;
            else //无法确定分界点位置，暴力缩小寻找空间
                r -= 1;
        }

        return numbers[m];
    }
}