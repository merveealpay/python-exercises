def edit_str():
    inp = input("write a string: ")
    inp = " ".join(inp.split()).capitalize()

    if inp.count("?") > 1:
        inp = inp.strip("?")
        inp = inp + "?"
    elif "?" not in inp:
        inp = inp + "?"

    return inp

print(edit_str())
