# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Tokyocabinet(AutotoolsPackage):
    """
    Tokyo Cabinet is a library of routines for managing a database.
    """

    homepage = "https://github.com/hthetiot/Tokyo-Cabinet"
    git = "https://github.com/hthetiot/Tokyo-Cabinet.git"

    version("develop", branch="master")
    version("1.1.47", commit="f8bd3c5")

    license("UNKNOWN", checked_by="github_user1")

