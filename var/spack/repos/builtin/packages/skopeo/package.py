# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Skopeo(MakefilePackage):
    """
    skopeo is a command line utility that performs various operations on
    container images and image repositories.
    """

    homepage = "https://github.com/containers/skopeo"
    url = "https://github.com/containers/skopeo/archive/v0.1.39.tar.gz"

    license("Apache-2.0")

    version("1.14.1", sha256="b174ada87751ecd7f8e0e292d163c9b0c4a2172a6ba32e1725ae272c24f7f841")
    version("1.14.0", sha256="062ca24dcc106c3758e90a4af207b67166437ab71128bd33749b0414e0a42f79")
    version("1.13.3", sha256="0b788fc5725ac79327f7c29797821a2bafc1c3c87bbfcb2998c2a1be949e314d")
    version("1.13.2", sha256="1b5e7b4fcbc3b0ba5637793605a5bdc6372ec11e60306aef0ed29ec1fd64893f")
    version("1.13.1", sha256="8e7195ff1c71c26f3e4b61d93239424b27293c2b3f9b8d67279b9ffd8adbbeca")
    version("1.13.0", sha256="65c90d5ba55a5075e56f9a4a5d96a46ca4c443f4cd2701c2eabb9592ba3460ce")
    version("1.12.0", sha256="f7bbb3748eeb0c29abf5bfe9b1c1a149464c4ea65705e25686df3b9bcbd7bb89")
    version("1.11.2", sha256="c7d0b0d1c379ae51e03e32ec31e243257d66de810d73704b7e9ac0e87cbec745")
    version("1.11.1", sha256="7e2b327a687d2230e9075120fff1024e6c2f22738a4179030121c953dda7d3b5")
    version("1.6.3", sha256="02aa74821e231134f1dcab86e1f29177d30f0d9a898e0d211513dca09007deb1")
    version("0.1.40", sha256="ee1e33245938fcb622f5864fac860e2d8bfa2fa907af4b5ffc3704ed0db46bbf")
    version("0.1.39", sha256="e9d70f7f7b891675a816f06a22df0490285ad20eefbd91f5da69ca12f56c29f2")
    version("0.1.38", sha256="104ceb9c582dc5c3a49dd1752c4c326bba03f2f801596f089372e831f48ed705")
    version("0.1.37", sha256="49c0c1b2c2f32422d3230f827ae405fc554fb34af41a54e59b2121ac1500505d")
    version("0.1.36", sha256="42f9b0bf53ae44bc294be400e2c5259f977ffa4d5dbac3576b0b5e23d59791fd")

    depends_on("c", type="build")  # generated

    depends_on("go")
    depends_on("go-md2man", type="build")
    depends_on("gpgme")
    depends_on("libassuan")
    depends_on("libgpg-error")
    depends_on("lvm2")

    def edit(self, spec, prefix):
        #CONTAINERSCONFDIR ?= /etc/containers
        #REGISTRIESDDIR ?= ${CONTAINERSCONFDIR}/registries.d
        #LOOKASIDEDIR ?= /var/lib/containers/sigstore
        makefile = FileFilter("Makefile")
        makefile.filter(r"/usr/local", self.prefix)
        makefile.filter(r"/etc/containers", f"{prefix}/etc/containers")
        makefile.filter(r"/var/lib/containers", f"{prefix}/var/lib/containers")

    def install(self, spec, prefix):
        make("binary", "install", "PREFIX={0}".format(prefix))
