def sort(width, height, length, mass):
    # Calculate the volume of the package
    volume = width * height * length

    # Determine if the package is bulky or heavy
    bulky = (volume >= 1000000) or (width >= 150 or height >= 150 or length >= 150)
    heavy = (mass >= 20)

    # Determine the stack based on the conditions
    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

# Example usage
if __name__ == "__main__":
    # Test cases
    print(sort(10,100,100,10)) #STANDARD
    print(sort(100, 100, 100, 10))  # SPECIAL
    print(sort(200, 200, 200, 10))  # SPECIAL (bulky)
    print(sort(100, 100, 100, 25))  # REJECTED (both bulky and heavy)
    print(sort(200, 200, 200, 25))  # REJECTED (both bulky and heavy)
