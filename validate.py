my_conf = {
        'b': True,
        'age': 13,
        'name': 'helloooooooooooooooo',
}
my_struct = {
        'b': {'type': 'bool', 'allowed': [True, False]},
        'age': {'type': 'integer', 'min': 10, 'max': 100},
        'name': {'type': 'string', 'min': 10, 'max': 200},
}


def check_structure(struct, conf):
    for key in struct:
        if key not in conf:
            return False
        if check_type(conf[key]) != struct[key]['type']:
            return False
        if type(conf[key]) is str:
            return struct[key]['max'] >= len(conf[key]) >= struct[key]['min']
        elif type(conf[key]) is int:
            return struct[key]['max'] >= conf[key] >= struct[key]['min']
        elif conf[key] not in struct[key]['allowed']:
            return False
    return True


def check_type(a):
    if type(a) is int:
        return 'integer'
    elif type(a) is str:
        return 'string'
    elif type(a) is bool:
        return 'bool'
    else:
        return None

print(check_structure(my_struct, my_conf))

