def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    s = []
    i = 0
    s.append(fruits.count("apple"))
    while i < len(fruits):
        if fruits[i] == "apple":
            s.append(i)
        i += 1
        return s
print(main(["apple", "banana", "apple", "pear", "apple"]))
