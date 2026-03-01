"""Simple CLI shipping cost calculator with multiple calculation methods."""


def calculate_standard_cost(weight: float, rate: float) -> float:
    """Calculate shipping cost using a basic per-kilogram rate."""
    return weight * rate


def calculate_tiered_cost(weight: float) -> float:
    """Calculate shipping cost using weight-based pricing tiers."""
    if weight <= 1:
        return 5.0
    if weight <= 5:
        return 5.0 + (weight - 1) * 3.5
    return 19.0 + (weight - 5) * 2.75


def main() -> None:
    print("Shipping Cost Calculator")
    print("Choose a calculation method:")
    print("1. Standard (weight × rate)")
    print("2. Tiered (weight brackets)")

    method = input("Enter method number (1 or 2): ").strip()
    weight = float(input("Enter the package weight in kilograms: "))
    date = input("Enter month: ").strip()

    if method == "1":
        rate = float(input("Enter the shipping rate per kilogram: "))
        shipping_cost = calculate_standard_cost(weight, rate)
        method_name = "Standard"
    elif method == "2":
        shipping_cost = calculate_tiered_cost(weight)
        method_name = "Tiered"
    else:
        raise ValueError("Invalid method selected. Please enter 1 or 2.")

    print(
        f"Shipping Cost ({method_name}): {shipping_cost:.2f} USD for this date {date}"
    )


if __name__ == "__main__":
    main()
