class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_value(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        counter = 0
        itr =self.head
        while itr:
            counter += 1
            itr = itr.next

        return counter

    def remove_at(self,index):
        if index < 0  or index >= self.get_length():
            raise Exception('index out of range')

        if index == 0:
            self.head = self.head.next
            return

        counter = 0
        itr = self.head
        while itr:
            if counter == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            counter += 1

    def insert_at(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception('invalid index')

        if index == 0:
            self.insert_at_begining(data)

        counter = 0
        itr = self.head
        while itr:
            if counter == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr=itr.next
            counter += 1

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_value(["banana","mango","grapes","orange"])
    ll.remove_at(2)
    ll.insert_at(2,'grapes')
    ll.print()