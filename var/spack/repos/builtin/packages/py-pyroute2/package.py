# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyroute2(PythonPackage):
    """Pyroute2 is a pure Python netlink library. The core requires only Python stdlib, no 3rd party libraries. The library was started as an RTNL protocol implementation, so the name is pyroute2, but now it supports many netlink protocols."""

    homepage = "https://pypi.org/project/pyroute2/"
    pypi = "pyroute2/pyroute2-0.7.5.tar.gz"

    version("0.7.5", sha256="1eeb2fa3e2543357df0a937a700c5b6761b2aa5284400aed46206470fe5c0be5")

    depends_on("py-setuptools", type="build")
