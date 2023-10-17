## What is a list method?

In python, lists come with many built-in methods that allow us to search, count, and modify lists. A *list method* is a special kind of function that is executed on a specific list. You've already seen one example of a list method, namely `append()`. Recall that the syntax for using the `append()` method is `your_list.append()`.

For example:
```python
cats_1 = []
cats_2 = []
# append "Tabby" to the cats_1 list:
cats_1.append("Tabby")
# append "Mochi" to the cats_2 list:
cats_2.append("Mochi")
```

In this section we will see several additional methods that apply to lists. Execute each these methods with the syntax `your_list.method_name()`.  We will learn just a subset of the available list methods. The full list can be found at [Python list documentation by w3schools](https://www.w3schools.com/python/python_ref_list.asp) or [Offical python documentation on list methods](https://docs.python.org/3/tutorial/datastructures.html). Here are the list methods you'll learn:
- the `count()` and `index()` methods for counting and searching
- the`insert()` and `extend()` methods for adding elements
- the `pop()` and `remove()` methods and the `del` keyword for removing elements
- the `reverse()` and `sort()` methods and the `sorted()` function for rearranging elements

Here are the details on using these methods.

<ul>
<li> 

`count(x)->int`

The call `your_list.count(x)` takes as a parameter the item to search for. It returns an `int` which gives the number of times that value appears in the list. Here are some example calls to `count()` with the corresponding return values:

```python
values = [81, 59, 42, 65, 72, 42, 42, 81]
values.count(42) # returns 3, since 42 appears 3 times in the list
values.count(23) # returns 0, since 23 does not appear in the list
```
</li>

<li> 

`index(x)->int`

The call `your_list.index(x)` searches for the value `x` in `your_list`. It then returns an `int` which is the *index* of the first time that value appears in the list. One down side of the `index()` method is that `x` must be in the list - if it isn't then a `ValueError` results. Here are some calls to `index()` and the corresponding return values:

```python
values = [81, 59, 42, 65, 72, 42, 42, 81]
values.index(72) # returns 4, since 72 appears at index 4
values.index(42) # returns 2, since 42 first appears at index 2
values.index(90) # results in a ValueError
```
</li>

<li>

`insert(i: int, x)->None`

The call `your_list.insert(i, x)` adds to the list by insertng the value `x` at index `i`. The index `i` should be a valid index for the new value, and the new value will be inserted before the item at that index.
See below how the contents of the list evolves after several calls to `insert()`:

```python
values = [59, 42, 72, 42, 42]
values.insert(0, 81) # list is now [81, 59, 42, 72, 42, 42]
values.insert(3, 65) # list is now [81, 59, 42, 65, 72, 42, 42]
values.insert(7, 21) # list is now [81, 59, 42, 65, 72, 42, 42, 21]
```
Note that `your_list.insert(0, x)` inserts at the front of `your_list`, and `your_list.insert(len(a), x)` is equivalent to `your_list.append(x)`.
</li>

<li>

`extend(another_list)->None`

The call `your_list.extend(another_list)` appends each element in `another_list` to the end of `your_list`. Note that `another_list` is not modified. For example:

```python
values = [81, 59, 42, 65, 72]
values_2 = [42, 42, 21]
# extend the list values by appending all of values_2 at its end
values.extend(values_2)
print(values)   # outputs [81, 59, 42, 65, 72, 42, 42, 21]
print(values_2) # outputs [42, 42, 21], note values_2 is unchanged
```

Notice that in the call `values.extend(values_2)`, the list `values` is changed, but `values_2`, passsed as a parameter, is not modified!
</li>
<li>

`pop()->List_type`

The call `your_list.pop()` removes the *last* element of a list. It returns the value that was stored there. You can alternately pass an integer parameter (`pop(index)->List_type`), which will remove and return the value stored at the index. The program crashes with an `IndexError` if an invalid index is passed. The following example shows how to call `pop()` and looks at the values that are returned.

```python
values = [81, 59, 42, 65, 72, 42, 42, 21]
# Last element 21 is removed from list, saved in variable 'removed':
removed = values.pop()
print(values)  # outputs [81, 59, 42, 65, 72, 42, 42]
print(removed) # outputs 21, the value that was popped
# Removes the element at index 3 (65) and saves it:
removed = values.pop(3)
print(values)  # outputs [81, 59, 42, 72, 42, 42]
print(removed) # outputs 65, the value that was just popped
values.pop(59) # Program crashes with an IndexError, pop index out of range
```

Notice that `your_list.pop()` is identical to `your_list.pop(len(your_list)-1)`
</li>


<li>

`remove(x)->None`

The call `your_list.remove(x)` removes the first occurrence of the value `x` from the list. Notice that it differs from the `pop()` method because you pass the *value* of the item you want to remove, rather than passing the *index*. If the value `x` is not in the list, then the program crashes with a `ValueError`. So check for membership of `x` in the list prior to calling `remove()`.

```python
values = [81, 59, 42, 65, 72, 42, 42, 21]
values.remove(42)   # removes the FIRST occurrence of 42 from the list
print(values)       # outputs [81, 59, 65, 72, 42, 42, 21]
if 2023 in values:  # evaluates to False, avoiding a ValueError on the next line
    values.remove(2023) 
values.remove(1000) # program crashes with ValueError
```
</li>

<li> 

The `del` keyword

This technique for removing elements from a list uses a keyword (`del`) rather than a method. It works similarly to `pop()`, except that it does not return the deleted values, and it can be used more generally to delete a slice of a list.

```python
values = [10, 20, 30, 40, 50, 60, 70]
del values[2]   # removes 30 from the list
print(values)   # outputs [10, 20, 40, 50, 60, 70]
del values[1:4] # removes items at index 1, 2 and 3
print(values)   # outputs [10, 60, 70]
del values[10]  # program crashes with an IndexError
```
</li>

<li>

`reverse()->None`

The call `your_list.reverse()` modifies the list by reversing the order of the elements.

```python
values = [3, 1, 4, 2, 8]
values.reverse()
print(values) # outputs [8, 2, 4, 1, 3]
```

If you want to access the list in reverse order, but not change the list itself, this can be done with a slice.

```python
values = [3, 1, 4, 2, 8]
print(values[::-1])  # outputs [8, 2, 4, 1, 3]
print(values)   # outputs [3, 1, 4, 2, 8], values itself is unchanged
```
Since the slice `values[::-1]` has its stop index and start index missing, we use the default values. The slice includes the entire list, but the step value of `-1` means the list will be traversed in reverse order. Notice that the slice just traverses the list in a different order - the contents of the list itself have not been altered.

</li>

<li>

`sort()->None`

The call `your_list.sort()` *modifies* the list by *sorting the elements from smallest to largest*. If you pass an optional `reverse=True` as a parameter, then the list is sorted in descending order.

```python
values = [3, 1, 4, 2, 8]
# sort the list in increasing order
# The contents of the list itself are modified!
values.sort()
print(values)  # outputs [1, 2, 3, 4, 8]
# Next sort the list in decreasing order
# The contents of the list itself are modified!
values.sort(reverse=True)
print(values)  # outputs [8, 4, 3, 2, 1]
```
</li>

<li>

`sorted(some_list)->list`

The `sorted()` function is *not* a method. Methods are called with the syntax `your_list.method_name()`. But unlike the methods described in this section, `sorted()` is a *function* that you pass your list to as a parameter. It *does not* modify your list! Instead, it builds a new list whose contents are your original list, but sorted. Passing a second parameter `reverse=True` produces a new list that is sorted in descending order.

```python
values = [3, 1, 4, 2, 8]
# produce a sorted copy of the list
# The contents of the list itself are NOT modified!
sorted_ascending = sorted(values)
print(sorted_ascending)  # outputs [1, 2, 3, 4, 8]
print(values) # outputs [3, 1, 4, 2, 8], values has NOT been modified
# produce a sorted copy of the list, descending order
# The contents of the list itself are NOT modified!
sorted_descending = sorted(values, reverse=True)
print(sorted_descending)  # outputs [8, 4, 3, 2, 1]
print(values) # outputs [3, 1, 4, 2, 8], values has NOT been modified
```

</ul>
