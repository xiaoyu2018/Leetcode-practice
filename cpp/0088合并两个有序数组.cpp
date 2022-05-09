#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

void merge1(vector<int> &nums1, int m, vector<int> &nums2, int n)
{
    for (int i = 0;i<n;++i)
        nums1[m + i] = nums2[i];

    sort(nums1.begin(), nums1.end());
}

void merge2(vector<int> &nums1, int m, vector<int> &nums2, int n)
{
    vector<int> temp(m);
    for (int i= 0;i<m;++i)
    {
        temp[i] = nums1[i];
    }
    int i = 0, j = 0, k = 0;

    while (i < m and j < n)
    {
        if (temp[i] < nums2[j])
            nums1[k] = temp[i++];
        
        else
            nums1[k] = nums2[j++];

        ++ k;
    }

    if(i==m)
    {
        for (int z = 0;z<n-j;++z)
            nums1[k + z] = nums2[j + z];
    }

        
    if(j==n)
    {
        for (int z = 0; z < m - i; ++z)
            nums1[k + z] = temp[i + z];
    }
}
