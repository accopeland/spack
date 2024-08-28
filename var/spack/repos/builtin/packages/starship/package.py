# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Starship(CargoPackage):
    """The minimal, blazing-fast, and infinitely customizable prompt for any shell!"""

    homepage = "https://github.com/starship/starship"
    url = "https://github.com/starship/starship/archive/refs/tags/v1.20.1.tar.gz"

    license("ISC")

    version("1.20.1", sha256="851d84be69f9171f10890e3b58b8c5ec6057dd873dc83bfe0bdf965f9844b5dc")
    version("1.20.0", sha256="ea73a5463d30c5d5dfd473b11a27f2f25942635121dc3fc89297eeb22755ce8f")
    version("1.19.0", sha256="cf789791b5c11d6d7a00628590696627bb8f980e3d7c7a0200026787b08aba37")
    version("1.18.2", sha256="505100002efe93dbff702edd82f814cadc340335487993e76dd6777dba461a7a")
    version("1.18.1", sha256="2ab61ae3d2e256266191f670a76a35fd06310ada2777efa0f2b6d2602071d13b")
    version("1.18.0", sha256="e387ead17edeccb603b15dc2bd9b61c6541e795e0f4a9d9015015743228c2368")
    version("1.17.1", sha256="2b2fc84feb0197104982e8baf17952449375917da66b7a98b3e3fd0be63e5dba")
    version("1.17.0", sha256="24b6c17b5d948e04149bf35bfc42889ec60168c2a158ae6f90589cd993099ba5")
    version("1.16.0", sha256="133888e190ce1563927e16ee693da3026d2e668d975ac373f853e030743775c5")
    version("1.15.0", sha256="e525476cf93d3a06332abf9e02415d4789fac6f28e4b7d98db7d83da08231828")
