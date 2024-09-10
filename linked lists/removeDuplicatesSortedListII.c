/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode **trav;
    for (trav = &head;*trav != NULL && (*trav)->next != NULL;){
        if ((*trav)->val == (*trav)->next->val) {
            int dupVal = (*trav)->val;
            while (((*trav)->val == dupVal && (*trav)->next != NULL)) {
                struct ListNode *temp = *trav;
                *trav = temp->next;
                free(temp);
            }
            if ((*trav)->next == NULL && (*trav)->val == dupVal) {
                struct ListNode *temp = *trav;
                *trav = temp->next;
                free(temp);
            }
        } else {
            trav = &(*trav)->next;
        }
    }
    return head;
}