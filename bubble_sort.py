class Sort:
    def bubble_sort(self,ele):
        size = len(ele)
        for i in range(size -1):
            swapped = False
            for j in range(size-1-i):
                if ele[j] > ele[j+1]:
                   temp = ele[j]
                   ele[j] = ele[j+1]
                   ele[j+1]=temp
                   swapped = True
            if not swapped:
                break
        return ele


if __name__ == '__main__':
    s = Sort()
    print(s.bubble_sort(['ad','gh','br','dh']))