# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Libelfin(AutotoolsPackage):
    """libelfin C++11 ELF/DWARF parser"""

    homepage = "https://github.com/antoyo/libelfin"
    url = "https://github.com/antoyo/libelfin"
    #git = "https://github.com/antoyo/libelfin.git"
    #version("e20edab", git="https://github.com/antoyo/libelfin/commit/e20edabd59453221fd63d1aae9bd5f0cdea97948" , commit="e20edab")
    url = "https://github.com/antoyo/libelfin/archive/refs/tags/v0.3.tar.gz"
    version("0.3", sha256="c338942b967582922b3514b54b93175ca9051a9668db92dd8ef619824d443ac7")

    depends_on("autoconf", type="build", when="@0.3 build_system=autotools")
    depends_on("automake", type="build", when="@0.3 build_system=autotools")
    depends_on("libtool", type="build", when="@0.3 build_system=autotools")
