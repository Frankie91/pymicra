"""
 PyMicrA - Python Micrometeorology Analysis tool
 --------------------------------
 Author: Tomas Chor
 Date of start: 2015-08-15
 --------------------------------

 This package is a collection of functions aimed at analysing 
 micrometeorology data. It mainly uses Pandas and Numpy for its
 analysis so these are required packages.
"""
from io import dataloggerConf, timeSeries, read_dlc, toUnitsCsv, readUnitsCsv
from micro import *
from data import *

import io
import physics
import util
import constants
import notation
from micro import spectral
import micro
import genalgs
__version__='0.1.0'

