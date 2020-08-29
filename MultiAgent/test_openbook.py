
import openbook

book = openbook.build_table(10)

assert len(book) > 0, "Your opening book is empty"

assert all(isinstance(k, tuple) for k in book), "All the keys should be `hashable`"
assert all(isinstance(v, tuple) and len(v) == 2 for v in book.values()), \
    "All the values should be tuples of (x, y) actions"

print("Looks like your book worked!")
print(book)