# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Buildah(Package):
    """A tool that facilitates building OCI images."""

    homepage = "https://github.com/containers/buildah"
    url = "https://github.com/containers/buildah/archive/refs/tags/v1.29.1.tar.gz"

    version("1.29.1", sha256="ac20cdbd81616f3f03ef42dc3139de118e3b6d0ed737c994c45dc1039e0fa1c1")

    depends_on("pkg-config",type="build")
    # depends_on("selinux")
    depends_on("go")

    def install(self, spec, prefix):
        make()
        make("install")
