
foreach(var line in new Solution().Generate(5))
{
    foreach(var i in line)
    {
        System.Console.WriteLine(i);
    }
}
