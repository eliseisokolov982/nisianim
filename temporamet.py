from typing import Any, Awaitable, Union

def process_value(value: Union[int, str]) -> Any:
    if isinstance(value, int):
        return value * 2
    elif isinstance(value, str):
        return value.upper()
    else:
        return None

async def async_task() -> Awaitable[int]:
    return 42

result = process_value(10)
print(result)  # Output: 20

result = process_value("hello")
print(result)  # Output: "HELLO"

result = process_value(3.14)
print(result)  # Output: None

awaitable_result = await async_task()
print(awaitable_result)  # Output: 42
