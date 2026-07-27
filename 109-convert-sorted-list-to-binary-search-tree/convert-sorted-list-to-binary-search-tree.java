import java.util.*;

class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        List<Integer> list = new ArrayList<>();

        while (head != null) {
            list.add(head.val);
            head = head.next;
        }

        return build(list, 0, list.size() - 1);
    }

    private TreeNode build(List<Integer> list, int left, int right) {
        if (left > right)
            return null;

        int mid = (left + right) / 2;

        TreeNode root = new TreeNode(list.get(mid));
        root.left = build(list, left, mid - 1);
        root.right = build(list, mid + 1, right);

        return root;
    }
}