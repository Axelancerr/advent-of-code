(
    lambda x:
        (
            lambda y:
                print(int("".join(y[0]), 2) * int("".join(y[1]), 2))
        )(
            [
                [__import__("collections").Counter([j[i] for j in x]).most_common()[0][0] for i in range(12)],
                [__import__("collections").Counter([j[i] for j in x]).most_common()[-1][0] for i in range(12)],
            ]
        )
)(
    list(map(list, map(str.strip, open("input.txt").readlines())))
)
