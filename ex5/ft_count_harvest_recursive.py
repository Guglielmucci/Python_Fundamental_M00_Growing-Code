def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def _recursive_helper(current_day: int) -> None:
        if current_day > days:
            return
        print(f"Day {current_day}")
        _recursive_helper(current_day + 1)
    _recursive_helper(1)
    print("Harvest Time!")
