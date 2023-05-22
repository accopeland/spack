# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RStudioServer(AutotoolsPackage):
    """RStudio Server enables you to run the RStudio IDE you know and love on a Linux server, accessed from your web browser, bringing the power and productivity of the RStudio IDE to a centralized server-based environment."""

    homepage = "https://posit.co/download/rstudio-server/"
    url = "https://github.com/rstudio/rstudio/tarball/v2022.07.2+576"

    # version("1.2.3", "0123456789abcdef0123456789abcdef")

    # depends_on("foo")

    def configure_args(self):
        args = []
        return args
