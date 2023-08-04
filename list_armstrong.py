def is_armstrong(num):
    num_str = str(num)
    power = len(num_str)
    return num == sum(int(digit)**power for digit in num_str)

def list_armstrong_numbers(limit):
    armstrong_numbers = [num for num in range(limit) if is_armstrong(num)]
    return armstrong_numbers

if __name__ == "__main__":
    limit = 1000000
    armstrong_numbers = list_armstrong_numbers(limit)
    print("Armstrong numbers up to", limit, "are:")
    print(armstrong_numbers)
