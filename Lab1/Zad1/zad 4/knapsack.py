MAX_BACKPACK_CAPACITY = 20

class Item:
    def __init__(self, weight: int, value: int, name: str) -> None:
        self.weight = weight
        self.value = value
        self.name = name


class Backpack:
    def __init__(self) -> None:
        self.items : list[Item] = []

    def __str__(self) -> str:
        if not self.items:
            return "Empty"
        return "\n".join(["    "+item.name for item in self.items])

    def add_item(self, item: Item):
        self.items.append(item)

    def empty_backpack(self):
        self.items = []

    @property
    def backpack_weight(self) -> int:
        return sum([item.weight for item in self.items])

    @property
    def backpack_value(self) -> int:
        return sum([item.value for item in self.items])


    @staticmethod
    def knapsack_procedural(items):
        n = len(items)
        dp = [[0 for _ in range(MAX_BACKPACK_CAPACITY + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(1, MAX_BACKPACK_CAPACITY + 1):
                if items[i-1].weight <= w:
                    dp[i][w] = max(items[i-1].value + dp[i-1][w-items[i-1].weight], dp[i-1][w])
                else:
                    dp[i][w] = dp[i-1][w]

        w = MAX_BACKPACK_CAPACITY
        optimal_items = []
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i-1][w]:
                optimal_items.append(items[i-1])
                w -= items[i-1].weight

        return optimal_items

    @staticmethod
    def knapsack_functional(items):
        def knapsack(n, capacity):
            if n == 0 or capacity == 0:
                return 0, []

            if items[n-1].weight > capacity:
                return knapsack(n-1, capacity)

            value_with, items_with = knapsack(n-1, capacity - items[n-1].weight)
            value_with += items[n-1].value

            value_without, items_without = knapsack(n-1, capacity)

            if value_with > value_without:
                return value_with, items_with + [items[n-1]]
            else:
                return value_without, items_without

        _, optimal_items = knapsack(len(items), MAX_BACKPACK_CAPACITY)
        return optimal_items


if __name__ == "__main__":
    backpack = Backpack()

    items = [
        Item(weight=5, value=30, name="Water Bottle"),
        Item(weight=10, value=50, name="Tent"),
        Item(weight=3, value=20, name="First Aid Kit"),
        Item(weight=7, value=40, name="Sleeping Bag"),
        Item(weight=2, value=10, name="Flashlight"),
        Item(weight=1, value=5, name="Map"),
        Item(weight=4, value=25, name="Hiking Boots"),
        Item(weight=6, value=35, name="Cooking Set"),
        Item(weight=8, value=45, name="Food Supplies"),
        Item(weight=9, value=55, name="Camera")
    ]


    optimal_items_procedural = Backpack.knapsack_procedural(items)
    for item in optimal_items_procedural:
        backpack.add_item(item)

    print("Procedural:")
    print(f"Max value: {backpack.backpack_value}")
    print(f"Backpack weight: {backpack.backpack_weight}")
    print("Items:")
    print(backpack)
    print("")

    backpack.empty_backpack()

    optimal_items_functional = Backpack.knapsack_procedural(items)
    for item in optimal_items_functional:
        backpack.add_item(item)

    print("Functional:")
    print(f"Max value: {backpack.backpack_value}")
    print(f"Backpack weight: {backpack.backpack_weight}")
    print("Items:")
    print(backpack)

