def print_movie(*args):
    print(type(args))
    for value in args:
        print(value)

movie = {
    "title": "The Matrix",
    "director": "Wachowski",
    "year": 1999
}

print_movie(*movie.values())

# The Matrix
# Wachowski
# 1999