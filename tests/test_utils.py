import nose
from melano.utils import (sort, group_by, count)


def test_utils_sort_single_key():
    items = [dict(x=1), dict(x=4), dict(x=2)]
    sorted_items = sort(items, 'x')
    nose.tools.assert_list_equal(sorted_items, [dict(x=1), dict(x=2), dict(x=4)])


def test_utils_sort_multiple_keys():
    items = [dict(x=1, y=5), dict(x=4, y=2), dict(x=2, y=3), dict(x=1, y=2)]
    sorted_items = sort(items, 'x', 'y')
    nose.tools.assert_list_equal(sorted_items, [dict(x=1, y=2), dict(x=1, y=5), dict(x=2, y=3), dict(x=4, y=2)])


def test_utils_group_by_single_key():
    items = [dict(x=1, y=5), dict(x=4, y=2), dict(x=2, y=3), dict(x=1, y=2)]
    expected = [
        {'items': [{'x': 1, 'y': 5}, {'x': 1, 'y': 2}], 'x': 1},
        {'items': [{'x': 2, 'y': 3}], 'x': 2},
        {'items': [{'x': 4, 'y': 2}], 'x': 4}
    ]
    group_items = group_by(items, 'x')
    nose.tools.assert_list_equal(group_items, expected)


def test_utils_group_by_multiple_keys():

    items = [dict(x=1, y=5), dict(x=4, y=2), dict(x=2, y=3), dict(x=1, y=2)]
    expected = [
        {'items': [{'x': 1, 'y': 2}], 'x': 1, 'y': 2},
        {'items': [{'x': 1, 'y': 5}], 'x': 1, 'y': 5},
        {'items': [{'x': 2, 'y': 3}], 'x': 2, 'y': 3},
        {'items': [{'x': 4, 'y': 2}], 'x': 4, 'y': 2}
    ]
    group_items = group_by(items, 'x', 'y')
    nose.tools.assert_list_equal(group_items, expected)


def test_utils_count_single_key():
    items = [dict(x=1, y=5), dict(x=4, y=2), dict(x=2, y=3), dict(x=1, y=2)]
    expected = [
        {'count': 2, 'x': 1},
        {'count': 1, 'x': 2},
        {'count': 1, 'x': 4}
    ]
    group_items = count(items, 'x')
    nose.tools.assert_list_equal(group_items, expected)
