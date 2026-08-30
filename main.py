from utils.calculator import add_nums , divide_nums,subract_nums,power_nums


if __name__ == "__main__":
    result = add_nums(5, 10)
    print(f"The sum is: {result}")
    print(f"The division is: {divide_nums(10, 2)}")
    print(f"The difference is: {subract_nums(10, 5)}")
    print(f"The power is: {power_nums(2, 3)}")