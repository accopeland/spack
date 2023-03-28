# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Arping(AutotoolsPackage):
    """Arping is a util to find out if a specific IP address on the LAN is 'taken'
and what MAC address owns it. Sure, you *could* just use 'ping' to find out if
it's taken and even if the computer blocks ping (and everything else) you still
get an entry in your ARP cache. But what if you aren't on a routable net? Or
the host blocks ping (all ICMP even)? Then you're screwed. Or you use arping."""

    homepage = " http://github.com/ThomasHabets/arping"
    url = "https://github.com/ThomasHabets/arping/archive/refs/tags/arping-2.23.tar.gz"

    version("2.23", sha256="8050295e3a44c710e21cfa55c91c37419fcbb74d1ab4d41add330b806ab45069")

    depends_on("autoconf", type="build", when="@2.23 build_system=autotools")
    depends_on("automake", type="build", when="@2.23 build_system=autotools")
    depends_on("libtool", type="build", when="@2.23 build_system=autotools")
    depends_on("libnet")
    depends_on("libpcap")
    # https://github.com/libnet/libnet

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
