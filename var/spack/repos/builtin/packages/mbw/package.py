# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Mbw(CMakePackage):
    """Memory Bandwidth Benchmark"""

    homepage = "https://github.com/raas/mbw"
    url = "https://github.com/raas/mbw/archive/refs/tags/v2.0.tar.gz"

    license("GPLv4")

    version("2.0", sha256="557f670e13ff663086fe239e4184d8ca6154b004bd5fde2b0a748e5aa543c87f")
    version("1.5", sha256="3c396ce09bb78c895e4d45e99b1ae07f80e3ea5eee59d78ed2048a7f2ae591ae")
    version("1.4", sha256="9f7365c752f4dfe0d7d46c599ff1e4b412179be764b0d712269d7ee61e0cf718")
    version("1.3", sha256="202df22e68471376dd8cdba3d3ceda6f47e46a0f9b3905d5272701acddc73ba8")

    depends_on("cmake", when="build")
