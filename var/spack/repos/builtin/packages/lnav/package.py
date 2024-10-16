# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *

class Lnav(AutotoolsPackage):
    """Log file navigator"""

    homepage = "https://github.com/tstack/lnav"
    url = "https://github.com/tstack/lnav/archive/refs/tags/v0.11.2.tar.gz"

    version("0.11.2-rc6", sha256="68b738f6997689eaa9ad062082caf4768ff6d692afd4c1fef4b7ec685c4c7340")
    version("0.11.2-rc5", sha256="4e7d861523c2108655f71ac81f4fce2d0589cc1483d42e64645e46e3e59dd0ad")
    version("0.11.2-rc3", sha256="30018e8553b3840199a1174bd52b9e18a601595cc2c55e549204739df484eac4")
    version("0.11.2-rc2", sha256="edb228052b300f05361a7b9260a6cfab08cb4fd2654caca716c103e22e547f77")
    version("0.11.2-rc1", sha256="6a8f51d9223cca097562b4575ad28d66ad73ea59f7a17ec261914b71405a1647")
    version("0.11.2", sha256="03b72fd02faccdbf98fcdeba62306794b677b8bcf49d6023117808f88ed627dc")

    variant("wireshark", default=False, description="tshark for interpreting pcap files")

    depends_on("autoconf", type="build", when="@0.11.2 build_system=autotools")
    depends_on("automake", type="build", when="@0.11.2 build_system=autotools")
    depends_on("libtool", type="build", when="@0.11.2 build_system=autotools")

    #gcc/clang - A C++14-compatible compiler.
    depends_on("pcre2")  # - The Perl Compatible Regular Expression v2 (PCRE2) library.
    depends_on("sqlite")
    depends_on("ncurses")
    depends_on("readline")
    depends_on("zlib")
    depends_on("bzip2")
    depends_on("curl") # libcurl
    depends_on("libarchive") # - The libarchive library for opening archive files, like zip/tgz.
    depends_on("wireshark", when="+wireshark") # - The 'tshark' program is used to interpret pcap files.
