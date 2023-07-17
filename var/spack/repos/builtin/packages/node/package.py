# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Node(Package):
    """Node.js is an open-source, cross-platform JavaScript runtime environment."""

    homepage = "https://nodejs.org/en/download"
    url = "https://nodejs.org/dist/v18.16.0/node-v18.16.0.tar.gz"

    version("18.16.0", sha256="6a4f5c5d76e5c50cef673099e56f19bc3266ae363f56ca0ab77dd2f3c5088c6d")

    def install(self, spec, prefix):
        configure() 
        mkdir(prefix.bin)
        make()
        install("node",prefix.bin)
