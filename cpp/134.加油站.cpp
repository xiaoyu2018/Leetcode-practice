#include<vector>

using namespace std;

// 贪心
//从左向右按次序相加，一旦出现和为负，则整个区间内都不可能成为起点
int canCompleteCircuit(vector<int> &gas, vector<int> &cost)
{
    int total_s = 0;
    int crt_s = 0;
    int start = 0;

    for (int i = 0; i < gas.size(); i++)
    {
        
        total_s += (gas[i] - cost[i]);
        crt_s += (gas[i] - cost[i]);

        if(crt_s<0)
        {
            start = i+1;
            crt_s = 0;
        }
    }

    if(total_s<0)
        return -1;

    return start;
}