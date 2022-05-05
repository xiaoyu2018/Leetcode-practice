#include <vector>
#include<iostream>

using namespace std;

int strStr(string haystack, string needle)
{
    int h_size = haystack.size();
    int n_size = needle.size();
    if(n_size==0)
        return 0;
    if(h_size<n_size)
        return -1;

    for (int i = 0;i<h_size;++i)
    {
        int j = 0;
        
        if(haystack[i]==needle[0])
        {
            j = 1;
            
            for (; j < n_size; ++j)
            {
                if (i + j >= h_size)
                    return -1;
             
                if (haystack[i + j] != needle[j])
                    break;
            }

        if (j == n_size)
            return i;
        }
    }

    return -1;
}

int main()
{
    string h = "asd";
    string n = "sd";

    cout<<strStr(h,n);
}