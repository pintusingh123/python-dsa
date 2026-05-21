class Double_ended_queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
# Example usage:
if __name__ == "__main__":
    deq = Double_ended_queue()
    deq.add_rear(1)
    deq.add_rear(2)
    deq.add_front(3)

    print(deq.remove_front())  # Output: 3
    print(deq.remove_rear())   # Output: 1
    print(deq.size())          # Output: 1