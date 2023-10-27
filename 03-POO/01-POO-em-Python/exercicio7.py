from typing import Optional, Union


class Database:
    def __init__(
        self,
        dialect: str,
        user: str,
        host: str,
        password: str,
        database: str,
        port: Optional[Union[str, int]] = ""
    ) -> None:
        """Creates a Database instance

        Parameters
        ----------
        dialect : str
        user : str
        host : str
        password : str
        database : str
        port : str | int, optional, by default ""

        >>> database = Database(
        ...     dialect = "",
        ...     user = "",
        ...     host = "",
        ...     password = "",
        ...     database = "",
        ...     port = "a",
        ... )
        Traceback (most recent call last):
        ...
        ValueError: `port` must have a numeric value
        """
        if isinstance(port, str) and not port.isnumeric():
            raise ValueError("`port` must have a numeric value")

