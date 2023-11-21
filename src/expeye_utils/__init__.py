from importlib.metadata import version

__version__ = version("expeye_utils")
del version

__all__ = ["__version__"]
