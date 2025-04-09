Copyright (c) European Space Agency, 2025.

<small><em>This file is subject to the terms and conditions defined in file 'LICENCE.txt', which is part of this source code package. No part of the package, including this file, may be copied, modified, propagated, or distributed except according to the terms contained in the file ‘LICENCE.txt’.</em></small>
***

# XMM-Newton SAS in ESA Datalabs
### *A New Browser Based Interactive Environment for XMM-Newton Analysis*

This is a repository with code and data analysis notebook for the X-ray binary Vela X-1 presented in the paper: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5177091.

Check [ReadMeTools.md](ReadMeTools.md) for details on the Python functions.
Check [ReadMeScripts.md](ReadMeScripts.md) for details on the Python scripts.

## Folder structure of the repository (XMM-SAS-Datalabs-Paper):

* [CaseStudy.ipynb](CaseStudy.ipynb): Jupyter Lab Notebook with the pySAS data extraction and visualisation on Vela X-1.
* [tools](tools): Python utility functions needed for plotting and visualisation.
* [scripts](scripts): Python scripts to run looped SAS tasks to extract data.

## Pre-requisites
If running the Notebook on [ESA Datalabs](https://datalabs.esa.int/) inside the XMM-SAS datalab, no pre-requisites are required.

To run locally you need python 3.10 or above and standard packages like `astropy`, `numpy`, `scipy`, `plotly`, `lcviz` and [HEASOFT](https://heasarc.gsfc.nasa.gov/lheasoft/) built from source in order to have `pyXspec` available. You will need SAS version 21.

---

*Author: Esin G. Gulbahar*

*Last Updated: 09/04/2025*