# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Xsv(MakefilePackage):
    """A fast CSV command line toolkit written in Rust."""

    homepage = "https://github.com/BurntSushi/xsv"
    url = "https://github.com/BurntSushi/xsv/archive/refs/tags/0.13.0.tar.gz"

    version("0.13.0", sha256="2b75309b764c9f2f3fdc1dd31eeea5a74498f7da21ae757b3ffd6fd537ec5345")

    depends_on("rust")
    #depends_on("cargo")

    def install(self, spec, prefix):
        cargo = which("cargo")
        cargo("install", "--root", prefix, "--path", ".")
