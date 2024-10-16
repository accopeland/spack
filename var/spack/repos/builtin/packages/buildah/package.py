# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Buildah(GoPackage):
    """A tool that facilitates building OCI images

     error found in build log:
     4     # [pkg-config --cflags  -- gpgme]
     5     Package gpgme was not found in the pkg-config search path.
     6     Perhaps you should add the directory containing `gpgme.pc'
     7     to the PKG_CONFIG_PATH environment variable
     8     Package 'gpgme', required by 'virtual:world', not found
     9     # github.com/containers/storage/drivers/btrfs
  >> 10    vendor/github.com/containers/storage/drivers/btrfs/btrfs.go:12:10: fatal error: btrfs/ioctl.h: No such file or directory
     11       12 | #include <btrfs/ioctl.h>
     12          |          ^~~~~~~~~~~~~~~
     13    compilation terminated.


    """

    homepage = "https://github.com/containers/buildah"
    url = "https://github.com/containers/buildah/archive/refs/tags/v1.29.1.tar.gz"

    version("1.37.4", sha256="6e81e01b6a4f6e14c9cd12766dfa1dcf272f6b832bf32bf78e0567eb44b9c065")
    version("1.37.3", sha256="089183944be7817698b732058f66abdf6be1722074cda3e5bb5e6477a2d75ebe")
    version("1.37.2", sha256="3fe80cf6b0c6f892ce3cff609e95a14e101e8deacb6397652fbea85728f11ec6")
    version("1.37.1", sha256="b9f30418d8250cac56c2eb6d6fe56f80d316b9996a041df162095f45920dede7")
    version("1.37.0", sha256="f59adef68d88f21efc022f60c09cd084c4fd68a72f0282df09514fb0431069d9")
    version("1.36.0", sha256="c2dd61b3d31576c71001eae1b7cabd7e714bdef8dd7b84d8d59496f26810840d")
    version("1.35.4", sha256="7d655453d6ff150503a4ecd61481622d83735f89fc69cf1805f0d3a1619c8c2c")
    version("1.33.8", sha256="7f77e51610cb6283196d143379cf24c1544ee484ce9881997b48846fd4a0442f")
    version("1.29.1", sha256="ac20cdbd81616f3f03ef42dc3139de118e3b6d0ed737c994c45dc1039e0fa1c1")

    depends_on("pkg-config",type="build")
    depends_on("gpgme", type="build")
    # depends_on("selinux")
    #    depends_on("go")

class GoBuilder(spack.build_systems.go.GoBuilder):
    phases = ( "build", "install")

    @property
    def build_args(self):
        args = super().build_args
        args.extend(["-mod=vendor", "./cmd/buildah"])
        return args

    def build(self, pkg, spec, prefix):
        go("mod", "vendor")
        go("build",*self.build_args)
