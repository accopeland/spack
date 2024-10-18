# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Sq(GoPackage):
    """
    sq is a command line tool that provides jq-style access to structured data
    sources: SQL databases, or document formats like CSV or Excel.
    """

    homepage = "https://github.com/neilotoole/sq"
    url = "https://github.com/neilotoole/sq/archive/refs/tags/v0.48.3.tar.gz"

    license("MIT")

    version("0.48.3", sha256="46e75e2db83a6cbc98b07dbcfb23de03fc41b2b2cbc7de7aaee0425cef4fb9bb")
    version("0.48.1", sha256="5207f3cf86e90877efb025f7b44530b39e082cc2e4c27741a261ea84ee5fdfa3")
    version("0.47.4", sha256="d75f745ca2360d79d1a6dc76d3e43348ae8f61b77daa4793b4b4a28113001765")
    version("0.47.3", sha256="57297d480bf44db2e6b9a04ff1475f42836ab98f2d543263222b907b5222d225")
    version("0.47.2", sha256="3ff0208439e2c9b51384b73cec3bffdbc565dcfd75ba7521b04a477e9ca2c9ba")
    version("0.47.1", sha256="ee1d74cf6e8ad917249267efe3c20d00c5b284982d090296c7d0d92fa445a39e")
    version("0.47.0", sha256="047f26c9c739d978a7f32cf51b80009be41f8e45decf24999c61cce5a25fa531")
    version("0.46.1", sha256="ce376e021e3753b8b6a9733c4374b28117cf619ccf837d50b7753d6dc1abac71")
    version("0.46.0", sha256="ee3d857113baf14a95da277d20b840c233ec8015c40cc05a296f63c975cc9906")
    version("0.45.0", sha256="d1067ee9d8e0a8ca0f4a857205e97dfde7eca8489527ac7df5f7aab6a3bb8335")
