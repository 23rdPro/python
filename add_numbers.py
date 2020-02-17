def digital_root(number: int):
    sum_digits = 0
    for digit in str(number):
        sum_digits += int(digit)
    if len(str(sum_digits)) > 1:
        final_sum = sum(int(all_digits) for all_digits in str(sum_digits))
        return final_sum
    return sum_digits


def digital_root_2(number: int):
    sum_number = sum(int(digit) for digit in str(number))
    if len(str(sum_number)) > 1:
        final_sum = sum(int(num) for num in str(sum_number))
        return final_sum
    return sum_number


nums = digital_root_2(132189)
print(nums)
