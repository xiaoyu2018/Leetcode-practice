public partial class Solution
{
    private int count = 0;
    private int res = -1;
    private void InOrder(TreeNode root,ref int k)
    {
        if(root!=null)
        {
            InOrder(root.right,ref k);
            if(++count==k)
            {
                res = root.val;
                return;
            }
            InOrder(root.left, ref k);
        }
    }
    public int KthLargest(TreeNode root, int k)
    {
        InOrder(root, ref k);
        return res;
    }
}