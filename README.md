# Asuna
A package with useful fucntions to help Hajime.

```shell
python -m pip install -U git+https://github.com/Hajime8673/Asuna
```

```py
from Asuna import Context

ctx = Context({'asuna': 10})
print(ctx.asuna)  # Output: 10
print(ctx.sakura)  # Output: None

ctx = Context({'asuna': 10}, default=0, miyuki=5)
print(ctx.asuna)  # Output: 10
print(ctx.sakura)  # Output: 0
print(ctx.miyuki)  # Output: 5
```

```py
from Asuna import Chunker

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunk_size = 3
result = Chunker.chunk(my_list, chunk_size)
print(result) # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8]
list3 = [9, 10, 11, 12]
result = Chunker.multi_chunk(list1, list2, list3, chunk_size=3, default_value=0)
print(result) # Output: [[1, 6, 9], [2, 7, 10], [3, 8, 11], [4, 0, 12], [5, 0, 0]]
```

#### Note: Not meant for any production environment, please refrain from using in production.
