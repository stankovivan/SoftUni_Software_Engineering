def rectangle(length, width):
    resul = type(length) == str
    result = type(width) == str
    if resul or result or resul and result:
        return f"Enter valid values!"

    def area():
        return f"Rectangle area: {length * width}"

    def perimeter():
        return f"Rectangle perimeter: {2 * (length + width)}"
    return area() + "\n" + perimeter()


print(rectangle(2, "10"))
