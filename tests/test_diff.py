import nose
from melano.diff import (json_diff, list_diff)


def test_diff_json_simple_equal():
    errors = json_diff(x=dict(x=1, y=2, z=3), y=dict(x=1, y=2, z=3))
    nose.tools.assert_equal(len(errors), 0)


def test_diff_json_simple_not_equal():
    errors = json_diff(x=dict(a=1, b=1, c=3), y=dict(a=1, b=2, c=3))
    nose.tools.assert_equal(len(errors), 1)
    nose.tools.assert_equal(errors[0]['type'], 'MISMATCH')
    nose.tools.assert_equal(errors[0]['field'], 'b')
    nose.tools.assert_equal(errors[0]['x'], 1)
    nose.tools.assert_equal(errors[0]['y'], 2)
    nose.tools.assert_equal(errors[0]['message'], 'b: 1 (int) != 2 (int)')


def test_diff_json_simple_missing_x():
    errors = json_diff(x=dict(a=1, b=2), y=dict(a=1, b=2, c=3))
    nose.tools.assert_equal(len(errors), 1)
    nose.tools.assert_equal(errors[0]['type'], 'MISSING')
    nose.tools.assert_equal(errors[0]['field'], 'c')
    nose.tools.assert_equal(errors[0]['y'], 3)
    nose.tools.assert_equal(errors[0]['message'], 'c: not found')


def test_diff_json_simple_missing_y():
    errors = json_diff(x=dict(a=1, b=2, c=3), y=dict(a=1, b=2))
    nose.tools.assert_equal(len(errors), 1)
    nose.tools.assert_equal(errors[0]['type'], 'MISSING')
    nose.tools.assert_equal(errors[0]['field'], 'c')
    nose.tools.assert_equal(errors[0]['x'], 3)
    nose.tools.assert_equal(errors[0]['message'], 'c: not found')


def test_diff_list_simple_missing_y():
    errors = list_diff(x=[1, 2, 3], y=[1, 2])
    nose.tools.assert_equal(len(errors), 1)
    nose.tools.assert_equal(errors[0]['type'], 'MISSING')
    nose.tools.assert_equal(errors[0]['x'], 3)
    nose.tools.assert_equal(errors[0]['message'], '[2]: not found')


def test_diff_list_simple_mismatch():
    errors = list_diff(x=[1, 3], y=[1, 2])
    nose.tools.assert_equal(len(errors), 1)
    nose.tools.assert_equal(errors[0]['type'], 'MISMATCH')
    nose.tools.assert_equal(errors[0]['x'], 3)
    nose.tools.assert_equal(errors[0]['y'], 2)
    nose.tools.assert_equal(errors[0]['message'], '[1]: 3 (int) != 2 (int)')


def test_diff_json_nested_missing_field():
    x = dict(name='john', age=22, address=dict(address1='20 XYZ', state='CA'), phone_numbers=[123456, 345678])
    y = dict(name='john', age=22, address=dict(address1='20 XYZ'), phone_numbers=[123456, 345678])
    errors = json_diff(x, y)
    nose.tools.assert_equal(len(errors), 1)
    nose.tools.assert_equal(errors[0]['type'], 'MISSING')
    nose.tools.assert_equal(errors[0]['field'], 'address.state')
    nose.tools.assert_equal(errors[0]['x'], 'CA')
    nose.tools.assert_equal(errors[0]['message'], 'address.state: not found')


def test_diff_json_nested_mismatch_value():
    x = dict(name='john', age=22, address=dict(address1='20 XYZ', state='CA'), phone_numbers=[123456, 345678])
    y = dict(name='john', age=22, address=dict(address1='20 XYZ', state='PA'), phone_numbers=[123456, 345678])
    errors = json_diff(x, y)
    nose.tools.assert_equal(len(errors), 1)
    nose.tools.assert_equal(errors[0]['type'], 'MISMATCH')
    nose.tools.assert_equal(errors[0]['field'], 'address.state')
    nose.tools.assert_equal(errors[0]['x'], 'CA')
    nose.tools.assert_equal(errors[0]['y'], 'PA')
    nose.tools.assert_equal(errors[0]['message'], 'address.state: CA (str) != PA (str)')


def test_diff_json_nested_dict_list_mismatch():
    x = dict(name='john', age=22, addresses=[dict(address1='20 XYZ', state='CA')])
    y = dict(name='john', age=22, addresses=[dict(address1='20 XYZ', state='PA')])
    errors = json_diff(x, y)
    nose.tools.assert_equal(len(errors), 1)
    nose.tools.assert_equal(errors[0]['type'], 'MISMATCH')
    nose.tools.assert_equal(errors[0]['field'], 'addresses[0].state')
    nose.tools.assert_equal(errors[0]['x'], 'CA')
    nose.tools.assert_equal(errors[0]['y'], 'PA')
    nose.tools.assert_equal(errors[0]['message'], 'addresses[0].state: CA (str) != PA (str)')


def test_diff_json_nested_dict_list_missing_x():
    x = dict(name='john', age=22, addresses=[dict(address1='20 XYZ', state='CA')])
    y = dict(name='john', age=22, addresses=[])
    errors = json_diff(x, y)
    nose.tools.assert_equal(len(errors), 1)
    nose.tools.assert_equal(errors[0]['type'], 'MISSING')
    nose.tools.assert_equal(errors[0]['field'], 'addresses[0]')
    nose.tools.assert_equal(errors[0]['x'], dict(address1='20 XYZ', state='CA'))
    nose.tools.assert_equal(errors[0]['message'], 'addresses[0]: not found')


def test_diff_json_nested_dict_list_missing_y():
    x = dict(name='john', age=22, addresses=[dict(address1='20 XYZ', state='CA')])
    y = dict(name='john', age=22, addresses=[dict(address1='20 XYZ', state='CA'), dict(address1='10 XYZ', state='PA')])
    errors = json_diff(x, y)
    nose.tools.assert_equal(len(errors), 1)
    nose.tools.assert_equal(errors[0]['type'], 'MISSING')
    nose.tools.assert_equal(errors[0]['field'], 'addresses[1]')
    nose.tools.assert_equal(errors[0]['y'], dict(address1='10 XYZ', state='PA'))
    nose.tools.assert_equal(errors[0]['message'], 'addresses[1]: not found')

