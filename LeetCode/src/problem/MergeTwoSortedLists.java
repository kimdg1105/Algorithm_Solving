package problem;


/*
 * Problem Number: 21
 * https://leetcode.com/problems/merge-two-sorted-lists/
 */

public class MergeTwoSortedLists {

    private ListNode pickSmaller(ListNode a, ListNode b) {
        if (a == null && b != null) {
            return b;
        }
        if (b == null && a != null) {
            return a;
        }
        if (a.val >= b.val) {
            return b;
        } else {
            return a;
        }
    }

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode smallerNode = null;
        if (list1 == null) {
            smallerNode = list2;
        } else if (list2 == null) {
            smallerNode = list1;
        } else {
            smallerNode = pickSmaller(list1, list2);
        }

        if (smallerNode == null) {
            return null;
        }

        if (smallerNode == list1) {
            return new ListNode(smallerNode.val, mergeTwoLists(list1.next, list2));
        }
        if (smallerNode == list2) {
            return new ListNode(smallerNode.val, mergeTwoLists(list1, list2.next));
        }
        return null;
    }

    class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }
}
