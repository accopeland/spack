# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Fdt(MavenPackage):
    """
    FDT is an Application for Efficient Data Transfers which is capable of
    reading and writing at disk speed over wide area networks (with standard
    TCP). It is written in Java, runs an all major platforms and it is easy to
    use. FDT is based on an asynchronous, flexible multithreaded system and is
    using the capabilities of the Java NIO libraries.
    """

    homepage = "https://github.com/fast-data-transfer/fdt"
    url = "https://github.com/fast-data-transfer/fdt/archive/refs/tags/0.26.3.tar.gz"

    version("0.26.3", sha256="2f55e83b246d0a2426cfd72ceb91d723f4946764c7c4e268713cea2e8083549b")

    depends_on("maven", type="build")
    depends_on("java", type="run")

    def build(self, spec, prefix):
        pass
