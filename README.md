# entry
### _for python_

Do getopt with one decorator.

## installing
Combine `./setup.py install --root=$prefix` with the package manager of your 
choice. Some crazy person maintains an AUR package, so the majority of linux 
users that I care about can do `pacaur -S python-entry`.

## using
```
from entry import entry
@entry
def main(file, init=False, config='default.conf'):
    print(file, init, config)
```

 vi:fo=atw
