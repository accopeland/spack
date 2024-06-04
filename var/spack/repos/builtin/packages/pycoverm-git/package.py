# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PycovermGit(CargoPackage):
    """
    FIXME - is this python or rust pkg ? 

    Simple Python interface to CoverM's fast coverage estimation functions 

    This package is still in experimental stages and aims to be a simple
    Python interface to CoverM's fast coverage estimation functions. Currently,
    pyCoverM provides two functions: is_bam_sorted, which checks whether a BAM
    file is sorted by coordinate, and get_coverages_from_bam, that computes
    average contig coverages from sorted BAM files.
    """

    homepage = "https://github.com/apcamargo/pycoverm"
    url = "https://github.com/apcamargo/pycoverm.git"

    # maintainers("github_user1", "github_user2")

    license("BSD-2-Clause")
    #version("0.6.0", md5="0123456789abcdef0123456789abcdef")

    # specific versions
    #depends_on("python@3.9:", type=("build", "run"))
    #depends_on("py-pip", type="build")
    ## depends_on("py-wheel@X.Y:", type="build")
    #depends_on("numpy@1.24.2:")
    #depends_on("torch@1.13.1:")
    #depends_on("networkx@3.1:") # missing
    #depends_on("scikit-learn@1.2.2:")
    #depends_on("pandas@2.0.0:")
    #depends_on("dadaptation@3.0:")
    #depends_on("loguru@0.7.2:")

    # build backend (see pyproject.toml)
    #depends_on("py-cython:0.29.5", type="build")
