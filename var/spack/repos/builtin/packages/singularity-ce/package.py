# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
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
#     spack install singularity-ce
#
# You can edit this file again by typing:
#
#     spack edit singularity-ce
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class SingularityCe(MakefilePackage):
    """SingularityCE is the Community Edition of Singularity, an open source container platform designed to be simple, fast, and secure."""

    homepage = "https://sylabs.io/singularity/"
    url = "https://github.com/sylabs/singularity/releases/download/v3.11.1/singularity-ce-3.11.1.tar.gz"

    version("3.11.1", sha256="93d1665b994ef17ae8ef3a0784ae94cade8435af0a3e4bad2efbac525938b457")

    depends_on("libseccomp")
    depends_on("glib") # 2.0
    depends_on("pkg-config")
    depends_on("squashfs")
    depends_on("cryptsetup")
    depends_on("runc")
    #depends_on("uidmap")
    depends_on("go",type="build")

# FIXME
# ./mconfig
# make -C builddir
# sudo make -C builddir install

    def edit(self, spec, prefix):
        # FIXME: Edit the Makefile if necessary
        # FIXME: If not needed delete this function
        # makefile = FileFilter("Makefile")
        # makefile.filter("CC = .*", "CC = cc")
        pass
