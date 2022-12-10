
public class CQueue
{
    private int top1, top2;
    private int[] st1,st2;
    public CQueue()
    {
        top1 = top2 = -1;
        st1 = new int[10000];
        st2 = new int[10000];
    }

    public void AppendTail(int value)
    {
        st1[++top1] = value;
    }

    public int DeleteHead()
    {
        if(top2==-1)
        {
            while (top1!=-1)
            {
                st2[++top2] = st1[top1--];
            }
        }

        if(top2==-1)
            return -1;
        top2--;
        return st2[top2 + 1];

    }
}