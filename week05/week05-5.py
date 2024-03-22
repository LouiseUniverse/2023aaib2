class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a=[]
        while head != None:
            a.append(head.val)
            head = head.next
        print(a)

        N=len(a)
        for i in range(N):
            if a[i] != a[N-1-i]: return False
        return True
