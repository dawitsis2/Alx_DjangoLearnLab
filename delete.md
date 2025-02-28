# Delete a Book Instance

## Command
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

