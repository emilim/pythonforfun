def tap(obj):
    return [obj, obj]

obj = {
    'width': 0,
    'height': 0,
    'color': 0
    }

collezione = tap(obj)
collezione[0] = tap(collezione[0])

print(collezione)

