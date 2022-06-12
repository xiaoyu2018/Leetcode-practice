#include<string>
#include<iostream>
using namespace std;

// 扩容后使用双指针
string replaceSpace(string s)
{
    int count = 0;

    for(char ch :s)
    {
        if(ch==' ')
            ++count;
    }
    int old_size = s.size();
    s.resize(old_size + count * 2);
    int new_size = s.size();

    for (int i = old_size-1, j = new_size-1;i<j;--i,--j)
    {   
        if(s[i]==' ')
        {
            s[j--] = '0';
            s[j--] = '2';
            s[j] = '%';
        }
        else
            s[j] = s[i];
    }

    return s;
}


int main()
{
    string s = "hello world";
    // s=replaceSpace(s);
    
    cout << s;
}