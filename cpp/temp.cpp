#include<stdio.h>
#include<string.h>

struct TreeNode
{
    char val[50];
    TreeNode *left;
    TreeNode *right;
};

char st1[100];
int st2[200];
int top1=-1, top2=-1;

int string2Num(char s[])
{
    int len = 0;
    for (; s[len]!='\0'; ++len)
        ;
    int res = 0;
    for (int i = len - 1; i >= 0; i--)
    {
        res = res * 10 + s[i] - '0';
    }

    return res;
}
void Tree2Stack(TreeNode *root)
{
    if(root)
    {
        if (
            root->val[0] == '+' ||
            root->val[0] == '-' ||
            root->val[0] == '*' ||
            root->val[0] == '/' )
        {
            st1[++top1] = root->val[0];
        }

        else
        {
            st2[++top2] = string2Num(root->val);
        }

        // 满足无交换律的二元计算计算顺序
        Tree2Stack(root->right);
        Tree2Stack(root->left);
    }
}

int GetResult()
{
    while (top1>-1)
    {
        char op= st1[top1--];
        int a = st2[top2--];
        int b = st2[top2--];
        switch (op)
        {
        case '+':
            st2[++top2] = a + b;
            break;
        case '-':
            st2[++top2] = a - b;
            break;
        case '*':
            st2[++top2] = a * b;
            break;
        case '/':
            st2[++top2] = a / b;
            break;
        }
    }

    return st2[top2];
}

int main()
{

    printf("%d", sizeof(int));
}