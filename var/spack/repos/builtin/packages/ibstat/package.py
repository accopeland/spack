from spack.package import *


class Ibstat(AutotoolsPackage):
    """infiniband-diags is a set of utilities designed to help configure, debug, and
maintain infiniband fabrics.  Many tools and utilities are provided.  Some with
similar functionality.
"""

    homepage = "https://github.com/weiny2/infiniband-diags"
    url = "https://github.com/weiny2/infiniband-diags/archive/refs/tags/1.6.7.tar.gz"

    version("1.6.7", sha256="e4cec41c3d2eef748432c75603a223fe55eb80b97c2ae00f5fe648edb0e541aa")

    depends_on("autoconf", type="build", when="@1.6.7 build_system=autotools")
    depends_on("automake", type="build", when="@1.6.7 build_system=autotools")
    depends_on("libtool", type="build", when="@1.6.7 build_system=autotools")
