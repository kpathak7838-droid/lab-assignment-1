# AERT Toolkit 

# -------------------------
# Part A: Stack ADT
# -------------------------
class StackADT:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# -------------------------
# Part B: Factorial
# -------------------------
def factorial(n):
    if n < 0:
        return "Invalid Input"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# -------------------------
# Fibonacci (Naive + Memo)
# -------------------------
call_count_naive = 0
call_count_memo = 0

def fib_naive(n):
    global call_count_naive
    call_count_naive += 1

    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)


memo = {}
def fib_memo(n):
    global call_count_memo
    call_count_memo += 1

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n-1) + fib_memo(n-2)

    return memo[n]


# -------------------------
# Part C: Tower of Hanoi using Stack
# -------------------------
def hanoi(n, source, aux, dest, stack):
    if n == 1:
        move = f"Move disk 1 from {source} to {dest}"
        print(move)
        stack.push(move)
        return

    hanoi(n-1, source, dest, aux, stack)

    move = f"Move disk {n} from {source} to {dest}"
    print(move)
    stack.push(move)

    hanoi(n-1, aux, source, dest, stack)


# -------------------------
# Part D: Binary Search
# -------------------------
def binary_search(arr, key, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)


# -------------------------
# MAIN FUNCTION
# -------------------------
def main():
    print("===== AERT TOOLKIT =====")

    # Stack Demo
    print("\n----- STACK ADT -----")
    s = StackADT()
    s.push(10)
    s.push(20)
    print("Top:", s.peek())
    print("Size:", s.size())
    print("Pop:", s.pop())

    # Factorial
    print("\n----- FACTORIAL -----")
    for n in [0, 1, 5, 10]:
        print(f"Factorial({n}) = {factorial(n)}")

    # Fibonacci
    print("\n----- FIBONACCI -----")
    for n in [5, 10, 20, 30]:
        global call_count_naive, call_count_memo
        call_count_naive = 0
        call_count_memo = 0
        memo.clear()

        print(f"\nN = {n}")
        print("Naive:", fib_naive(n), "| Calls:", call_count_naive)
        print("Memo :", fib_memo(n), "| Calls:", call_count_memo)

    # Tower of Hanoi using Stack
    print("\n----- TOWER OF HANOI (N=3) -----")
    move_stack = StackADT()
    hanoi(3, 'A', 'B', 'C', move_stack)

    print("\nStored Moves in Stack:")
    temp_stack = StackADT()

    # Reverse stack to print in correct order
    while not move_stack.is_empty():
        temp_stack.push(move_stack.pop())

    while not temp_stack.is_empty():
        print(temp_stack.pop())

    # Binary Search
    print("\n----- BINARY SEARCH -----")
    arr = [1, 3, 5, 7, 9, 11, 13]
    tests = [7, 1, 13, 2]

    for key in tests:
        result = binary_search(arr, key, 0, len(arr)-1)
        print(f"Search {key}: {result}")

    print("Empty array test:", binary_search([], 5, 0, -1))


# Run program
if __name__ == "__main__":
    main()
