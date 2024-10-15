# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Globusconnectpersonal(Package):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://docs.globus.org/how-to/globus-connect-personal-linux/"
    url = "https://downloads.globus.org/globus-connect-personal/linux/stable/globusconnectpersonal-latest.tgz"

    version("latest", "172f224d54df196ba18c702f6dd795de")

    depends_on("tk")
