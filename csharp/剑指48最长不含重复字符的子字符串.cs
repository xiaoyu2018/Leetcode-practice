public partial class Solution
{
    public int LengthOfLongestSubstring1(string s)
    {
        if (s.Length < 1)
            return 0;

        int res = 1, temp = 1;
        Dictionary<char, int> dict = new();
        dict[s[0]] = 0;

        for (int i = 1; i < s.Length; i++)
        {
            int j = dict.GetValueOrDefault(s[i], -1);
            dict[s[i]] = i;
            temp = j < i - temp ? temp + 1 : i - j;
            res = Math.Max(res, temp);
        }
        return res;
    }
}