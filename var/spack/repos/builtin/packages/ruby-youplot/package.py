# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RubyYouplot(RubyPackage):
    """A command line tool that draw plots on the terminal."""

    homepage = "https://github.com/red-data-tools/YouPlot"
    url = "https://rubygems.org/downloads/youplot-0.4.5.gem"

    version("0.4.5", sha256="31b7a5d38a0924953e77a5cc8d463106c1282e457fddea1dbeb3bd297931be46", expand=False)

    license("MIT")

    depends_on("ruby-unicode-plot", type="run") # >=0.0.5
