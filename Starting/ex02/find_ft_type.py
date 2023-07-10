def all_thing_is_obj(object: any) -> int:
    if isinstance(object, list):
        print("List : {}".format(type(object)))
    elif isinstance(object, tuple):
        print("Tuple : {}".format(type(object)))
    elif isinstance(object, set):
        print("Set : {}".format(type(object)))
    elif isinstance(object, dict):
        print("Dict : {}".format(type(object)))
    elif isinstance(object, str):
        print("{} is in the kitchen : {}".format(object, type(object)))
    else:
        print("Type not found")
    return 42