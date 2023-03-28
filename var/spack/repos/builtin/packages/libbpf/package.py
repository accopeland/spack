# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Libbpf(MakefilePackage):
    """Automated upstream mirror for libbpf stand-alone build."""

    homepage = "https://github.com/libbpf/libbpf"
    url = "https://github.com/libbpf/libbpf/archive/refs/tags/v1.1.0.tar.gz"

    version("1.1.0", sha256="5da826c968fdb8a2f714701cfef7a4b7078be030cf58b56143b245816301cbb8")

    #depends_on("libelf")
    depends_on("elfutils")  # GElf_Nhdr (gelf.h)

    # should have pkg_config find elfutils gelf.h

    build_directory = 'src'

    def edit(self, spec, prefix):
        env['PREFIX'] = prefix
        # makefile = FileFilter("Makefile")
        # makefile.filter("CC = .*", "CC = cc")
