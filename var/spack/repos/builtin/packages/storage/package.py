# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Storage(GoPackage):
    """ 
    Container Storage Library. Part of https://github.com/containers

    FIXME: broken

    go build github.com/containers/storage/pkg/devicemapper:
# pkg-config --cflags  -- devmapper
Package devmapper was not found in the pkg-config search path.
Perhaps you should add the directory containing `devmapper.pc'
to the PKG_CONFIG_PATH environment variable
No package 'devmapper' found
pkg-config: exit status 1
# github.com/containers/storage/drivers/btrfs
drivers/btrfs/btrfs.go:12:10: fatal error: btrfs/ioctl.h: No such file or directory
   12 | #include <btrfs/ioctl.h>
      |          ^~~~~~~~~~~~~~~
compilation terminated.
==> Error: ProcessError: Command exited with status 1:
    '/clusterfs/jgi/groups/gentech/homes/accopeland/spack-acc/opt/spack/linux-rocky8-zen2/gcc-12.2.0/go-1.20-jmloxxuv4qaxg5otpy7rk5ubug4bjurq/bin/go' 'build' '-ldflags' '-s -w' '-o' 'storage'

1 error found in build log:
     5     Package devmapper was not found in the pkg-config search path.
     6     Perhaps you should add the directory containing `devmapper.pc'
     7     to the PKG_CONFIG_PATH environment variable
     8     No package 'devmapper' found
     9     pkg-config: exit status 1
     10    # github.com/containers/storage/drivers/btrfs
  >> 11    drivers/btrfs/btrfs.go:12:10: fatal error: btrfs/ioctl.h: No such file or directory
     12       12 | #include <btrfs/ioctl.h>
     13          |          ^~~~~~~~~~~~~~~
     14    compilation terminated.

    """

    homepage = "https://github.com/containers/storage"
    url = "https://github.com/containers/storage/archive/refs/tags/v1.51.0.tar.gz"

    license("Apache")

    version("1.51.0", sha256="383bf3d7ef5eec3afee20ae37ca0caf8f2c2ef0ec14104cba2476f73db571c5e")
    version("1.50.2", sha256="8ed20cea8cd9bb6ecb63220a0b3f32df63445fe06fb8074c50e3c942e7d1ca0f")
    version("1.50.1", sha256="49a74926a4955c8401ee492b4e580acd9d0c91e35b4462bcfff08a6d3dc0127c")
    version("1.50.0", sha256="89d65438210ffacac9d879ccc25315d620bd6c84f2276293a9c6a1aea26641c0")
    version("1.49.0", sha256="08c1020e848518f87601239365122833e0bdb6b4c1600bd3b2cd0cf758d31c2f")
    version("1.48.1", sha256="aff55afc3c801ab5f63fce4690f10031129601315dcaf9c26ba46c8c03a0ba8e")
    version("1.48.0", sha256="5a59739d545d2cb054c5079a9fa1beb3a4611c0aef617c65792f1e3d9739fe19")
    version("1.47.0", sha256="3ec92961e0e4eb3916285121781308beebdbca20f2f90b1ce84bcda5caa10bd1")
    version("1.45.6", sha256="ac13cfad2e95e948653f077330ef99752edb9ab480e5b23b3d982bca701568f0")
    version("1.45.5", sha256="d39179b7dc07fdf70fdfe8c04c74fef321fdc0a75d41e1a628529461231d26cb")

    depends_on("go@1.20:")

    def install(self, spec, prefix):
        tags="seccomp  btrfs_noversion exclude_graphdriver_btrfs libdm_no_deferred_remove  systemd"
        make("TAGS={0}".format(tags), "install", "PREFIX={0}".format(prefix))
