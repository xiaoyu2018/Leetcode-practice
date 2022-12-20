public class MinStack
{

    /** initialize your data structure here. */
    Stack<int> st = new();
    Stack<int> as_st = new();
    public MinStack()
    {
        as_st.Push(int.MaxValue);
    }

    public void Push(int x)
    {
        st.Push(x);

        as_st.Push(Math.Min(x, as_st.Peek()));
            
    }

    public void Pop()
    {
        st.TryPop(out _);
        as_st.TryPop(out _);
    }

    public int? Top()
    {
        int res;
        if(st.TryPeek(out res))
            return res;
        return null;
    }

    public int? Min()
    {
        int res;
        if(as_st.TryPeek(out res))
            return res;
        return null;
    }
}
