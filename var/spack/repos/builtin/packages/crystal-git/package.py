# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install crystal-git
#
# You can edit this file again by typing:
#
#     spack edit crystal-git
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class CrystalGit(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://crystal-lang.org"
    url = "https://github.com/crystal-lang/crystal.git"

    # maintainers = ["github_user1", "github_user2"]

    # version("1.2.3", "0123456789abcdef0123456789abcdef")

    # depends_on("foo")

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make()
        make("install")
