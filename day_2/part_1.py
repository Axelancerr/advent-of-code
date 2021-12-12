(
    lambda x:
        print(x[0]["forward"] * (x[0]["down"] - x[0]["up"]))
)(
    (
        lambda y:
            (y, [y.__setitem__(command[0], y.__getitem__(command[0]) + int(command[1])) for command in list(map(str.split, open("input.txt").readlines()))])
    )(
        {"up": 0, "down": 0, "forward": 0}
    )
)
