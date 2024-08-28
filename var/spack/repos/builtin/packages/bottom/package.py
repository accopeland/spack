# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Bottom(CargoPackage):
    """Yet another cross-platform graphical process/system monitor."""

    homepage = "https://github.com/ClementTsang/bottom"
    url = "https://github.com/ClementTsang/bottom/archive/refs/tags/0.9.7.tar.gz"

    license("MIT")

    version("0.9.7", sha256="29c3f75323ae0245576ea23268bb0956757352bf3b16d05f511357655b9cc71e")
    version("0.9.6", sha256="202130e0d7c362d0d0cf211f6a13e31be3a02f13f998f88571e59a7735d60667")
    version("0.9.5", sha256="538a8fce1f9a65c1c84811f0b89db083301fea06364ff725cca1a776b9e4ee3c")
    version("0.9.4", sha256="199123ef354bcabaa8a2e3b7b477b324f5b647d503a2599d08296733846eea6e")
    version("0.9.3", sha256="53a1466c3d2ed8f38401e8929cf2da796e703e4d70339d215f855b2304c07f72")
    version("0.9.2", sha256="c6b1f6eefa814607cbc6f1ebf6358a070293413d09583963970d650b724a3b3a")
    version("0.9.1", sha256="15136784ba4783c994bbfc1fe978ccf47360b2f2aa14ce37f8d5f93871ec9d57")
    version("0.9.0", sha256="0b5ba825905748a6146307517cf5e148bbc7ce13070a8448cc2d38ee68c1a42c")
    version("0.8.0", sha256="0fe6a826d18570ab33b2af3b26ce28c61e3aa830abb2b622f2c3b81da802437a")

    depends_on("rust@1.70:", type="build")
