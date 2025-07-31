# Python - Async

This project covers the basics of asynchronous programming in Python using `async` / `await`, `asyncio`, and coroutines.

## Objectives

By the end of this project, you should be able to:

- Use `async` and `await` syntax
- Run async programs with `asyncio.run()`
- Create and manage multiple coroutines
- Use `asyncio.create_task()` and `asyncio.gather()`
- Measure execution time of async tasks
- Use `random.uniform()` to simulate async delays

##  Tasks Overview

| Task | File | Description |
|------|------|-------------|
| 0 | `0-basic_async_syntax.py` | `wait_random`: waits for a random delay (async) |
| 1 | `1-concurrent_coroutines.py` | `wait_n`: run `wait_random` n times concurrently |
| 2 | `2-measure_runtime.py` | `measure_time`: measure avg runtime of `wait_n` |
| 3 | `3-tasks.py` | `task_wait_random`: wrap `wait_random` as a Task |
| 4 | `4-tasks.py` | `task_wait_n`: like `wait_n` but uses Tasks |

##  Requirements

- Python 3.9
- `pycodestyle` compliant (version 2.5.x)
- All functions must be type-annotated
- Use `asyncio` and `random` modules
- All files must be executable and end with a newline