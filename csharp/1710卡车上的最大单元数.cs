public partial class Solution
{

    public int MaximumUnits(int[][] boxTypes, int truckSize)
    {
        int res = 0;
        Array.Sort(boxTypes, new Comp());

        // foreach(var t in boxTypes)
        // {
        //     foreach(var i in t)
        //     {
        //         System.Console.Write($"{i} ");
        //     }
        //     System.Console.WriteLine();
        // } 

        foreach (var box in boxTypes)
        {
            if (box[0] > truckSize)
            {
                res += truckSize * box[1];
                break;
            }
            truckSize -= box[0];
            res += box[0] * box[1];
        }


        return res;
    }
}

internal class Comp : IComparer<int[]>
{
    public int Compare(int[]? x, int[]? y)
    {
        if (x != null && y != null)
            return y[1] - x[1];
        throw new Exception("!!!");
    }
}