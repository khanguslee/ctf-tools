# CTF Tools

Random scripts to use for CTFs.

## Installation Guide

1. Create virtual environment in current folder

    ```bash
    python3 -m venv .venv
    ```

2. Activate virtual environment

    ```bash
      source .venv/bin/activate
    ```

3. Install packages

4. Deactivate virtual environment

    ```bash
    deactivate
    ```

## Tools

### `netcat.py`

This tool is similar to the `netcat` CLI tool.

If you need to communicate to a non-http server, you might sometimes need to communicate via 
tcp/udp protocol instead.

