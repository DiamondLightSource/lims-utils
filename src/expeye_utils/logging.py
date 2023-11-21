import logging

class EndpointFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        if type(record.args) is not tuple:
            return True

        return not record.args or record.args[2] != "/docs"


def register_loggers():
    """Register Uvicorn error and access logs, filtering out calls to /docs by default"""
    uvicorn_logger = logging.getLogger("uvicorn.access")
    uvicorn_logger.addFilter(EndpointFilter())

    logging.basicConfig(format="%(levelname)s: %(message)s")
    app_logger = logging.getLogger("uvicorn")
    app_logger.setLevel("INFO")

