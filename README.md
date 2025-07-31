Copyright (c) European Space Agency, 2025.

<small><em>This file is subject to the terms and conditions defined in file 'LICENCE.txt', which is part of this source code package. No part of the package, including this file, may be copied, modified, propagated, or distributed except according to the terms contained in the file ‘LICENCE.txt’.</em></small>
***

# XMM-Newton SAS in ESA Datalabs
### *A New Browser Based Interactive Environment for XMM-Newton Analysis*

This is a repository with code and data analysis notebook for the X-ray binary Vela X-1 presented in the paper: [SAS in ESA Datalabs: A New Platform for XMM-Newton Analysis](https://www.sciencedirect.com/science/article/pii/S2213133725000423?via%3Dihub).

Check [ReadMeTools.md](ReadMeTools.md) for details on the Python functions.
Check [ReadMeScripts.md](ReadMeScripts.md) for details on the Python scripts.

## Folder structure of the repository (XMM-SAS-Datalabs-Paper):

* [CaseStudy.ipynb](CaseStudy.ipynb): Jupyter Lab Notebook with the pySAS data extraction and visualisation on Vela X-1.
* [tools](tools): Python utility functions needed for plotting and visualisation.
* [scripts](scripts): Python scripts to run looped SAS tasks to extract data.

## Pre-requisites
If running the Notebook on [ESA Datalabs](https://datalabs.esa.int/) inside the XMM-SAS datalab, no pre-requisites are required. **Everything is already pre-configured inside the datalab!**

### To run locally
To run the Notebook locally you need Python 3.10 or above and standard packages/software listed in [requirements.txt](requirements.txt).
The Docker container environment used in the XMM-SAS Datalab has [HEASOFT](https://heasarc.gsfc.nasa.gov/lheasoft/) built from source in order to also have [`xspec`](https://heasarc.gsfc.nasa.gov/xanadu/xspec/) available (MIT license). You will need [SAS](https://www.cosmos.esa.int/web/xmm-newton/what-is-sas) version 21.0.0 to have access to pysas-wrapper (GPL-3.0 license) and SAS commands.

---

*Author: Esin G. Gulbahar*

*Last Updated: 27/05/2025*
