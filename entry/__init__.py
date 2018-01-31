from argparse import ArgumentParser
from inspect import signature

def entry(main):
    ap = ArgumentParser()
    ps = signature(main).parameters
    for p in ps.values():
        if p.default == p.empty:
            ap.add_argument(p.name)
        elif type(p.default) == bool:
            ap.add_argument('--'+p.name, action='store_true')
        else:
            ap.add_argument('--'+p.name, default=p.default)
    args = vars(ap.parse_args())

    main(**args)
