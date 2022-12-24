
public partial class Solution
{

    public IList<IList<int>> LevelOrder1(TreeNode root)
    {
        Queue<TreeNode> nodes = new Queue<TreeNode>();
        List<IList<int>> res = new();
        nodes.Enqueue(root);

        while (nodes.Count>0)
        {
            int size = nodes.Count;
            List<int> temp = new();
            for (int i = 0; i<size;++i)
            {
                TreeNode crt = nodes.Dequeue();
                if(crt!=null)
                {
                    temp.Add(crt.val);
                    nodes.Enqueue(crt.left);
                    nodes.Enqueue(crt.right);
                }
            }
            if(temp.Count>0)
                res.Add(temp);
        }
        return res;
    }
}