import unittest

from final_kr.task_1.triangle import Triangle
from test_data.test_triangle_data import TestTriangleData


EPS = 0.001


class TestTriangle(unittest.TestCase):
    @staticmethod
    def _equals_float(x, y):
        return abs(x - y) < EPS

    def test_check_if_exist_positive(self):
        for a, b, c in TestTriangleData.test_if_exists_positive:
            try:
                Triangle(a, b, c)
            except ValueError:
                self.fail("Triangle exists, but class calculates otherwise")

    def test_check_if_exist_negative(self):
        for a, b, c in TestTriangleData.test_if_exists_negative:
            try:
                Triangle(a, b, c)
                self.fail("Triangle does not exist, but class calculates otherwise")
            except ValueError:
                pass

    def test_perimetr(self):
        for correct_p, a, b, c in TestTriangleData.test_perimetr_data:
            tri = Triangle(a, b, c)
            assert self._equals_float(correct_p, tri.perimetr()), (f"Incorrect perimetr calculation for tringle with "
                                                                   f"sides ({a}, {b}, {c}) and perimetr {correct_p} != "
                                                                   f"{tri.perimetr()} returned from tri.perimetr()")

    def test_square(self):
        for correct_s, a, b, c in TestTriangleData.test_square_data:
            tri = Triangle(a, b, c)
            assert self._equals_float(correct_s, tri.square()), (f"Incorrect perimetr calculation for tringle with "
                                                                 f"sides ({a}, {b}, {c}) and perimetr {correct_s} != "
                                                                 f"{tri.square()} returned from tri.perimetr()")

    def test_equal(self):
        for t1, t2 in TestTriangleData.test_eq_data:
            assert t1 == t2, (f"Class must return True when comparing triangles "
                              f"Triangle({t1.a, t1.b, t1.c}) and Triangle({t2.a, t2.b, t2.c})")

    def test_not_equal(self):
        for t1, t2 in TestTriangleData.test_not_eq_data:
            assert t1 != t2, (f"Class must return True when comparing triangles "
                              f"Triangle({t1.a, t1.b, t1.c}) and Triangle({t2.a, t2.b, t2.c})")

    def test_less_than(self):
        for t1, t2 in TestTriangleData.test_less_than_data:
            assert t1 < t2, f"Triangle({t1.a, t1.b, t1.c}) must be less than Triangle({t2.a, t2.b, t2.c})"

    def test_greater_than(self):
        for t1, t2 in TestTriangleData.test_greater_than_data:
            assert t1 > t2, f"Triangle({t1.a, t1.b, t1.c}) must be greater than Triangle({t2.a, t2.b, t2.c})"

    def test_less_than_or_equal(self):
        for t1, t2 in TestTriangleData.test_less_than_or_equal_data:
            assert t1 <= t2, f"Triangle({t1.a, t1.b, t1.c}) must be less than or equal Triangle({t2.a, t2.b, t2.c})"

    def test_greater_than_or_equal(self):
        for t1, t2 in TestTriangleData.test_greater_than_or_equal_data:
            assert t1 >= t2, f"Triangle({t1.a, t1.b, t1.c}) must be greater than or equal Triangle({t2.a, t2.b, t2.c})"

    def test_mul(self):
        for a, b, c, const in TestTriangleData.test_mul_data:
            t1 = Triangle(a, b, c)
            t1 * 2
            assert (t1 == Triangle(a*const, b*const, c*const),
                    f"Triangle({a}, {b}, {c}) is incorrectly multiplied by const = {const}")

    # Method name in class is "equal", but it checks if triangles are similar, hence the name of the test method
    def test_similar_triangle(self):
        for t1, t2, similar in TestTriangleData.test_similar_triangle_data:
            assert t1.equal(t2) == t2.equal(t1) == similar, \
                f"Method 'equal' must return {similar}, but returns {not similar} instead."

    def test_is_right_angled(self):
        for t, is_right_angled in TestTriangleData.test_is_right_triangle_data:
            assert t.is_right_angled() == is_right_angled, \
                f"Triangle({t.a}, {t.b}, {t.c}).is_right_angled() must return {is_right_angled}."

    def test_is_right(self):
        for t, is_right in TestTriangleData.test_is_right_data:
            assert t.is_right_triangle() == is_right, \
                f"Triangle({t.a}, {t.b}, {t.c}).is_right_triangle() must return {is_right}."

    def test_two_sides_eq(self):
        for t, two_sides_eq in TestTriangleData.two_sides_eq_data:
            assert t.two_sides_eq() == two_sides_eq, \
                f"Triangle({t.a}, {t.b}, {t.c}).two_sides_eq() must return {two_sides_eq}."

    def test_del(self):
        for t in TestTriangleData.test_del_data:
            try:
                del t
                t
                self.fail(f"__del__ failed for Triangle({t.a}, {t.b}, {t.c}).")
            except UnboundLocalError:
                pass
