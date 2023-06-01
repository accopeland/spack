# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Proxychains(AutotoolsPackage):
    """proxychains - a tool that forces any TCP connection made by any given application to follow through proxy like TOR or any other SOCKS4, SOCKS5 or HTTP(S) proxy. Supported auth-types: "user/pass" for SOCKS4/5, "basic" for HTTP."""

    homepage = "https://github.com/haad/proxychains"
    url = "https://github.com/haad/proxychains/archive/refs/tags/proxychains-4.4.0.tar.gz"

    version("4.4.0", sha256="d886d2e4568261dfca6d132666371a49e1b155e43ab3786d0f2ae7407de4c4ff")

    depends_on("autoconf",type="build")

    def configure_args(self):
        args = []
        return args
