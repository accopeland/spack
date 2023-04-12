# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlLibnet(PerlPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://cpan.metacpan.org/authors/id/S/SH/SHAY/libnet-3.15.tar.gz"

    version("3.15", sha256="a71f4db580e1a767d6936faa5baf38f1fa617824342da078b561283e86f8f4a2")
    version("3.14", sha256="153c8eb8ef0f19cf2c631d5b45d05de98516937f34e261125ef242fba1fe2ea4")
    version("3.13", sha256="5a35fb1f2d4aa291680eb1af38899fab453c22c28e71f7c7bd3747b5a3db348c")

    # FIXME: Add dependencies if required:
    # depends_on("perl-foo", type=("build", "run"))

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
