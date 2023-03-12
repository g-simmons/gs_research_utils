import timeit


def get_logger():
    from loguru import logger
    import sys

    logger.remove()
    logger.add(
        sys.stderr, format="{time} {level} {message}", level="INFO", colorize=True
    )
    return logger


logger = get_logger()


def time_it(func):
    def wrapper(*args, **kwargs):
        run = None
        if hasattr(func, "__self__"):
            if hasattr(func.__self__, "run"):
                run = func.__self__.run
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        if run:
            run.log({"time_" + func.__name__: end_time - start_time})
        print(
            "Function %s took %f seconds to run."
            % (func.__name__, end_time - start_time)
        )
        return result

    return wrapper
