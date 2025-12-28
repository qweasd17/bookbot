def word_count(content):
    return len(content.split())

def char_count(content):
    result = {}
    for letter in content:
        key = letter.lower()
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result

def sort_fn(item):
    return item["num"]

def sort_chars(chars):
    result = []
    for key in chars:
        item = {}
        item["char"] = key
        item["num"] = chars[key]
        result.append(item)
    result.sort(key=sort_fn, reverse=True)
    return result