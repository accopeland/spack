# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Lima(Package):
    """Linux virtual machines, typically on macOS, for running containerd"""

    homepage = "https://github.com/lima-vm/lima"
    url = "https://github.com/lima-vm/lima/releases/tag/v0.15.0"

    version("1.2.1", sha256="549937fe7763d655952a4779bef83a5de4f10873daa7d1b8c154b7af592dba7f")
    version("1.2.0", sha256="ebc1747bd1a31e766652bbe0a1887b335d358bb45a69e6295c13580e0d7e0d08")
    version("1.1.0", sha256="ef58c1408fcf8df55c18fcb136c5c48afa669ed2b99ae91f07abe80dfaf91dea")

    depends_on("go")
