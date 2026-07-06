"""Pro"""
def main():
    """Pro func"""
    x = int(input())
    y = int(input())
    a = int(input())
    z = int(input())
    if z < x:
        bill = z * a
    else:
        bill = (z // x) * y * a + (z % x) * a
    print(bill)
main()
