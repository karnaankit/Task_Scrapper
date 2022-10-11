my_conf = {
        'conf_one': 13,
        'conf_two': 'hello',
        'conf_three': False,
}
my_struct = {
        'conf_one': int,
        'conf_two': str,
        'conf_three': bool}
leng = {
            'int_max': 200,
            'int_min': 0,
            'str_max': 2000,
            'str_min': 4,
        }


def check_structure(struct, conf):
    if isinstance(struct, dict) and isinstance(conf, dict):
        return all(k in conf and check_structure(struct[k], conf[k]) for k in struct)
    if isinstance(struct, list) and isinstance(conf, list):
        return all(check_structure(struct[0], c) for c in conf)
    elif isinstance(struct, type):
        return isinstance(conf, struct)
    else:
        return False


def check_length(conf, length):
    if isinstance(conf, dict):
        return all(k in conf and check_length(conf[k], length) for k in conf)
    if isinstance(conf, list):
        return all(check_length(c, length) for c in conf)
    elif isinstance(conf, str):
        return length['str_max'] >= len(conf) >= length['str_min']
    elif isinstance(conf, int):
        return length['int_max'] >= conf >= length['int_min']
    else:
        return False


if check_structure(my_struct, my_conf) and check_length(my_conf, leng):
    print(True)
else:
    print(False)
