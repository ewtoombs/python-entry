def entry(*a, **kw):
    def tmp(main):
        from argparse import ArgumentParser
        from inspect import signature
        ap = ArgumentParser(*a, **kw)
        for p in signature(main).parameters.values():
            if p.default == p.empty:
                ap.add_argument(p.name)
            elif type(p.default) == bool:
                ap.add_argument('--'+p.name, action='store_true')
            else:
                ap.add_argument('--'+p.name, default=p.default)
        main(p)
        return ap.parse_args()
    return tmp
