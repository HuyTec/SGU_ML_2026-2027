```
python -m pip show numpy
------------------------------------------------
# Thiet lap ban dau

git config --global user.name "Ten Cua Ban"

git config --global user.email "email@example.com"
------------------------------------------------
#Kiem tra trang thái
git status

git status -sb
------------------------------------------------
# Xem thay doi
git diff

git log --oneline --graph --decorate
------------------------------------------------
# Add
git add .

git add tenfile

git add -u
-------------------------------------------------
# Commit:

git commit -m "Update notes"

git commit -am "Quick update"
-------------------------------------------------
# Push: đẩy lên

git push

git push origin main

-------------------------------------------------
# Pull: kéo về

git pull

git pull origin main

-------------------------------------------------
# Chia nhanh:

git branch
-------------------------------------------------
# Restore:

git restore --staged NOTES.md

git restore NOTES.md

# Reset:

git reset --hard HEAD~1
_________________________________________________

# activate moi truong ao: ai_practice_py312

conda activate ai_practice_py312

--------------------------------------------------

# thoat moi truong ao:

conda deactivate

--------------------------------------------------

# Tắt mặc định env base
conda config --set auto_activate_base false
```
# CHEAT SHEET
```
from dataclasses import dataclass
from typing import List, Optional, Any
from functools import lru_cache
from contextlib import contextmanager
import time
```
# -----------------------------
# CONFIG + UNPACKING
# -----------------------------
```
DEFAULT_CONFIG = {"lr": 0.01, "epochs": 100}
EXTRA_CONFIG = {"batch_size": 32}
CONFIG = {**DEFAULT_CONFIG, **EXTRA_CONFIG}
```

# -----------------------------
# CONTEXT MANAGER
# -----------------------------
```
@contextmanager
def timer(name: str):
    start = time.time()
    yield
    print(f"[{name}] time = {time.time() - start:.4f}s")
```

# -----------------------------
# DATACLASS + __slots__
# -----------------------------
```
@dataclass(slots=True)
class Point:
    x: float
    y: float
```

# -----------------------------
# GENERATOR
# -----------------------------
```
def squares(n: int):
    for i in range(n):
        yield i * i
```

# -----------------------------
# FUNCTION UTILITIES
# -----------------------------
```
def mean(values: List[float], /, *, default: Optional[float] = None) -> float:
    if not values:
        if default is None:
            raise ValueError("Empty list")
        return default
    return sum(values) / len(values)


def flexible_func(*args: Any, **kwargs: Any) -> None:
    print("args:", args)
    print("kwargs:", kwargs)
```

# -----------------------------
# DECORATOR
# -----------------------------
```
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```
```
@log_call
def add(a: int, b: int) -> int:
    return a + b
```

# -----------------------------
# WALRUS OPERATOR
# -----------------------------
```
def check_length(arr: list[int]) -> None:
    if (n := len(arr)) > 5:
        print(f"Long list: {n}")
    else:
        print("Short list")
```

# -----------------------------
# CACHING (AI / ALGO STYLE)
# -----------------------------
```
@lru_cache
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

# -----------------------------
# CALLABLE OBJECT
# -----------------------------
```
class Model:
    def __call__(self, x: float) -> float:
        return x * CONFIG["lr"]
```
# OS Absolute Path
```
base = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(base, "filename")
```