/**
 * Definition for singly-linked list.
 * l1ublic class ListNode {
 *     l1ublic int val;
 *     l1ublic ListNode next;
 *     l1ublic ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode listHead = new ListNode(0);
        ListNode ll1 = l1, ll2 = l2, current = listHead;
        int carry = 0;
        while (ll1 != null || ll2 != null) {
            int x = (ll1 != null) ? ll1.val : 0;
            int y = (ll2 != null) ? ll2.val : 0;
            int sum = carry + x + y;
            carry = sum / 10;
            current.next = new ListNode(sum % 10);
            current = current.next;
            if (ll1 != null) ll1 = ll1.next;
            if (ll2 != null) ll2 = ll2.next;
        }
        if (carry > 0) {
            current.next = new ListNode(carry);
        }
        return listHead.next;
        
    }
}