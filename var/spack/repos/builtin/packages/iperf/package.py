# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Iperf(AutotoolsPackage):
    """iperf3: A TCP, UDP, and SCTP network bandwidth measurement tool"""

    homepage = "https://github.com/esnet/iperf"
    url = "https://github.com/esnet/iperf/archive/refs/tags/3.13.tar.gz"

    version("3.13", sha256="a49d23fe0d3b1482047ad7f3b9e384c69657a63b486c4e3f0ce512a077d94434")

    # FIXME: Add dependencies if required.
    # depends_on("foo")

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
