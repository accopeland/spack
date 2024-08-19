# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Netavark(CargoPackage):
    """
    Netavark is a rust based network stack for containers. It is being designed to work with Podman
    but is also applicable for other OCI container management applications.
    """

    homepage = "https://github.com/containers/netavark"
    url = "https://github.com/containers/netavark/archive/refs/tags/v1.11.0.tar.gz"
    license("APACHE")

    version("1.11.0", sha256="5b96e5a00a41a550d716f1e5c180df6e0ee5b0ce20961827ef17aff3d6a92f9c")
    version("1.10.3", sha256="fdc3010cb221f0fcef0302f57ef6f4d9168a61f9606238a3e1ed4d2e348257b7")
    version("1.10.2", sha256="5df03e3dc82e208dd49684e7b182ffe6c158ad9d9d06cba0c3d4820f471bfaa4")
    version("1.10.1", sha256="8870d36f87cfef802a6af06f64069397b7e69b0de0e6b0ba79c06d785c2e9bb7")
    version("1.10.0", sha256="35020dc6e5d45b0179e8590fe5b9c5f1a8cefc8e5ab94b6cd5447b86a85d1627")
    version("1.9.0", sha256="9ec50b715ded0a0699134c001656fdd1411e3fb5325d347695c6cb8cc5fcf572")
    version("1.8.0", sha256="b1422ef6927458e9f80f7d322b751e29ab5d04d8ed6cb065baa82fa4291af10f")
    version("1.7.0", sha256="b0ed7d80fd96ef2af88e7a001d91024919125e5842d9772de94648044630e116")
    version("1.6.0", sha256="3bec9e9b0f3f8f857370900010fb2125ead462d43998ad8f43e4387a5b06f9d6")
    version("1.5.1", sha256="090091aaa3151318e384911695ea647dd792c34f3a626a26f7f0efec252a8113")

    #depends_on("rust@1.78:", type="build")
    #depends_on("go-md2man", type="build")
    depends_on("protobuf", type="build")
