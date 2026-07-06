"""seven"""
def main():
    """seven func"""
    x = int(input())
    a = x % 4
    if not a:
        print("1")
    elif a == 1:
        print("7")
    elif a == 2:
        print("9")
    elif a == 3:
        print("3")
main()
