#function to generate ListNode


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()

    @classmethod
    def from_list(cls, arr):
        head = ListNode(arr[0])
        temp = head
        for i in range(1, len(arr)):
            temp.next = ListNode(arr[i])
            temp = temp.next
        return cls(head)

    @classmethod
    def random_list(cls, length):
        import random
        arr = [random.randint(0, 100) for _ in range(length)]
        return cls.from_list(arr)

    def to_list(self):
        temp = self.head
        arr = []
        while temp:
            arr.append(temp.val)
            temp = temp.next
        return arr
