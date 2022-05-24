#include<unordered_set>
#include<vector>
using namespace std;


vector<int> intersection(vector<int> &nums1, vector<int> &nums2)
{
    unordered_set<int> res;
    unordered_set<int> s(nums1.begin(), nums1.end());

    for(int i : nums2)
    {
        if(s.find(i)!=s.end())
            res.insert(i);
    }

    return vector<int>(res.begin(),res.end());
}