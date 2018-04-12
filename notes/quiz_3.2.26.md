# Notes on Quiz 3.2.26

**Quiz: Transpose with Zip**

Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix. There's actually a cool trick for this! Feel free to look at the solutions if you can't figure it out.

```python
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = # replace with your code
print(data_transpose)
```

**Solution: Transpose with Zip**

```python
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)
```

First let's consider `zip`. It takes two or more iterables (lists, sets, dicts, etc) as arguments. When you iterate through `zip`, it returns the first element in each iterable as a tuple, then the second element in each iterable as a tuple, and so on. Calling `tuple(zip(...))` automatically iterates through `zip` and builds the tuple. Then what we want is something that looks like:

```python
zip((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
```

where each of the tuples is one argument to `zip`. This will return tuples `(0, 3, 6, 9)`, `(1, 4, 7, 10)`, and `(2, 5, 8, 11)`.

We can brute force this

```python
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(data[0], data[1], data[2], data[3]))
```

We can also do it in a nicer way using *unpacking*. If you write `*data` in the function argument, it will unpack each element in `data` and pass each of the elements as an argument to the function. So, `zip(*data)` is a shorter way to write `zip(data[0], data[1], data[2], data[3])`. However the second option only works if `data` has 4 elements, while `zip(*data)` will work regardless of the length of `data`.

So then, the general way to do this which works with any size tuple similar to `data` is

```python
tuple(zip(*data))
```