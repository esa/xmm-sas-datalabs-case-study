#   Copyright (c) European Space Agency, 2025.
#
#   This file is subject to the terms and conditions defined in file 'LICENCE.txt', which
#   is part of this source code package. No part of the package, including
#   this file, may be copied, modified, propagated, or distributed except according to
#   the terms contained in the file ‘LICENCE.txt’.

from pysas.wrapper import Wrapper as w
import os.path
from os import path
import subprocess
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.table import Table



# Define path to working directory
home = os.path.expanduser('~')
wdir=f'{home}/VelaX1-data'

# Set up path to CCFs
ccf_paths = ['/data/user/pub', '/data/pub']
for user_ccfpath in ccf_paths:
    ccf_path = f'{home}{user_ccfpath}'
    if os.path.isdir(ccf_path):
        os.environ['SAS_CCFPATH'] = ccf_path
        print("Path to the XMM-Newton CCFs: " + ccf_path + "\n")
        break
else:
    raise FileNotFoundError("Cannot locate the specified CCF paths, please check your data volume.")

inargs = [f'sas_ccf={wdir}/ccf.cif', f'sas_odf={wdir}/3553_0841890201_SCX00000SUM.SAS', f'workdir={wdir}']
w('startsas', inargs).run()

table = wdir + "/PN_clean_evt.fits"
gti_dir = "./gti_files"

# Extract spectra for each GTI
spectrum_dir = "./spectra"
os.makedirs(spectrum_dir, exist_ok=True)

# Avoiding pile-up regions
rawX1src= 32
rawX2src = 44
rawX3src = 36
rawX4src = 40

for gti_file in sorted(os.listdir(gti_dir)):
    gti_path = os.path.join(gti_dir, gti_file)
    output_spectrum = os.path.join(spectrum_dir, f"spectrum_{os.path.splitext(gti_file)[0]}.fits")
    print(f"Processing {gti_file}...")
    cmd = "evselect"
    expression = f'(FLAG==0) && (PATTERN<=4) && (RAWX in [{rawX1src}:{rawX3src}] || RAWX in [{rawX4src}:{rawX2src}]) && (gti({gti_path},TIME))' 
    inargs = [f'table={table}', 'withspectrumset=yes', f'spectrumset={output_spectrum}', 'energycolumn=PI', 'spectralbinsize=5', 'withspecranges=yes', 'specchannelmin=0', 'specchannelmax=20479', f'expression={expression}']
    w(cmd, inargs).run()
    
    cmd        = "backscale"            
    inargs     = [f'spectrumset={output_spectrum}',f'badpixlocation={table}']
    w(cmd, inargs).run()
    
    cmd        = "rmfgen" 
    in_RESPFile = os.path.join(spectrum_dir, f"PN_{os.path.splitext(gti_file)[0]}.rmf")
    inargs     = [f'spectrumset={output_spectrum}',f'rmfset={in_RESPFile}']
    w(cmd, inargs).run()
    
    cmd        = "arfgen" 
    in_ARFFile = os.path.join(spectrum_dir, f"PN_{os.path.splitext(gti_file)[0]}.arf")
    inargs     = [f'spectrumset={output_spectrum}',f'arfset={in_ARFFile}', 'withrmfset=yes',f'rmfset={in_RESPFile}',f'badpixlocation={table}','detmaptype=psf', 'applyabsfluxcorr=yes']
    w(cmd, inargs).run()
    
    cmd        = "specgroup" 
    in_GRPFile = os.path.join(spectrum_dir, f"PN_spectrum_grp_{os.path.splitext(gti_file)[0]}.fits")
    inargs     = [f'spectrumset={output_spectrum}','mincounts=25','oversample=3', f'rmfset={in_RESPFile}',f'arfset={in_ARFFile}', f'groupedset={in_GRPFile}']
    w(cmd, inargs).run()
    

print(f"Spectra saved in {spectrum_dir}.")