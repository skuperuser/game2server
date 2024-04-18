# alpinecraft
Can be used to easily transform a (game) server into a general-purpose linux server using proot.

To use this 'jailbreak', follow these steps:
 1. Stop your server.

 2. Take a look at your server's startup args.

 3. Copy all files to the directory containing the executable for your server.

 4. Replace your server's executable's contents with the contents of copycontents.txt.

 5. (Re)start your server.

## For example:
Let's say your startup args are:
./bin/x64/factorio --port 19410 --server-settings data/server-settings.json --start-server gamesave.zip

The executable is /bin/x64/factorio. you'll need to place the files into /bin/x64.

After this, the directory should contain the following:
- system
- init.sh
- readme.txt
- factorio

Now, open the executable file, delete its contents, and paste the contents of copycontents.txt file in it.

That's it. You can now start your server as usual.
