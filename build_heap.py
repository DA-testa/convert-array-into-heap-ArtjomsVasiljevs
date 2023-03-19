# python3

def build_heap(data):
    swaps = []
    for i in range(len(data)//2, -1, -1):
        min_idx = i
        left_child = 2 * i + 1
        if left_child < len(data) and data[left_child] < data[min_idx]:
            min_idx = left_child
        right_child = 2 * i + 2
        if right_child < len(data) and data[right_child] < data[min_idx]:
            min_idx = right_child
        if i != min_idx:
            data[i], data[min_idx] = data[min_idx], data[i]
            swaps.append((i, min_idx))
            while min_idx * 2 + 1 < len(data):
                j = min_idx * 2 + 1
                if j + 1 < len(data) and data[j+1] < data[j]:
                    j += 1
                if data[min_idx] <= data[j]:
                    break
                swaps.append((min_idx, j))
                data[min_idx], data[j] = data[j], data[min_idx]
                min_idx = j
    return swaps

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
if __name__ == "__main__":
    main()
