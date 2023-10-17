# Though os.system() is simple to use because it takes a string argument, it is recommended that you use the more powerful subprocess.run() function.
# You can use the subprocess module to spawn new processes, connect to input/output/error pipes, and obtain error codes.
# The subprocess.run() function can take many new arguments, but those additional arguments are optional.

import subprocess

# The "-l" is an argument that tells the ls command to use a long-listing format.

# subprocess.run(["ls", "-l"])

# You will call the uname command to get system information.

# command="uname"
# commandArgument="-a"
# print(f'Gathering system information with command: {command} {commandArgument}')
# subprocess.run([command,commandArgument])

# The "-l" is an argument that tells the ls command to use a long-listing format.

command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])