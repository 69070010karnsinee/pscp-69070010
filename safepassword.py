"""safe"""
def main():
    """safe func"""
    letter = input()
    num = int(input())
    if letter + str(num) == "H4567":
        print("safe unlocked")
    elif letter == "H" and num != 4567:
        print("safe locked - change digit")
    elif num == 4567 and letter != "H":
        print("safe locked - change char")
    else:
        print("safe locked")
main()
