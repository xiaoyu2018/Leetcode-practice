package main.algorithm;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class LC0040组合总和Ⅱ {
    List<List<Integer>> res = new ArrayList<>();
    ArrayList<Integer> tmp = new ArrayList<>();
    private void _solve(int[] candidates,int start,int target,int s)
    {
        if (s > target)
            return;
        if(s==target)
        {
            res.add((ArrayList<Integer>) tmp.clone());
        }

        Set<Integer> memo = new HashSet<>();
        for(int i=start;i<candidates.length;++i)
        {
            if(!memo.contains(candidates[i]))
            {
                tmp.add(candidates[i]);
                _solve(candidates, i+1, target, s+candidates[i]);
                tmp.remove(tmp.size() - 1);

            }
            memo.add(candidates[i]);
        }
        
    }

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        _solve(candidates, 0, target, 0);
        return res;
    }
}
