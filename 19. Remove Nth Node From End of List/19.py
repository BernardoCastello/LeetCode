# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        stack = []
        while head:
            stack.append(ListNode(head.val))
            head = head.next
        
        del stack[-n]

        answer = ListNode(0)
        current = answer
        for i in stack:
            current.next = i
            current = current.next
        
        return answer.next

        
        
    

# --- Função de percorrer ---
def print_lista(head):
    current = head
    while current:
        print(f"Valor: {current.val}")
        current = current.next
    print("Fim da lista")


# 1. Criando os nós
no1 = ListNode(1)
no2 = ListNode(2)
no3 = ListNode(3)
no4 = ListNode(4)
no5 = ListNode(5)

# 2. Ligando os nós (10 -> 20 -> 30 -> None)
no1.next = no2
no2.next = no3
no3.next = no4
no4.next = no5

print_lista(no1)

S = Solution()

no1 = S.removeNthFromEnd(no1, 2)
print_lista(no1)