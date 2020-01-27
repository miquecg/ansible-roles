from itertools import chain

def build_list(options):
    names, values = map(formatter, options.keys()), options.values()
    return flatten(zip(names, values))

def formatter(opt):
    return '--{}'.format(opt)

def flatten(nested):
    return list(chain.from_iterable(nested))

class FilterModule(object):

    def filters(self):
        return {
            'opts_list': build_list
        }
