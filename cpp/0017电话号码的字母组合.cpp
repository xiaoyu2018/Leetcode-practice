#include<vector>
#include<iostream>
#include<vector>

using namespace std;

const string d2lmap[10] = {
    "",
    "",
    "abc",
    "def",
    "ghi",
    "jkl",
    "mno",
    "pqrs",
    "tuv",
    "wxyz",
};

vector<string> res;
string temp = "";

//建立回溯树，明确深度和广度，深度用递归遍历，广度用循环遍历
void backTracking(int s, vector<int> digits)
{
    if(s==digits.size())
    {
        res.push_back(temp);
        return;
    }

    for(char ch :d2lmap[digits[s]])
    {
        temp.push_back(ch);
        backTracking(s + 1, digits);
        temp.pop_back();
    }
    
}

vector<string> letterCombinations(string digits)
{

    if(digits.size())
    {
        int num = stoi(digits);
        int len = digits.size();
        vector<int> nums(len);
        do
        {
            nums[len - 1] = num % 10;
            
            num /= 10;
        } while (--len);

        for (auto i : nums)
        {
            cout << i;
        }

        backTracking(0, nums);
    }

    return res;
}


int main()
{
    letterCombinations("123");
}