# entry
### _for python_

An extremely minimalist and convenient entry point for short python scripts.  
More or less ductapes your script to argparse.

## installing
Combine `./setup.py install --root=$prefix` with the package manager of your 
choice. Some crazy person maintains an AUR package, so the majority of linux 
users that I care about can do `pacaur -S python-entry`.

## using
```
@entrypoint
def main(file, init=False, config='default.conf'):
    print(file, init, config)
```

 vi:fo=atw
