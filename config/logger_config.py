import logging
import uvicorn

FORMAT: str = "%(levelprefix)s %(asctime)s [%(name)s]  %(message)s"


def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    handler = logging.StreamHandler()
    formatter = uvicorn.logging.DefaultFormatter(FORMAT, datefmt="%Y-%m-%d %H:%M:%S")

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger