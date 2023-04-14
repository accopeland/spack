# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Buildah(Package):
    """A tool that facilitates building OCI images

    FIXME: work in progress

    => buildah: Executing phase: 'install'
    ==> Error: ProcessError: Command exited with status 2:
    'make' '-j16'

4 errors found in build log:
     32    # pkg-config --cflags  -- devmapper
     33    Package devmapper was not found in the pkg-config search path.
     34    Perhaps you should add the directory containing `devmapper.pc'
     35    to the PKG_CONFIG_PATH environment variable
     36    No package 'devmapper' found
     37    pkg-config: exit status 1
  >> 38    make: *** [Makefile:92: bin/imgtype] Error 2
     39    make: *** Waiting for unfinished jobs....
  >> 40    make: *** [Makefile:98: bin/tutorial] Error 2
  >> 41    make: *** [Makefile:73: bin/buildah] Error 2
  >> 42    make: *** [Makefile:95: bin/copy] Error 2
     43    make[1]: Leaving directory '/tmp/accopeland/spack-stage/spack-stage-buildah-1.29.1-sjhepbljoxvr4uy3yhoixewocjwif6sm/spack-src
           /tests/tools'

See build log for details:
  /tmp/accopeland/spack-stage/spack-stage-buildah-1.29.1-sjhepbljoxvr4uy3yhoixewocjwif6sm/spack-build-out.txt

    ."""

    homepage = "https://github.com/containers/buildah"
    url = "https://github.com/containers/buildah/archive/refs/tags/v1.29.1.tar.gz"

    version("1.29.1", sha256="ac20cdbd81616f3f03ef42dc3139de118e3b6d0ed737c994c45dc1039e0fa1c1")

    depends_on("pkg-config",type="build")
    # depends_on("selinux")
    depends_on("go")

    def install(self, spec, prefix):
        make()
        make("install")
