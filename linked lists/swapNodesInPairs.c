/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head) {
    if (head == NULL || head->next == NULL) {
        return head;
    } else {
        struct ListNode *temp = head->next;
        head->next = swapPairs(temp->next);
        temp->next = head;
        return temp;
    }
}