# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result=ListNode()
        
        res_cur=result
        l1_cur=l1
        l2_cur=l2
        flag=0
        
        while True:
            if l1_cur!=None:
                res_cur.next=ListNode()
                res_cur=res_cur.next
                if l2_cur!=None:
                    res_cur.val=l1_cur.val+l2_cur.val+flag
                    l1_cur=l1_cur.next
                    l2_cur=l2_cur.next
                else:
                    res_cur.val=l1_cur.val+flag
                    l1_cur=l1_cur.next
            else:
                if l2_cur!=None:
                    res_cur.next=ListNode()
                    res_cur=res_cur.next
                    res_cur.val=l2_cur.val+flag
                    l2_cur=l2_cur.next
                else:
                    if flag==1:
                        res_cur.next=ListNode()
                        res_cur.next.val=1
                    break
                    
            if res_cur.val>=10:
                flag=1
                res_cur.val-=10
            else:
                flag=0            
            
        return result.next
                