(
    lambda x:
        print(x[0]["forward"] * (x[0]["down"] - x[0]["up"]))
)(
    (
        commands := {"up": 0, "down": 0, "forward": 0},
        [
            commands.__setitem__(
                command,
                commands[command] + int(amount)
            ) for command, amount in list(map(str.split, open("input.txt").readlines()))
        ]
    )
)
