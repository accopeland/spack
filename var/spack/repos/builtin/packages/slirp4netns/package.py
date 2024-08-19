# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Slirp4netns(AutotoolsPackage):
    """User-mode networking for unprivileged network namespaces"""

    homepage = "https://github.com/rootless-containers/slirp4netns"
    url = "https://github.com/rootless-containers/slirp4netns/archive/v1.1.12.tar.gz"
    maintainers("bernhardkaindl")

    license("GPL-2.0-or-later")

    version("1.3.1", sha256="a3b7c7b593b279c46d25a48b583371ab762968e98b6a46457d8d52a755852eb9")
    version("1.3.0", sha256="551a63647114a0c50dd115640161c9330832e2466f602fd3d1eaf95d3226baab")
    version("1.2.3", sha256="acce648fab8fe5f113c41a8fd6d20177708519b4ddaa60f845e1998a17b22ca5")
    version("1.2.2", sha256="2450afb5730ee86a70f9c3f0d3fbc8981ab8e147246f4e0d354f0226a3a40b36")
    version("1.2.1", sha256="51aa240e1e29905ed35b449ca718539a01221aab3b6d291c4dc6777f0eb9d7d9")

    version("1.2.0", sha256="b584edde686d3cfbac210cbdb93c4b0ba5d8cc0a6a4d92b9dfc3c5baec99c727")
    version("1.1.12", sha256="279dfe58a61b9d769f620b6c0552edd93daba75d7761f7c3742ec4d26aaa2962")

    depends_on("c", type="build")  # generated

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("glib")
    depends_on("libcap")
    depends_on("libseccomp")
    depends_on("libslirp")
