# Asuna
A package with useful fucntions to help Hajime.


## Note: Not meant for any production environment, please refrain from using in production.


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
