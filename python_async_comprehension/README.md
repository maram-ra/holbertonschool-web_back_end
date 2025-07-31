# Python - Async Comprehension

This project focuses on asynchronous generators and comprehensions in Python. You'll explore how to create async generators, use `async for` inside comprehensions, and execute async operations concurrently using `asyncio`.

---

##  Learning Objectives

By the end of this project, you should be able to:

- Define an **asynchronous generator** using `async def` and `yield`
- Use `async for` inside **list comprehensions**
- Run multiple async operations concurrently with `asyncio.gather`
- Type-annotate async generators and coroutines properly

---

##  Tasks Overview

| Task | File | Description |
|------|------|-------------|
| 0 | `0-async_generator.py` | Create an async generator that yields 10 random numbers with a 1-second delay |
| 1 | `1-async_comprehension.py` | Use an async comprehension to collect values from the generator |
| 2 | `2-measure_runtime.py` | Run four async comprehensions in parallel and measure total execution time |

---

## 🛠 Requirements

- Python 3.9 on Ubuntu 20.04 LTS
- Files must pass `pycodestyle` (version 2.5.x)
- All coroutines must be **type-annotated**
- All modules and functions must include **real sentence docstrings**
- All files must be executable and end with a newline

---

