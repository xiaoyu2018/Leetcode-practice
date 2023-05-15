package main.algorithm;

import java.util.Stack;

public class LC0739每日温度 {
    // 超时
    public int[] dailyTemperatures1(int[] temperatures) {
        int size = temperatures.length;
        int[] res = new int[size];

        for (int i = 0; i < size - 1; i++) {
            int crt = temperatures[i];
            for (int j = i + 1; j < size; j++) {
                if (temperatures[j] > crt) {
                    res[i] = j - i;
                    break;
                }
            }
        }
        return res;
    }
    
    // 单调栈
    // 求左侧第一个比当前值大的值下标
    // 单调栈中存放下标，存放的是由栈底到栈顶递减的值的下标
    // 因为下一个元素如果比栈内元素大的话，便找到了左侧第一个比当前值大的值下标
    public int[] dailyTemperatures(int[] temperatures) {
        int size = temperatures.length;
        int[] res = new int[size];
        Stack<Integer> st = new Stack<>();

        st.add(0);

        for (int i = 1; i < size; i++) {
            do{
                if(temperatures[st.peek()]<temperatures[i])
                {
                    int tmp = st.pop();
                    res[tmp] = i - tmp;
                }
                else
                    break;
            } while (!st.isEmpty());
            st.add(i);
        }
        return res;
    }
}
