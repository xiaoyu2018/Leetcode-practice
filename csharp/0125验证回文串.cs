public partial class Solution
{
    public bool IsPalindrome(string s)
    {
        string filtered_s = "";

        foreach(char c in s.ToLower())
        {
            if(char.IsDigit(c)||char.IsLetter(c))
            {
                filtered_s += c;
            }
        }

        IEnumerable<char> temp = filtered_s.Reverse();
        string rev_s = new string(temp.ToArray());

        return rev_s.Equals(filtered_s);

    }
}