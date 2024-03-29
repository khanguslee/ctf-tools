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

### `redis_gopher.py`

For redis <v7 you can run commands via the gopher protocol.
See https://maxchadwick.xyz/blog/ssrf-exploits-against-redis for more information

### `pyyaml_exploit.py`

Tool to generate a pyyaml payload that can run a command.
Exploit exists for pyyaml <v5.4

### `pickle_exploit.py`

Tool to generate a base64 encoded pickle payload that can run a command.
