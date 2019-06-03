
def binarysearch(search_space, target_value, low, high):
    range_size = (high - low) + 1
    mid = (high + low) // 2

    if target_value == search_space[mid]:
        pos = mid
    elif range_size == 1:
        pos = -1
    else:
        if target_value < search_space[mid]:
            pos = binarysearch(search_space, target_value, low, mid)
        else:
            pos = binarysearch(search_space, target_value, mid+1, high)
    print(pos)
    return pos


def main():
    search_space = []
    x = input("Enter Search Space Value: ")
    for x in range(0, int(x), 1):
        search_space.append(x)
    target_value = input("Enter Target Value: ")

    pos = binarysearch(search_space, int(target_value), 0, len(search_space)-1)

    if pos >= 0:
        print("Found at position %d." % pos)
    else:
        print('Not Found.')


if __name__ == "__main__":
    main()
