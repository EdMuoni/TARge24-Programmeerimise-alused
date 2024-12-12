def triangle_area(a, h):
    return a * h / 2


s = triangle_area(10, 10)
print(s)


def hello():
    print("Hello World")


def hello_name(name):
    print(f"Hello {name}")


hello()
hello_name("World")

nums = [1, 3, 14, 27, 15, 100, 151, 9, 2]
mapped = map(lambda x: x * 2, nums)
print(list(mapped))  # [2, 6, 28, 54, 30, 200, 302, 18, 4]
