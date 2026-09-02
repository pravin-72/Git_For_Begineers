from utils.calculator import add_nums , divide_nums,subract_nums,power_nums,multiply_nums


if __name__ == "__main__":
    result = add_nums(5, 10)
    print(f"The sum : {result}")
    print(f"The division : {divide_nums(10, 2)}")
    print(f"The difference : {subract_nums(10, 5)}")
    print(f"The power : {power_nums(2, 3)}")
    print(f"The product : {multiply_nums(5, 10)}")
