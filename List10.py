def main(list1):
    """
    A list of zeros and ones is given. Find how many ones and how many zeros there are and return to the list form.
    Args:
        list1(list): parameter
    Returns:
        list: return answer
    """
    i = 0
    ls = []
    ls1 = []
    ls2 = []

    while i < len(list1):
        if list1[i] == 1:
            ls1.append(list1[i])
        else:
            if list1[i] == 0:
                ls2.append(list1[i])
        i += 1
    ls.append(len(ls1))
    ls.append(len(ls2))
    return ls

print(main([0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1]))
