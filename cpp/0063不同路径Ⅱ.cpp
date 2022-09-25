#include<vector>
#include<iostream>
using namespace std;

int uniquePathsWithObstacles(vector<vector<int>> &obstacleGrid)
{
    const int m = obstacleGrid.size();
    const int n = obstacleGrid[0].size();
    // 使用一维滚动数组
    int dp[n] = {0};

    for (int i = 0;i<n&&!obstacleGrid[0][i];i++)
        dp[i] = 1;
    
    for (int i = 1; i < m; i++)
        for (int j = 0; j < n; j++)
            dp[j] = obstacleGrid[i][j] ? 0 : (j == 0 ? dp[j] : dp[j] + dp[j - 1]);
        
    

    return dp[n - 1];
}

int main()
{
    vector<vector<int>> v = {{1, 0}, {0, 0}};

    cout << uniquePathsWithObstacles(v);
}