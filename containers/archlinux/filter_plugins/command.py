from itertools import chain

def build_list(options):
    return list(chain.from_iterable(formatter(options)))

def formatter(options):
    def long_option(opt):
        return ('--{}'.format(opt))

    return zip(map(long_option, options.keys()), options.values())

class FilterModule(object):

    def filters(self):
        return {
            'opts_list': build_list
        }
