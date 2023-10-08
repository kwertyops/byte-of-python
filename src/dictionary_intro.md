## What is a dictionary?

A dictionary in python is much like the familiar idea of a dictionary: each word is paired with its meanings. You look up the meanings based on the word, but you cannot search for the word based on a meaning. We think of the word as the *key* and the list of meanings as the associated *value*. Each key is unique (it appears only once in the dictionary). Associated values are allowed to be duplicated. We say a dictionary *maps* or *associates* a key with a value. That's why in Computer Science dictionaries are also called *maps*.

## Examples of appplications of a python dictionaries

- A University system stores students records. Each student record is identified with their unique student ID. Two students might have the same name, but never the same ID. The student ID is the *key*, and the associated value is the entire student record, including personal information and transcript. The system allows searching, adding new students, modifying the contents of their record, or removing former students. In all cases, the student record is accessed using the key (the student ID).

- The Social Security Administration keeps records for all taxpayers. The unique social security numbers for each person are used as the keys to access their associated tax records. No two people can ever have the same Social Security Number. Typical actions are to add new people, and to access and modify their records. All actions use the SSN as the key to find their associated tax records.

- An airline stores reservations records. Each reservation is stored under a unique confirmation code (typically they look something like `PQ56SRV`). The data is all stored with these unique confirmation code as the keys, with the information about the reservation as the associated value. We must be able to access, add, remove and modify reseration records.

## Key features of dictionaries

- An *item* in a dictionary consists of a pair: a unique *key* (student ID, SSN, airline confirmation code) and its associated *value* (transcript, tax records, reservation information).

- The dictionary itself is a collection of items.

- We must be able to search for, add, remove, and modify items. These operations need to be done quickly and efficiently.