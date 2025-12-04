def field(items, *args):
    assert len(args) > 0

    if len(args) == 1:
        key = args[0]
        for item in items:
            value = item.get(key)
            if value is not None:
                yield value
    else:
        for item in items:
            new_dict = {key: item.get(key) for key in args if item.get(key) is not None}
            if new_dict: 
                yield new_dict

if __name__ == "__main__":
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': None, 'color': 'black'},
        {'title': 'Стол', 'price': 5300, 'color': None},
        {'title': None, 'price': None, 'color': None},
    ]

    print("field(goods, 'title') →")
    for x in field(goods, 'title'):
        print(x)

    print("\nfield(goods, 'title', 'price') →")
    for x in field(goods, 'title', 'price'):
        print(x)
