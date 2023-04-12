# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Hpnssh(AutotoolsPackage):
    """HPN-SSH based on OpenSSH"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/rapier1/openssh-portable"
    url = "https://github.com/rapier1/openssh-portable/archive/refs/tags/hpn-9_2_P1.tar.gz"
    git = "https://github.com/rapier1/openssh-portable.git"

    version("develop", branch="master")
    version("9_2_P1", sha256="91432a2cb364f0b3b4b5d5437d51b811137994b774f01bbfd9ef5184471aa570")

    depends_on("autoconf")
    depends_on("automake")
    depends_on("libtool", type="build", when="@9_2_P1 build_system=autotools")
