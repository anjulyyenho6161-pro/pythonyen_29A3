s = input("Nhập một xâu ký tự: ")

# Xâu palindrome đọc từ trái qua phải hay từ phải qua trái đều giống nhau
if s == s[::-1]:
    print(f"'{s}' là một xâu palindrome.")
else:
    print(f"'{s}' không phải là xâu palindrome.")