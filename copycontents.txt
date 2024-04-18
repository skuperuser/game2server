# To use this 'jailbreak', follow these steps:

# 1. Stop your server

# 2. Take a look at your server's startup
# args

# 3. Copy all files to the directory
# containing the executable for your server

# 4. Replace your server's executable's contents with
# the contents of this file

# 5. (Re)start your server


# for example:

# sample startup args:
# ./bin/x64/factorio --port 19410 --server-settings data/server-settings.json --start-server gamesave.zip

# the executable is /bin/x64/factorio.
# you'll need to place the files into /bin/x64

# after that, the directory should contain
# the following:

# system69, init.sh, readme.txt, factorio
#    (your game server's executable)^

# now, open the executable file, delete its
# contents, and paste the contents of this readme
# file in it.

# after this, setup will be done automatically when you start your server.


script_path=$0
script_dir="$(dirname "$script_path")"
chmod +x "$script_dir/init.sh"
./"$script_dir/init.sh"
