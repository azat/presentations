#!/usr/bin/env python3
# https://gist.github.com/azat/fe1c087d2bc25f1b831281e1ff80ff9b

import argparse

# Overhead for sparsehash [1].
#
#  [1]: https://tristanpenman.com/blog/posts/2017/10/11/sparsehash-internals/
SPARSEHASH_ELEMENT_OVERHEAD_64BIT = 2.66666667  # (64+48+16)/48
SPARSEHASH_ELEMENT_OVERHEAD_32BIT = 2           # (32+48+16)/48


def sparsehash_size(elements, element_size, load_factor, element_overhead_bits):
    # to bits
    element_size_bits = element_size * 8
    used_elements_bits = elements*(element_size_bits+element_overhead_bits)
    unused_elements_q = 1/load_factor-1
    unused_elements_bits = unused_elements_q*elements*element_overhead_bits
    bits = (used_elements_bits + unused_elements_bits)
    bytes = bits / 8
    return bytes

def sparsehash_size_64(elements, element_size, load_factor):
    return sparsehash_size(elements, element_size, load_factor, SPARSEHASH_ELEMENT_OVERHEAD_64BIT)

def sparsehash_size_32(elements, element_size, load_factor):
    return sparsehash_size(elements, element_size, load_factor, SPARSEHASH_ELEMENT_OVERHEAD_32BIT)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--size', default=1e9, type=int)
    parser.add_argument('-S', '--structure-size', help='Do not forget to respect alignment', default=16, type=int)
    parser.add_argument('-L', '--load-factor', default=0.456, type=float)
    parser.add_argument('--bits', default='64', choices=['32', '64'])
    opts = parser.parse_args()

    bytes = 0
    if opts.bits == '32':
        bytes = sparsehash_size_32(opts.size, opts.structure_size, opts.load_factor)
    else:
        bytes = sparsehash_size_64(opts.size, opts.structure_size, opts.load_factor)
    print('{:.2f} GiB'.format(bytes/1024/1024/1024))

main()
