class Solution {
    public ListNode insertionSortList(ListNode head) {
        ListNode dummy = new ListNode(0);

        while (head != null) {
            ListNode cur = head;
            head = head.next;

            ListNode p = dummy;
            while (p.next != null && p.next.val < cur.val)
                p = p.next;

            cur.next = p.next;
            p.next = cur;
        }

        return dummy.next;
    }
}