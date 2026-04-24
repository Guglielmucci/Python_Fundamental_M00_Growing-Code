def ft_seed_inventory(seed: str, quantity: int, unit: str) -> None:
    capitalize_seed = seed.capitalize()
    if unit == "packets":
        print(f"{capitalize_seed} seed: {quantity} packets avaible")
    elif unit == "grams":
        print(f"{capitalize_seed} seed: {quantity} grams total")
    elif unit == "area":
        print(f"{capitalize_seed} seed: cover {quantity} square meters ")
    else:
        print("Unknown unit type")
