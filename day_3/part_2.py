(
    lambda input_1, input_2:
        (
            lambda x, y:
                print(int(input_1[0], 2) * int(input_2[0], 2))
        )(
            (
                lambda myself:
                    lambda index:
                        myself(myself, index)
            )(
                lambda myself, index:
                    (
                        (
                            lambda most_common:
                                [input_1.remove(b) for b in [binary for binary in input_1 if binary[index] != most_common]]
                        )(
                            (i := __import__("collections").Counter([binary[index] for binary in input_1]).most_common())[0 if i[0][1] > i[1][1] else (0 if i[0][0] == "1" else 1)][0]
                        ),
                        None if len(input_1) == 1 else myself(myself, index + 1)
                    )
            )(
                0
            ),
            (
                lambda myself:
                    lambda index:
                        myself(myself, index)
            )(
                lambda myself, index:
                    (
                        (
                            lambda least_common:
                                [input_2.remove(b) for b in [binary for binary in input_2 if binary[index] != least_common]]
                        )(
                            (i := __import__("collections").Counter([binary[index] for binary in input_2]).most_common())[1 if i[0][1] > i[1][1] else 0 if i[0][0] == "0" else 1][0]
                        ),
                        None if len(input_2) == 1 else myself(myself, index + 1)
                    )
            )(
                0
            ),
        )
)(
    list(map(str.strip, open("input.txt").readlines())),
    list(map(str.strip, open("input.txt").readlines())),
)
