# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import os

from spack.package import *


class Prrte(AutotoolsPackage):
    """PRRTE is the Reference RunTime Environment implementation for PMIx.
    It is capable of operating within a host SMS. The reference RTE
    therefore provides an easy way of exploring PMIx capabilities and
    testing PMIx-based applications outside of a PMIx-enabled
    environment."""

    homepage = "https://pmix.org"
    url = "https://github.com/pmix/prrte/releases/download/v1.0.0/prrte-1.0.0.tar.bz2"
    git = "https://github.com/pmix/prrte.git"
    maintainers("rhc54")

    license("BSD-3-Clause-Open-MPI")

    version("develop", branch="master")
    version("3.0.5", sha256="75ce732b02f3bc7eff5e51b81469e4373f1effc6a42d8445e2935d3670e58c8e")
    version("3.0.4", sha256="7394c2ef9ea548cbc223b62a943f470cfbccf74b3879ac92564d148537f229df")
    version("3.0.3", sha256="25b30a6252ecaeb98d3c2244710493ee5d0bbc31bfa939a42df391bde7293b80")
    version("3.0.2", sha256="1aaa1bb930e8e940251ea682b4a6abc24e4849fa9ffbaaaaf2750a38ba4e474a")
    version("3.0.1", sha256="98fe184b191e78571877492620cc90dd5d46b603a64490fa8356843b39628683")
    version("3.0.0", sha256="0898797e5530e2e37f248a1b32d572828cb3304b0c427b376ea006a1452ba565")
    version("1.0.0", sha256="a9b3715e059c10ed091bd6e3a0d8896f7752e43ee731abcc95fb962e67132a2d")

    depends_on("pmix")
    depends_on("libevent")
    depends_on("hwloc")
    depends_on("perl", type=("build"))
    depends_on("m4", type=("build"))
    depends_on("autoconf", type=("build"))
    depends_on("automake", type=("build"))
    depends_on("libtool", type=("build"))
    depends_on("flex", type=("build"))
    depends_on("pkgconfig", type="build")

    def autoreconf(self, spec, prefix):
        # If configure exists nothing needs to be done
        if os.path.exists(self.configure_abs_path):
            return
        with working_dir(self.configure_directory):
            perl = spec["perl"].command
            perl("autogen.pl")

    def configure_args(self):
        spec = self.spec
        config_args = ["--enable-shared", "--enable-static", "--disable-sphinx"]

        # libevent
        config_args.append("--with-libevent={0}".format(spec["libevent"].prefix))
        # hwloc
        config_args.append("--with-hwloc={0}".format(spec["hwloc"].prefix))
        # pmix
        config_args.append("--with-pmix={0}".format(spec["pmix"].prefix))

        return config_args
