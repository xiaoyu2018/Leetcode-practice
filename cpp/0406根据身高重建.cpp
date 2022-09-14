#include<list>
#include<vector>
#include<algorithm>

using namespace std;
static bool cmp(const vector<int> &a, const vector<int> &b)
{
    if(a[0]!=b[0])
        return a[0] > b[0];
    return a[1] < b[1];
}
vector<vector<int>> reconstructQueue(vector<vector<int>> & people)
{
    sort(people.begin(), people.end(), cmp);
    list<vector<int>> que; // list底层是链表实现，插入效率比vector高的多
    for (int i = 0; i < people.size(); i++)
    {
        int position = people[i][1]; // 插入到下标为position的位置
        std::list<vector<int>>::iterator it = que.begin();
        while (position--)
        { // 寻找在插入位置
            it++;
        }
        que.insert(it, people[i]);
    }
    return vector<vector<int>>(que.begin(), que.end());
}