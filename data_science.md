# Data Science {#data-science}

Python is becoming an increasingly popular choice for many applications, but in particular it has become one of the standards in the field of Data Science.

Because of its popularity and applicability to this field, let's explore a few fundamental techniques for working with existing datasets and how Python can help make our lives easier!

## Tabular Data

First, let's focus on a common data format known as "tabular data". This just means data that is best represented as a table. A relatable way of thinking about this kind of data might be an Excel spreadsheet that represents a collection of "items" of the same type. Each row represents one "item", and each column is an attribute of that "item":

| **Name** | **Age** | **Favorite Icecream** |
| --- | --- | --- |
| Bob | 24 | Chocolate |
| Alice | 31 | Vanilla |
| John | 48 | Strawberry |

For example, this a sheet of "people", where each row is a "person", and each column is an attribute of that person.

There are many different ways of working with tabular data (storing it, reading it, modifying it, analyzing it) and we're going to focus on one that will let us explore and use the data structures we're already familiar with.

---

## CSV (Comma-Separated Values)

The simplest way of representing a table is to just put it in a text file. Even for this, there are many ways you could choose to do it, but probably the most common way is using comma-separated-values (CSV).

Each row of text will represent one item, where the attributes of that item are separated by commas. Typically, the first row of text in the file will be the names of the columns (attributes):

```
name,age,fav_icecream
Bob,24,chocolate
Alice,31,vanilla
John,48,strawberry
```

Note: sometimes this can be hard to read visually due to the mis-alignment of columns. If you're using VSCode (or something similar) you can install add-ons that color your CSV to make the columns clearer (or add spacing to align them).

Since a .csv file is just a text file, we can read it as we would normally read any text file in Python (with the open() function). But turning that text into other data structures (lists/dictionaries) is so common that Python has a built-in CSV reader!:

```python
import csv

with open('mydata.csv') as csvfile:
    rows = csv.reader(csvfile)
    for r in rows:
        print(r)
        # r is a list of the values
        # [value1, value2, ...]
```

So in one go, we've turned the CSV file full of text into a **list of lists**, containing our data!

NOTE: You can also read files with separators other than a comma:

```python
rows = csv.reader(csvfile, delimiter=';')
```

The CSV format is more general than the specific use-case we're talking about here (tabular data) - it's really just a way of storing lists of values in rows! For the specific use-case of tabular data (i.e. items in rows, with attributes in columns, and a starting row of column names) there's a specific tool that we'll use from the csv module:

```python
with open('mydata.csv') as csvfile:
    # here's the magic step:
    rows = list(csv.DictReader(csvfile))
    for r in rows:
        print(r)
        # r is now a dictionary!
        # { column_name: attribute, ... }
```

So now, we've turned our text (CSV) representation of a table... into a **list of dictionaries**!!! Each dictionary represents one full "Person", with all of their attributes. It looks like this:

```python
[
    { "name": "Bob",
      "age": 24,
      "fav_icecream": "chocolate" },
    { "name": "Alice",
      "age": 31,
      "fav_icecream": "vanilla" },
    { "name": "John",
      "age": 48,
      "fav_icecream": "strawberry"}
]
```