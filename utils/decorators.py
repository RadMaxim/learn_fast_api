from functools import wraps
import logging


def log_return(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("DECORATOR LOG START")

        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned: {result}")

        return result

    return wrapper


def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("DECORATOR Exception START")

        try:
            return func(*args, **kwargs)


        except Exception as error:
            logging.error(f"{func.__name__} error: {error}")

            return {
                "error": str(error)
            }

    return wrapper