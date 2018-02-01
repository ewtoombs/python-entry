# entry
### _for python_

Do getopt with one decorator.

## installing
Combine `./setup.py install --root=$prefix` with the package manager of your 
choice. Some crazy person maintains an AUR package, so the majority of linux 
users that I care about can do `pacaur -S python-entry`.

## using
```
script:
----------8<----------
#!/usr/bin/env python

from entry import entry

@entry
def main(file, init=False, config='default.conf'):
    print(file, init, config)
----------8<----------
% ./script
usage: script [-h] [--init] [--config CONFIG] file
script: error: the following arguments are required: file
% ./script spam.txt
spam.txt False default.conf
% ./script --init --config wacky-nonstandard-config.conf beans.txt
beans.txt True wacky-nonstandard-config.conf
```

 vi:fo=atw
