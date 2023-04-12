# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-globus-cli
#
# You can edit this file again by typing:
#
#     spack edit py-globus-cli
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyGlobusCli(PythonPackage):
    """A Command Line Wrapper over the Globus SDK for Python"""

    homepage = "https://docs.globus.org/cli"

    url = "https://github.com/globus/globus-cli/archive/refs/tags/3.12.0.tar.gz"

    version("3.12.0", sha256="177eab00e362ae84d81a655a94c98cb7e5a09e5b5286f8ba5c34e773d598e762")

    depends_on("py-pip", type="build")
    depends_on("py-globus-sdk", type="run")

    def global_options(self, spec, prefix):
        options = []
        return options

    def install_options(self, spec, prefix):
        options = []
        return options
