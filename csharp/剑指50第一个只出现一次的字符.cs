
public partial class Solution
{
    public char FirstUniqChar(string s)
    {
        Dictionary<char, int> dict = new Dictionary<char, int>();

        foreach(char ch in s)
        {
            dict[ch] = dict.ContainsKey(ch)?dict[ch] + 1 :1;
        }

        foreach(char key in dict.Keys)
        {
            if(dict[key]==1)
                return key;
        }
        return ' ';
    }
}