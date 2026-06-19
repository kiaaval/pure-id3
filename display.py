def summarize(subtree):
    # collapse a subtree onto one line, e.g. "Humidity? (High→No, Normal→Yes)"
    if isinstance(subtree, str):                    # leaf -> just the label
        return subtree
    inner = ", ".join(v + "→" + summarize(child) for v, child in subtree["branches"].items())
    return subtree["feature"] + "? (" + inner + ")"


def print_tree(tree, indent="        "):
    if isinstance(tree, str):                       # whole tree is a single leaf
        print(indent + tree)
        return
    print(indent + tree["feature"] + "?")
    items = list(tree["branches"].items())
    for i, (value, child) in enumerate(items):
        connector = "└── " if i == len(items) - 1 else "├── "
        print(indent + connector + value + " → " + summarize(child))


def ask(name, options):
    while True:
        val = input(f"{name} {options}: ").strip()
        if val in options:
            return val
        print("Invalid, try again.")
