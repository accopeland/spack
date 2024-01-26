# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import os

from spack.package import *


class Packer(GoPackage):
    """
    Packer is a tool for building identical machine images for multiple platforms from a single source configuration.
    """

    homepage = "https://github.com/hashicorp/packer"
    url = "https://github.com/hashicorp/packer/archive/refs/tags/v1.9.5.tar.gz"
    git = "https://github.com/hashicorp/packer.git"

    license("BULI-1")

    version("master", branch="master")
    version("1.10.0", sha256="d4f8c8741786c675b01a3be14dc24fb60baf69991908b1c4644277dae47cf946")
    #version("1.9.5", tag="v1.9.5", commit="6d28df4be6845e2e3216eab739904a4788acb172")
    version("1.9.5", sha256="a6da3e455578f5373c5e333023a7be483e9c22f4235ccd599fe39d42df55f870")
    version("1.9.4", sha256="c07db8375190668571077784f4a650514d6ef879ae45cb4c3c1717ad8308c47e")
    version("1.9.3", sha256="d13035521bb352b79fe9a09a0cb84f5d0a4619df06f71a5f8c22fbe6fbf922a4")
    version("1.9.2", sha256="16e5aa31892e917c18f866596c8fedd93e8631f72881997f20143bf2d22b91ee")
    version("1.9.1", sha256="1f3ae38fe9313a072547d1ce5674d74438ad5d59b042a87428534ac39bfd47b7")
    version("1.9.0", sha256="8502b551724d211bff75fbbbf8f2c5bcecfaf4c84caca2f64cda0a6918f0dd3d")
    version("1.8.7", sha256="0b3a45a3ecb0b5e993a0a39ee4599d69b58c1419cebddbfc45c61eb15389ba98")
    version("1.8.6", sha256="11acae341130dff0950a80e4c56df416d547298f42ca49e8e862de23afe1046f")

    depends_on("go@1.19:")

    # use ./scripts/build.sh ?
    # No, relies on gox and does 31 builds and assumes we are working in a git repo
    #patch("build_for_linux_amd64_only.patch")

    def build(self, spec, prefix):
        go("build","-o","bin/packer")

    #def url_for_version(self, version):
    #    path_to_package = os.path.join(os.path.dirname(__file__))
    #    return os.path.join(path_to_package,"v{}.tar.gz".format(version))

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        # binary will be in bin/packer
        install("bin/packer", prefix.bin)
