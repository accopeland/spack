# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class NcbiMagicblast(AutotoolsPackage):
    """Magic-BLAST is a tool for mapping large next-generation RNA or DNA
    sequencing runs against a whole genome or transcriptome."""

    homepage = "https://ncbi.github.io/magicblast/"
    url = "https://ftp.ncbi.nlm.nih.gov/blast/executables/magicblast/LATEST/ncbi-magicblast-1.7.1-src.tar.gz"

    version("1.7.1", sha256="31e795b00956a6173d432469895648c24aa602d725c77dcb3d77e63d3b4e773e")
    version("1.5.0", sha256="b261914d9f7ffc0e655079ceba3e348ba11df1a1f73c4e47a4b1ca154754985c")
    version("1.3.0", sha256="47b9b65d595b5cb0c4fef22bc7f7c038fb8d4a0accdbe560d7232820575aff67")

    depends_on("cpio", type="build")
    depends_on("lmdb")

    configure_directory = "c++"

    def configure_args(self):
        return ["--without-internal"]
