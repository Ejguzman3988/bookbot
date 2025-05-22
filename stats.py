def read_file(filepath):
    with open(filepath) as f:
        return f.read()


def get_num_words(filepath):
    contents = read_file(filepath)
    words = contents.split()
    num_words = len(words)
    print(f"Found {num_words} total words")


def get_num_chars(filepath):
    contents = read_file(filepath)
    memo = {}
    for i in range(len(contents)):
        char = contents[i].lower()
        if char in memo:
            memo[char] += 1
        else:
            memo[char] = 1
    return memo


def format_dict(dict):
    list = []
    for key in dict:
        value = dict[key]
        if key.isalpha():
            list.append({"char": key, "num": value})

    def sortFunc(dict):
        return -dict["num"]

    list.sort(key=sortFunc)

    return list


def print_num_chars(filepath):
    num_chars = get_num_chars(filepath)
    formatted = format_dict(num_chars)
    for i in range(len(formatted)):
        print(f"{formatted[i]['char']}: {formatted[i]['num']}")
