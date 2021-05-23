# dedup_hardlinks.py

You are given a directory with some files under it (assume there's no sub directories).

Some files have more than one hardlinks. Please only keep one hardlink per file and remove any additional hardlinks.  

You can decide whichever hardlink you want to keep. There might be softlinks as well but you can ignore them.


files:

- hello2

- bye

- goodbye (hardlink of bye)

- hi(hardlink of hello2)

- hello (hardlink of hello2)

- hi2 (softlink of hello2)

remaining files:

- one of (hello2, hello, hi)

- one of (bye, goodbye)

- hi2
