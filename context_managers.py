import contextlib
import random
from typing import Generator, Any


@contextlib.contextmanager
def rand_state(seed: int | None = None) -> Generator:
    state: tuple[Any, ...] = random.getstate()
    random.seed(seed)
    try:
        yield
    finally:
        random.setstate(state)