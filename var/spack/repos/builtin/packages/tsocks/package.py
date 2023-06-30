# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Tsocks(AutotoolsPackage):
    """tsocks, a transparent SOCKS proxying library."""

    homepage = "https://github.com/zouguangxian/tsocks"
    url = "https://github.com/zouguangxian/tsocks"
    version('2019-05-14', git='https://github.com/zouguangxian/tsocks.git',commit='217d9eb818b23702150f26d903fa31ccf176ac9b')

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")

    def autoreconf(self, spec, prefix):
        autoreconf("--install", "--verbose", "--force")

    def configure_args(self):
        args = []
        return args
