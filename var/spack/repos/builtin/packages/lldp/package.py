# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Lldp(AutotoolsPackage):
    """
    LLDP (Link Layer Discovery Protocol) is an industry standard protocol (IEEE 802.1ab)
    designed to supplant proprietary Link-Layer protocols such as Extreme's EDP
    (Extreme Discovery Protocol) and CDP (Cisco Discovery Protocol). The goal
    of LLDP is to provide an inter-vendor compatible mechanism to deliver
    Link-Layer notifications to adjacent network devices.
    """

    homepage = "https://github.com/lldpd/lldpd"
    url = "https://github.com/lldpd/lldpd/archive/refs/tags/1.0.18.tar.gz"

    license("ISC")

    version("1.0.18", sha256="e2ea97b4387165c768161626a370979baa977e3d3a43fe75bb05d2f76aa825ad")
    version("1.0.17", sha256="8ea4115e061e0dceac59761b84d21e025c48d424e632d09d1201cfdf79309bff")
    version("1.0.16", sha256="9bc6154377b97187d96d5e22aa5c4946c6cbc85f1416149853cc0940639a77e5")
    version("1.0.15", sha256="bdb1f9e29f61c3be99e421e88a431536c53e62f1ab7189a6d5b8e1d2d55d8899")
    version("1.0.14", sha256="0cb77fd7634401347b8311db1bf64d4fc3890acba90915e2cc2c5f79045ddbf0")
    version("1.0.13", sha256="4a167b2f197554185262f0e0da9f89810e2ab4598439493e176b85c74c328d8c")
    version("1.0.12", sha256="cabc3aeca31890eedbedbac11e9b39f12fc73d275ecc9d9de19f4864476f66c9")
    version("1.0.11", sha256="046b25e5125b6e37adc6953910537724664f971a20e862613063dd15f711342d")
    version("1.0.10", sha256="fa3d8063dd5802d10de8876a1d2d7987ef02d5ef204f2a338619d3be7f69126c")
    version("1.0.9", sha256="08adb528bb7a4fff1ff00c7ba65168b59cf351e5ba58b27c24e46e09f603667c")

    depends_on("c", type="build")
    depends_on("autoconf", type="build")
    depends_on("autoconf-archive", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("pkgconfig", type="build")
    depends_on("libevent", type="build")

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.append_path("ACLOCAL_PATH", self.prefix.share.aclocal) # Adds ACLOCAL path for autotools

    def autoreconf(self, spec, prefix):
        sh = which("sh")
        sh("./autogen.sh")
        autoreconf("--install","--verbose","--force")
