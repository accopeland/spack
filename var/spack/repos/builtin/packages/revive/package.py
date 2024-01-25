# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *

class Revive(GoPackage):
    """
    ~6x faster, stricter, configurable, extensible, and beautiful drop-in replacement for golint 
    """

    homepage = "https://github.com/mgechev/revive"
    url = "https://github.com/mgechev/revive/archive/refs/tags/v1.3.6.tar.gz"

    license("MIT")

    version("1.3.6", sha256="64ee2af7820143ec6967b1da3eda641ef74cee071fc7f48d8a0e2e9f272e66d3")
    version("1.3.5", sha256="c99e543eb8ee46d94c43cbbe3b02d47552bc802155358e10e9bffaee87539e23")
    version("1.3.4", sha256="78a5a5a416d9d6fb2111e978da59b6347516453d60d84ba7914bb1f839b00fe2")
    version("1.3.3", sha256="961e7c268dad0934bff169043c9ac0ec736f62854a48a791111fd979549fada0")

    depends_on("go@1.20:")
