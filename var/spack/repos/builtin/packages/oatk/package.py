# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Oatk(MakefilePackage):
    """ Oatk is designed for de novo assembly of complex plant organelle genomes using PacBio HiFi data. The toolkit consists of three major tools. syncasm is a de novo HiFi read assembler using a sparse de Bruijn graph constructed from closed syncmers (Edgar, R. 2021). hmm_annotation is a HMMER wrapper for convenient annotation of organelle sequences using a pre-built HMM profile database which is available at OatkDB. pathfinder is a tool used for parsing and circularising organelle genomes from the assembled sequences combining the HMM annotations and assembly graph structure. oatk is a wrapper for running syncasm, hmm_annotation and path_finder collectively."""

    homepage = "https://github.com/c-zhou/oatk"
    url = "https://github.com/c-zhou/oatk/archive/refs/tags/0.1.tar.gz"

    version("0.1", sha256="94cd0df443e0ed01ef70e92d22ddc731aca85e6bdb5cb54200a1b07a967410ec")

    depends_on("zlib")
    depends_on("hmmer")
