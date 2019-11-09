"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def ReadFemResp(f_name="2002FemResp.dat.gz"):
    df = thinkstats2.ReadStataDct(f_name)
    return df
    
def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    df = ReadFemResp()
    print(df)
    
#     print('%s: All tests passed.' % script)
    

# if __name__ == '__main__':
#     main(*sys.argv)
