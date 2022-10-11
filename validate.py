my_conf = {
        'age': 13,
        'b': True,
        'name': 'hellooooooooooooooooo',
}
my_struct = {
        'age': {'type': int, 'allowed': range(1, 100)},
        'b': {'type': bool, 'allowed': [True, False]},
        'name': {'type': str, 'min': 10, 'max': 200},
}


def check_structure(struct, conf):
    for key in struct:
        if type(conf[key]) != struct[key]['type']:
            return False
        if type(conf[key]) is str:
            return struct[key]['max'] >= len(conf[key]) >= struct[key]['min']
        elif conf[key] not in struct[key]['allowed']:
            return False
    return True


print(check_structure(my_struct, my_conf))

