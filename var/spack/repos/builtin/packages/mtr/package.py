# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Mtr(AutotoolsPackage):
    """ mtr, a network diagnostic tool"""

    homepage = "http://www.bitwizard.nl/mtr/"
    url = "https://github.com/traviscross/mtr/archive/refs/tags/v0.95.tar.gz"

    version("0.95", sha256="12490fb660ba5fb34df8c06a0f62b4f9cbd11a584fc3f6eceda0a99124e8596f")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("autoconf-archive", type="build")

    def setup_dependent_build_environment(self, env, dependent_spec):
        """Adds the ACLOCAL path for autotools."""
        env.append_path("ACLOCAL_PATH", self.prefix.share.aclocal)

