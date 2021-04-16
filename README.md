# melano

`melano` is JSON utility library

## features
### dict compare

```shell
>>> from melano import diff
>>> x, y = dict(x=1, y=2), dict(x=2, z=1)
>>> diff.compare(x, y)
[{'field': 'x', 'x': 1, 'type': 'MISMATCH', 'y': 2, 'message': 'x: 1 (int) != 2 (int)'}, {'field': 'y', 'x': 2, 'type': 'MISSING', 'message': 'y: not found'}, {'field': 'z', 'y': 1, 'type': 'MISSING', 'message': 'z: not found'}]
```

### list of dict operations
#### sort 

```shell
>>> from melano import sort
>>> items = [dict(x=1, y=5), dict(x=4, y=2), dict(x=2, y=3), dict(x=1, y=2)]
>>> sort(items, 'x', 'y')
[{'x': 1, 'y': 2}, {'x': 1, 'y': 5}, {'x': 2, 'y': 3}, {'x': 4, 'y': 2}]
```

#### group by

```shell
>>> from melano import group_by
>>> items = [dict(x=1, y=5, z=5), dict(x=4, y=2, z=3), dict(x=4, y=2, z=10)]
>>> group_by(items, 'x', 'y')
[{'x': 1, 'y': 5, 'items': [{'x': 1, 'y': 5, 'z': 5}]}, {'x': 4, 'y': 2, 'items': [{'x': 4, 'y': 2, 'z': 3}, {'x': 4, 'y': 2, 'z': 10}]}]
```

#### count

```shell
>>> from melano import count
>>> items = [dict(x=1, y=5, z=5), dict(x=4, y=2, z=3), dict(x=4, y=2, z=10)]
>>> count(items, 'x', 'y')
[{'x': 1, 'y': 5, 'count': 1}, {'x': 4, 'y': 2, 'count': 2}]
```