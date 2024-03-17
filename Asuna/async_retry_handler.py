import asyncio
from typing import Callable, Any, Union


class AsyncRetryHandler:
    def __init__(self, on_error=True, on_match=[], on_unmatch=[], on_type_match=[], on_type_unmatch=[],
                 retries=3, retry_delay=0.0, delay_multiply=0, handler=None):
        """
        Initializes AsyncRetryHandler class with specified parameters.

        Args:
            on_error (bool): Whether to retry on error. Default is True.
            on_match (list): List of expected return values to retry.
            on_unmatch (list): List of unexpected return values to retry.
            on_type_match (list): List of expected return value types to retry.
            on_type_unmatch (list): List of unexpected return value types to retry.
            retries (int): Maximum number of retries.
            retry_delay (float): Delay between each retry.
            delay_multiply (int): Multiplier for increasing delay with each retry.
            handler (callable): Custom handler function to evaluate the return value.
        """
        self.on_error = on_error
        self.on_match = on_match
        self.on_unmatch = on_unmatch
        self.on_type_match = on_type_match
        self.on_type_unmatch = on_type_unmatch
        self.retries = retries
        self.retry_delay = retry_delay
        self.delay_multiply = delay_multiply
        self.handler = handler

    def retry(self, func: Callable[..., Any]) -> Callable[..., Any]:
        """
        Decorator function to handle retries of a given asynchronous function.

        Args:
            func (callable): The asynchronous function to decorate.

        Returns:
            callable: Decorated asynchronous function.
        """
        async def wrapper(*args, **kwargs) -> Any:
            for attempt in range(self.retries + 1):
                try:
                    result = func(*args, **kwargs) if not asyncio.iscoroutinefunction(func) else await func(*args, **kwargs)

                    if (not self.on_match or result not in self.on_match) and \
                       (not self.on_unmatch or result in self.on_unmatch) and \
                       (not self.on_type_match or not isinstance(result, tuple(self.on_type_match))) and \
                       (not self.on_type_unmatch or isinstance(result, tuple(self.on_type_unmatch))) and \
                       (not self.handler or self.handler(result) if not asyncio.iscoroutinefunction(self.handler) else await self.handler(result)):
                        return result
                except Exception as e:
                    if not self.on_error:
                        raise e

                if attempt < self.retries and self.retry_delay > 0 and not attempt+1 == self.retries:
                    await asyncio.sleep(self.retry_delay + (attempt * self.retry_delay * self.delay_multiply))

            raise RuntimeError(f"Maximum retries ({self.retries}) exceeded")

        return wrapper
