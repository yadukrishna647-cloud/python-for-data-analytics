mark = int(input("Enter your mark: "))
if mark < 50:
    if mark >= 40:
        print("failed")
        print("you may pass with moderation")
    else:
        print("fail")
else:
    print("pass")            