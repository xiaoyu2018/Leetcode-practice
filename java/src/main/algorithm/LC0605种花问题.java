package main.algorithm;

public class LC0605种花问题 {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int res = 0;
        int i = 0;
        int size = flowerbed.length;
        while (i < size) {
            if (i > 0 && flowerbed[i - 1] == 1)
            {
                i += 1;
                continue;
            }
            if (flowerbed[i] == 0) {
                if ((i + 1) == size || flowerbed[i + 1] == 0)
                    res += 1;
                else
                {
                    i += 3;
                    continue;
                }
            }
            i += 2;
        }

        return res >= n;
    }
}
