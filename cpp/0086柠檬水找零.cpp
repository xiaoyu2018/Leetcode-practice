#include<vector>

using namespace std;


bool lemonadeChange(vector<int> &bills)
{
    //记录5美元和10美元的数量
    int changes[2] = {0};

    for(int m:bills)
    {
        bool fall = false;
        switch (m)
        {
        case 20:
            //只可能找零一次10元
            if(changes[1])
            {
                changes[1]--;
                m -= 10;
            }
            fall = true;
        case 10:
            //付10元：找一张五元，进账一张十元
            //付20元，不进账零钱，找一张或三张十元
            if(!fall)
                changes[1]++;
            for (;m>5&&changes[0]>0;m-=5,changes[0]--)
                ;
            break;
        case 5:
            changes[0]++;
        }

        if(m!=5)
            return false;
    }

    return true;
}