def reverse(strng: str):
    if strng == "":
        return ""
    else:
        char = strng[-1]
        return char + reverse(strng[:-1])

print(reverse("python"))