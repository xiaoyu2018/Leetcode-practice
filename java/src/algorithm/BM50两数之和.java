package algorithm;

import java.util.Hashtable;
import java.util.Map;

public class BM50两数之和 {
    public int[] twoSum(int[] numbers, int target) {
        Map<Integer, Integer> map = new Hashtable<Integer, Integer>();
        map.put(numbers[0], 0);

        for(int i=1;i<numbers.length;++i)
        {
            if (map.containsKey(target - numbers[i]))
                return new int[] { map.get(target - numbers[i])+1, i+1 };
            map.put(numbers[i], i);
        }
        
        return new int[] {};
    }
}
