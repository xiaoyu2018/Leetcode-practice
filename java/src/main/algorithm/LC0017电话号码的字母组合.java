package main.algorithm;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LC0017电话号码的字母组合 {
    Map<Character,String> memo=new HashMap<>();
    List<String> res = new ArrayList<>();
    private void _solve(int i,String digits,String tmp)
    {
        if(i==digits.length())
        {
            if (!tmp.equals(""))
                res.add(tmp);
            return;
        }

        String vals = memo.get(digits.charAt(i));
        for(int j=0;j<vals.length();j++)
        {
            _solve(i+1, digits, tmp+vals.charAt(j));
        }

    }

    public List<String> letterCombinations(String digits) {
        memo.put('2', "abc");
        memo.put('3', "def");
        memo.put('4', "ghi");
        memo.put('5', "jkl");
        memo.put('6', "mno");
        memo.put('7', "pqrs");
        memo.put('8', "tuv");
        memo.put('9', "wxyz");
        
        _solve(0, digits, "");

        return res;
    }
}

