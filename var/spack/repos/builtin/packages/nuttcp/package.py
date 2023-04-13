# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *

class Nuttcp(MakefilePackage):
    """nuttcp is a network performance measurement tool intended for use by network and system managers. Its most basic usage is to determine the raw TCP (or UDP) network layer throughput by transferring memory buffers from a source system across an interconnecting network to a destination system, either transferring data for a specified time interval, or alternatively transferring a specified number of bytes. In addition to reporting the achieved network throughput in Mbps, nuttcp also provides additional useful information related to the data transfer such as user, system, and wall-clock time, transmitter and receiver CPU utilization, and loss percentage (for UDP transfers)."""

    homepage = "https://www.nuttcp.net/Welcome%20Page.html"
    url = "http://nuttcp.net/nuttcp/nuttcp-8.2.2.tar.bz2"

    version("8.2.2", sha256="7ead7a89e7aaa059d20e34042c58a198c2981cad729550d1388ddfc9036d3983")
    version("8.1.4", sha256="737f702ec931ec12fcf54e66c4c1d5af72bd3631439ffa724ed2ac40ab2de78d")

    # depends_on("foo")

    def build(self, spec, prefix):
        make("nuttcp")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("nuttcp",join_path(prefix.bin))

