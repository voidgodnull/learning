def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)





def reverse_string(s):
    # Base Case: Empty string or single character string
    if len(s) <= 1:
        return s
    # Recursive Step: Take the first character, reverse the rest, then append the first char
    else:
        return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))  # Output: olleh
print(reverse_string("python")) # Output: nohtyp
print(reverse_string("a"))      # Output: a
print(reverse_string(""))       # Output:





def deep_sum(nested_list):
    total = 0
    for item in nested_list:
        if isinstance(item, list):
            total += deep_sum(item)  # Recursive call for nested lists
        else:
            total += item            # Add the number
    return total

my_list1 = [1, 2, [3, 4], 5]
my_list2 = [1, [2, [3, 4]], 5, [6]]
my_list3 = [1, [2, [3, [4, [5]]]]]

print(deep_sum(my_list1)) # Output: 15
print(deep_sum(my_list2)) # Output: 21
print(deep_sum(my_list3)) # Output: 15
