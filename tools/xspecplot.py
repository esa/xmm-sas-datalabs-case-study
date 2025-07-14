#   Copyright (c) European Space Agency, 2025.
#
#   This file is subject to the terms and conditions defined in file 'LICENCE.txt', which
#   is part of this source code package. No part of the package, including
#   this file, may be copied, modified, propagated, or distributed except according to
#   the terms contained in the file ‘LICENCE.txt’.
#
# The latest Xspec reference is https://ui.adsabs.harvard.edu/abs/1996ASPC..101…17A/abstract<https://ui.adsabs.harvard.edu/abs/1996ASPC..101%E2%80%A617A/abstract>
# Xspec 12 was developed by: Keith Arnaud<https://heasarc.gsfc.nasa.gov/docs/bios/arnaud.html>, Ben Dorman, and Craig Gordon
# HEASARC<https://heasarc.gsfc.nasa.gov/> Software Development, Astrophysics Science Divsion
# Code 660.1, NASA/GSFC, Greenbelt MD 20771
#
# Please send comments, questions, and bug reports to xspechelp@athena.gsfc.nasa.gov[cid:image001.gif@01DBF4A2.DDE7B1F0]<mailto:xspechelp@athena.gsfc.nasa.gov>
#
# Disclaimer of endorsement
#
# The U.S. government, including NASA, neither endorses nor guarantees in any way the external organizations, services, advice, or products included in the external website links. 
# Furthermore, the U.S. government neither controls nor guarantees the accuracy, relevance, timeliness, or completeness of the information contained in non-government website links.


import os.path
from os import path
import subprocess
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.table import Table
from matplotlib.colors import LogNorm
from matplotlib.ticker import ScalarFormatter  # For formatting axis labels
from xspec import *


def xspecplot(data, xAxis="keV", xLog=True, yLog=True, figname="multiple-spectra.png"):
    """
    Plots spectra using XSPEC and Matplotlib, stacked vertically.
    
    Parameters:
        data (list): List of XSPEC data objects. Indices must start from 1.
        xAxis (str): X-axis units (default is "keV").
        xLog (bool): Whether to use logarithmic scale for X-axis.
        yLog (bool): Whether to use logarithmic scale for Y-axis.
        title (str): Title for the entire figure.
    """
    Plot.device = "/null"    # Disable XSPEC native plot output
    Plot.xAxis = xAxis       # Set X axis to energy units
    Plot.xLog = xLog         # Logarithmic X-axis
    Plot.yLog = yLog         # Logarithmic Y-axis
    Plot("data")             # Generate XSPEC plots for source/background spectra

    num_plots = len(data)    # Number of plots
    fig, axes = plt.subplots(num_plots, 1, figsize=(8, 4 * num_plots), sharex=True)

    # Ensure axes is iterable (handles single dataset case)
    if num_plots == 1:
        axes = [axes]

    for i, (dataset, ax) in enumerate(zip(data, axes), start=1):  # Start enumeration from 1
        try:
            energies = Plot.x(i)    # X-axis values (index starts from 1)
            edeltas = Plot.xErr(i)  # X-axis error values
            rates = Plot.y(i)       # Y-axis values
            errors = Plot.yErr(i)   # Y-axis error values
            labels = Plot.labels()

            # Plot spectrum with error bars
            ax.errorbar(
                energies, rates,
                xerr=edeltas, yerr=errors,
                fmt='.'
            )
            
            # Configure subplot scales and labels
            if xLog: ax.set_xscale('log')
            if yLog: ax.set_yscale('log')
            ax.set_ylabel(labels[1] if labels else "Counts/sec")
            ax.set_yticks([0.5, 1, 2, 5, 10], labels=[0.5, 1, 2, 5, 10])
            #plt.yticks([0.5, 1, 2, 5, 10], labels=[0.5, 1, 2, 5, 10])
            ax.set_ylim(0.4, 12.5)
            for xval in [3, 6, 8]:
                ax.axvline(x=xval, color='red', linestyle='--', linewidth=1)
            ax.tick_params(axis='both', which='both', direction='in', top=True, right=True)
            ax.tick_params(axis='both', which='major', labelsize=13, length=10, width=1)
            ax.tick_params(axis='both', which='minor', length=5, width=1)

        except Exception as e:
            print(f"Error plotting dataset {i}: {e}")

    # Add shared X-axis label
    axes[-1].set_xlabel(labels[0] if labels else "Energy (keV)")
    plt.xticks([0.5, 1, 2, 5, 10], labels=[0.5, 1, 2, 5, 10])
    axes[-1].set_xlim(0.5, 10)

    # Add a global title
    #fig.suptitle(title, fontsize=16)

    # Adjust spacing to remove vertical gaps
    plt.subplots_adjust(hspace=0)
    
    plt.savefig(figname)

    plt.show()


