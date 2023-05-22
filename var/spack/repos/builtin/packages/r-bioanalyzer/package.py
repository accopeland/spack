# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *

class RBioanalyzer(RPackage):
    """R tools for Agilent electrophoresis data"""

    homepage = "https://github.com/jwfoley/bioanalyzeR"
    url = "https://github.com/jwfoley/bioanalyzeR/releases/download/v0.10.0/bioanalyzeR_0.10.0.tar.gz"

    version("0.10.0", sha256="d9b59164834c9773056158148347da2cb6e12a6a85276bc24a427e25caeb2e44")

    depends_on("r-xml", type="run")
    depends_on("r-base64enc", type="run")
    depends_on("r-plyr", type="run")
    depends_on("r-ggplot2", type="run")

    def configure_args(self):
        args = []
        return args
