## \file /src/utils/get_free_port.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3
"""
Module for finding a free port.

Agrs:
    host (str): The host address to check for available ports.
    port_range (Optional[str | List[str]], optional): A port range specified as a string "min-max" or a list of strings.
           E.g.: "3000-3999", ["3000-3999", "8000-8010"], None. Defaults to `None`.

Returns:
    int: An available port number.

Raises:
    ValueError: If no free port can be found within the specified range, or if the port range is invalid.

Example:
    >>> get_free_port('localhost', '3000-3005')
    3001
"""

import socket
from typing import Optional, Tuple, List

import header  # Not used
from src.logger import logger

def get_free_port(host: str, port_range: Optional[str | List[str]] = None) -> int:
    """
    Finds and returns a free port within the specified range, or the first available port if no range is given.

    Args:
        host (str): The host address to check for available ports.
        port_range (Optional[str | List[str]], optional): A port range specified as a string "min-max" or a list of strings.
               E.g.: "3000-3999", ["3000-3999", "8000-8010"], None. Defaults to `None`.

    Returns:
        int: An available port number.

    Raises:
        ValueError: If no free port can be found within the specified range, or if the port range is invalid.
    """
    def _is_port_in_use(host: str, port: int) -> bool:
        """
        Checks if a given port is in use on the specified host.

        Args:
            host (str): The host address.
            port (int): The port number to check.

        Returns:
            bool: True if the port is in use, False otherwise.
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.bind((host, port))
                return False  # Port is available
            except OSError:
                return True  # Port is in use

    def _parse_port_range(port_range_str: str) -> Tuple[int, int]:
        """
        Parses port range string "min-max" into a tuple (min_port, max_port).

        Args:
            port_range_str (str): The port range string.

        Returns:
            Tuple[int, int]: A tuple containing minimum and maximum port numbers.

        Raises:
            ValueError: If the port range string format is invalid.
        """
        try:
            parts = port_range_str.split('-')
            if len(parts) != 2:
                logger.error(f'Error: Invalid port range string format: {port_range_str}')
                raise ValueError(f'Invalid port range string format: {port_range_str}')
            min_port = int(parts[0])
            max_port = int(parts[1])

            if min_port >= max_port:
                logger.error(f'Error: Invalid port range {port_range_str}')
                raise ValueError(f'Invalid port range {port_range_str}')
            return min_port, max_port

        except ValueError:
            logger.error(f'Error: Invalid port range {port_range_str}')
            raise ValueError(f'Invalid port range {port_range_str}')

    if port_range:
        if isinstance(port_range, str):
            try:
                min_port, max_port = _parse_port_range(port_range)
            except ValueError as e:
                logger.error(f'Error: {e}')
                raise ValueError(f'Invalid port range {port_range}')
            for port in range(min_port, max_port + 1):
                if not _is_port_in_use(host, port):
                    return port
            logger.error(f'Error: No free port found in range {port_range}')
            raise ValueError(f'No free port found in range {port_range}')

        elif isinstance(port_range, list):
            for item in port_range:
                try:
                    if isinstance(item, str):
                        min_port, max_port = _parse_port_range(item)
                    else:
                        logger.error(f'Error: Invalid port range item {item}')
                        raise ValueError(f'Invalid port range item {item}')

                    for port in range(min_port, max_port + 1):
                        if not _is_port_in_use(host, port):
                            return port
                except ValueError as e:
                    logger.error(f'Error: {e}')
                    continue  # Skip to the next range in the list if any range fails parsing or no port

            logger.error(f'Error: No free port found in specified ranges {port_range}')
            raise ValueError(f'No free port found in specified ranges {port_range}')

        else:
            logger.error(f'Error: Invalid port range type {type(port_range)}')
            raise ValueError(f'Invalid port range type {type(port_range)}')
    else:
        # If no range given, find first available port
        port = 1024  # start from 1024, since lower ports are system ports
        while True:
            if not _is_port_in_use(host, port):
                return port
            port += 1
            if port > 65535:
                logger.error(f'Error: No free port found')
                raise ValueError('No free port found')
