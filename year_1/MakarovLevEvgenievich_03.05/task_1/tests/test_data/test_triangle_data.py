from final_kr.task_1.triangle import Triangle


class TestTriangleData:
    # Each test case given in the format of (a, b, c)
    test_if_exists_positive = [
        (1, 1, 1),
        (1, 2, 2)
    ]

    # Each test case given in the format of (a, b, c)
    test_if_exists_negative = [
        (1, 2, 3),
        (2, 2, 5)
    ]

    # Each test case given in the format of (perimetr, a, b, c)
    test_perimetr_data = [
        (3, 1, 1, 1),
        (5, 1, 2, 2),
        (11, 2, 4, 5),
        (1.5, 0.5, 0.5, 0.5)
    ]

    # Each test case given in the format of (square, a, b, c)
    test_square_data = [
        (2, 2, 2, 2 * 2**0.5),
        (3**0.5 / 4, 1, 1, 1)
    ]

    # Each test case given in the format of (triangle_1: Triangle, triangle_2: Triangle)
    test_eq_data = [
        (Triangle(1, 2, 2), Triangle(2, 2, 1))
    ]

    # Each test case given in the format of (triangle_1: Triangle, triangle_2: Triangle)
    test_not_eq_data = [
        (Triangle(1, 2, 2), Triangle(2, 2, 2))
    ]

    # Each test case given in the format of (triangle_1: Triangle, triangle_2: Triangle)
    # where ttriangle_1 is less than triangle_2
    test_less_than_data = [
        (Triangle(1, 2, 2), Triangle(2, 2, 2))
    ]

    # Each test case given in the format of (triangle_1: Triangle, triangle_2: Triangle)
    # where ttriangle_1 is greater than triangle_2
    test_greater_than_data = [
        (Triangle(3, 2, 2), Triangle(1, 2, 2))
    ]

    # Each test case given in the format of (triangle_1: Triangle, triangle_2: Triangle)
    # where ttriangle_1 is less than or equal triangle_2
    test_less_than_or_equal_data = [
        (Triangle(1, 2, 2), Triangle(2, 2, 2)),
        (Triangle(1, 2, 2), Triangle(2, 2, 1))
    ]

    # Each test case given in the format of (triangle_1: Triangle, triangle_2: Triangle)
    # where ttriangle_1 is greater than or equal triangle_2
    test_greater_than_or_equal_data = [
        (Triangle(1, 2, 2), Triangle(2, 2, 1)),
        (Triangle(3, 2, 2), Triangle(1, 2, 2))
    ]

    # Each test case given in the format of (a, b, c, const)
    test_mul_data = [
        (1, 1, 1, 2)
    ]

    # Each test case given in the format of (triangle_1: Triangle, triangle_2: Triangle, similar: bool)
    test_similar_triangle_data = [
        (Triangle(1, 1, 1), Triangle(2, 2, 2), True)
    ]

    # Each test case given in the format of (triangle_1: Triangle, is_right_triangle: bool)
    test_is_right_triangle_data = [
        (Triangle(3, 4, 5), True),
        (Triangle(1, 1, 1), False)
    ]

    # Each test case given in the format of (triangle_1: Triangle, is_right_triangle: bool)
    test_is_right_data = [
        (Triangle(1, 1, 1), True)
    ]

    # Each test case given in the format of (triangle_1: Triangle, is_right_triangle: bool)
    two_sides_eq_data = [
        (Triangle(1, 1, 1), True),
        (Triangle(1, 2, 2), True)
    ]

    # Each test case given in the format of (triangle_1: Triangle)
    test_del_data = [
        Triangle(1, 1, 1)
    ]
