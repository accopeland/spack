# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Jaq(CargoPackage):
    """A jq clone focussed on correctness, speed, and simplicity"""

    homepage = "https://github.com/01mf02/jaq"
    url = "https://github.com/01mf02/jaq/archive/refs/tags/v1.2.0.tar.gz"

    license("MIT")

    version("1.2.0", sha256="3895dda6c808d93353bdcf3d265613c2c2fcdbbb20b1177bda8bb95fc0078277")
    version("1.1.2", sha256="26a4dd9b74a98f2c94283d3d0c8ec559ab2139a051997e0aa099cec5585e06bb")
    version("1.1.1", sha256="0969ff3f149354cd94326d8c1eac199be53127506ef6e5b823ae4e44c092ce44")
    version("1.1.0", sha256="40d334016d06a9f471220f8369815d2ce086e151ca3638ded9babbc94efe19bc")

    depends_on("rust@1.71:", type="build")

    def install(self, spec, prefix):
        cargo("build", "--release") # places binary into target/release/jaq
        cargo("install", "--locked","--root", prefix,  "--path", "jaq")  # installs binary
