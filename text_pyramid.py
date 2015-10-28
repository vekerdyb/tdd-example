def get_strings(input):
    results = []
    for index in range(len(input)):
        results.append(input[:index + 1])
    for index in range(len(input) - 1, 0, -1):
        results.append(input[:index])
    return results
