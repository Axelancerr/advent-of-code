(
    lambda x:
        print(x[0]["horizontal"] * x[0]["depth"])
)(
    (
        lambda y:
            (
                y,
                [
                    (
                        y.__setitem__("horizontal", y["horizontal"] + int(command[1])),
                        y.__setitem__("depth", y["depth"] + (y["aim"] * int(command[1])))
                    ) if command[0] == "forward"
                    else (y.__setitem__("aim", y["aim"] + int(command[1]))) if command[0] == "down"
                    else (y.__setitem__("aim", y["aim"] - int(command[1]))) if command[0] == "up" else None
                    for command in list(map(str.split, open("input.txt").readlines()))
                ]
            )
    )(
        {"aim": 0, "horizontal": 0, "depth": 0}
    )
)
