#! /usr/bin/env python

import os
from nipype.interfaces.fsl.maths import StdImage

convert = StdImage(in_file='data 1/f5.nii',
                     out_file='f5.nii')
print(convert.cmdline)
convert.run()
