# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Mutil(AutotoolsPackage):
    """Parallel utils based on coreutils patches"""

    homepage = "https://github.com/pkolano"
    git = "https://github.com/pkolano/mutil.git"

    license("UNKNOWN")

    #version("master", branch="master")
    version("1.822.6", tag="1.822.6", commit="782aec9")

    variant("mpi", default=True, description="Use MPI for parallel solvers")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("libgcrypt", type="build")
    depends_on("libgpg-error", type="build")
    depends_on("gnutls", type="build")
    depends_on("coreutils", type="build")
    depends_on("mpi", when="+mpi")

    def patch(self):
        # filter_file(r"MAKE_CXX_STANDARD 14 PARENT_SCOPE","MAKE_CXX_STANDARD 17 PARENT_SCOPE","dev/cmake/ComponentSetup.cmake",)
        # cd coreutils-8.22
        #   patch -p1 < /path/to/patch/coreutils-8.22.patch
        reutrn 

    def autoreconf(self, spec, prefix):
        autoupdate("--include=m4")
        autoreconf(
            "--install",
            "--verbose",
            "--force",
            "--include=m4",
            "--include=" + spec["libtool"].prefix + "/share/aclocal/",
        )

    def configure_args(self):
        args = []
        # --no-direct-read, --no-direct-write, --no-double-buffer,--no-fadvise-read, and --no-fadvise-write.
        args.append("--enable-swig")
        return args
