def get_obj_or_404(model, param, val):
    found = False
    for obj in model.objects:
        if obj.__getattribute__(param) == val:
            found = True
            break
    if not found:
        raise Exception(f"404 {model.__name__} Not Found")
    return obj