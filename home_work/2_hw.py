def task_1() -> list:
    a: int = 15
    b: float = 3.14
    c: str = 'строка'
    d: list = [1, 2, 'список']
    e: bool = True
    return a, type(a), b, type(b), c, type(c), d, type(d), e, type(e)

print(task_1())


def task_2() -> str:
    a = [1, 2, 3, 5, 8, 13, 21]
    return a[0:3]

print(task_2())


def task_3() -> int:
    a: int = 25
    return a**2

print(task_3())