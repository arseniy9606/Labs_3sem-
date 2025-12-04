class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get("ignore_case", False)
        self.items = iter(items)
        self.seen = set()

    def __iter__(self):
        return self

    def __next__(self):
        for item in self.items:
            key = item
            if isinstance(item, str) and self.ignore_case:
                key = item.lower()
            if key not in self.seen:
                self.seen.add(key)
                return item
        raise StopIteration


if __name__ == "__main__":
    from gen_random import gen_random

    print("Unique([1,1,1,2,2,2]) →")
    for x in Unique([1, 1, 1, 2, 2, 2]):
        print(x)

    print("\nUnique(gen_random(10, 1, 3)) →")
    for x in Unique(gen_random(10, 1, 3)):
        print(x)

    print("\nUnique(['a','A','b','B','a','A'], ignore_case=False) →")
    for x in Unique(['a', 'A', 'b', 'B', 'a', 'A'], ignore_case=False):
        print(x)

    print("\nUnique(['a','A','b','B','a','A'], ignore_case=True) →")
    for x in Unique(['a', 'A', 'b', 'B', 'a', 'A'], ignore_case=True):
        print(x)
