def kir_info(a):
    return f"your kir is {a} cm | you are {kir_size(a)}"

def kir_size(kir):
    if kir < 8:
        return "baby"
    elif 8 < kir < 13:
        return "teanager"
    elif 13 < kir < 22:
        return "Man"
    else:
        return "God"