def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val < target:
            low = mid + 1
        elif mid_val > target:
            high = mid - 1
        else:
            return mid

    return low


def sort_list(arr):
    return sorted(arr)


def main():
    try:
        input_sequence = input("Введите последовательность чисел через пробел: ")
        user_number = float(input("Введите любое число: "))

        # Преобразование введённой последовательности в список
        numbers = [float(num) for num in input_sequence.split()]

        # Сортировка списка по возрастанию элементов
        sorted_numbers = sort_list(numbers)

        # Устанавливается номер позиции элемента
        position = binary_search(sorted_numbers, user_number)

        if position < len(sorted_numbers):
            # Вывод результата
            print(f"Позиция элемента: {position}")
            print("Элементы списка после сортировки:", sorted_numbers[position:])
        else:
            print("Введенное число больше всех элементов в списке.")

    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите числа в правильном формате.")


if __name__ == "__main__":
    main()
