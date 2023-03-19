package test;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;

import main.algorithm.BM17二分查找I;

public class BM17二分查找ITest {
    
    BM17二分查找I inst;

    @BeforeEach
    public void setUp()
    {
        System.out.println("asdasdasdasdasdadasd");
        this.inst = new BM17二分查找I();
    }

    @AfterEach
    public void tearDown()
    {
        this.inst = null;
    }

    @Test
    public void testSearch1() {
        assertEquals(1, this.inst.search1(new int[] { 1, 2, 3 }, 2));
    }
    
    @Test
    public void testSearch2() {
        assertEquals(1, this.inst.search2(new int[] { 1, 2, 3 }, 2));
    }
}
