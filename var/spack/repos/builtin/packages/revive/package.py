# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Revive(GoPackage):
    """Fast linter for go"""

    homepage = "hhttps://github.com/mgechev/revive"
    url = "https://github.com/mgechev/revive/archive/refs/tags/v1.3.9.tar.gz"

    license("MIT")

    version("1.3.9", sha256="a9373b4a2cd480d5383831b6927bc701f9ca1d02c5dc3e7c3f34d4bb189167cb")
    version("1.3.7", sha256="b2dccf39ca74ac858feb67e07b7aecdcb14c8252bf000057acd19893494b2747")
    version("1.3.6", sha256="64ee2af7820143ec6967b1da3eda641ef74cee071fc7f48d8a0e2e9f272e66d3")
    version("1.3.5", sha256="c99e543eb8ee46d94c43cbbe3b02d47552bc802155358e10e9bffaee87539e23")
    version("1.3.4", sha256="78a5a5a416d9d6fb2111e978da59b6347516453d60d84ba7914bb1f839b00fe2")
    version("1.3.3", sha256="961e7c268dad0934bff169043c9ac0ec736f62854a48a791111fd979549fada0")
    version("1.3.2", sha256="3abccf0a2f2d9f257afbcfb48d96668ebb5fb360d2b460f9c1f166a9711ddeaa")
    version("1.3.1", sha256="b3b8804024cd2aadb0900912560ad8718d5d1fc47fba7d95d281b46a24352267")
    version("1.3.0", sha256="b33cf7c991e6e90fa6648dffde75d66b8cdd41761d382a1bf59cc4239e95ed39")
    version("1.2.5", sha256="a34fe667d51dd9824f06fa0985f58a4359e2883ee25b235d91e366f3c4be68d8")
