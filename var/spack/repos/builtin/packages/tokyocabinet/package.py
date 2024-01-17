# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *

class Tokyocabinet(AutotoolsPackage):
    """
    A "modern" rewrite of DBM, Tokyo Cabinet is a library of routines for managing a database.
    """

    homepage = "https://github.com/hthetiot/Tokyo-Cabinet"
    git = "https://github.com/hthetiot/Tokyo-Cabinet.git"
    #version('1.1.47', tag='1.1.47') #, submodules=True)
    version("develop", branch="master")

    license("LGPL")

    def install(self, spec, prefix):
        make()
        make("install")
