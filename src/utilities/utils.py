
def get_name_from_locator(locator):
    if '"' in locator:
        start = locator.find('"') + 1
        end = locator.rfind('"')
        return locator[start:end]
    elif '=' in locator:
        start = locator.find('=') + 1
        end = locator.find(']')
        return locator[start:end]
    else:
        return locator
