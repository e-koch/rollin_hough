rollin_hough
============
[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.18497.svg)](http://dx.doi.org/10.5281/zenodo.18497)

[![Build Status](https://travis-ci.org/e-koch/rollin_hough.svg?branch=master)](https://travis-ci.org/e-koch/rollin_hough)

Python implementation of the Rolling Hough Transform

Code is based on method presented in [Clark et al. (2014)](http://adsabs.harvard.edu/cgi-bin/bib_query?arXiv:1312.1338).
This method varies from the original by allowing for the distribution to begin at an arbitary angle. This is useful when external data (such as the polarization) is not available to 'zero' the distributions.

This code is used in [fil_finder](https://github.com/e-koch/fil_finder) to find the direction of filaments on the plane.

Requires
--------
*   numpy
*   scipy
*   matplotlib
