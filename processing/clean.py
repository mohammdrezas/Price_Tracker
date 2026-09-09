def clean_price(text):
    digits = ""
    for c in text:
        if c.isdigit():
            digits += c
    result = int(digits)
    return result

def clean_stock(text):
    if text.strip() == "موجود":
        return 1
    else:
        return 0


if __name__ == "__main__":
    print(clean_price("620,000 تومان"))
    print(clean_stock("موجود"))
    print(clean_stock("ناموجود"))