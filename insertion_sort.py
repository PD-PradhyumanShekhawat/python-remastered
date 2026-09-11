def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data


if __name__ == "__main__":
    numbers = [12, 11, 13, 5, 6]

    print("Before:", numbers)

    insertion_sort(numbers)

    print("After:", numbers)