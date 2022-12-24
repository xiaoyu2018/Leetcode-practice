public partial class Solution
{
    public class TreeNode
    {
        public int val;
        public TreeNode left;
        public TreeNode right;
        public TreeNode(int x) { val = x; }
    }

    public int[] LevelOrder(TreeNode root)
    {
        List<int> res = new ();
        Queue<TreeNode> nodes = new();
        nodes.Enqueue(root);
        
        while(nodes.Count>0)
        {
            TreeNode crt = nodes.Dequeue();
            if(crt!=null)
            {
                res.Add(crt.val);
                nodes.Enqueue(crt.left);
                nodes.Enqueue(crt.right);
            }
        }
            
        return res.ToArray();
    }
}