
from spack.package import *


class Ssdeep(AutotoolsPackage):
    """"Fuzzy hashing API and fuzzy hashing tool"""

    homepage = "https://www.example.com"
    url = "https://github.com/ssdeep-project/ssdeep/archive/refs/tags/release-2.14.1.tar.gz"

    license("UNKNOWN")

    version("2.14.1", sha256="d96f667a8427ad96da197884574c7ca8c7518a37d9ac8593b6ea77e7945720a4")
    version("2.14", sha256="7ebc488c2fa8aa3d9d5452542089fa7c8ed5a13fc21f23ab59021e7a47b2246a")
    version("2.13", sha256="8e3f3e1daad90aa24bbee94841dad8bb2344b3a988947d6b3a3b4b911b586f38")
    version("2.12", sha256="ce10e4396ba2a1a017976985b40bcd391408efe84dd4d534a8cc0e901515f948")
    version("2.11.1", sha256="06b560ac6d179033f4808537d6d66cf3c5d85df0ff2acd97fec597fbb072461a")
    version("2.11", sha256="f92fceb8a7f3c54a04370583a8053f360db5d637234198fbd3494d17bc2c2f82")
    version("2.10", sha256="520a66089fdbcbdaddb9ce53ff163bb54c26631ce088c753a71721bfd750c1e5")
    version("2.9", sha256="06fb69a42c2e5bccdea9f80dcb6e9208944e2fe6faf2f505567a4ac161989412")
    version("2.8", sha256="3485a8dc3f9b271099f09f8b04b24cc3c1f66b8bfa92080d30d7d5ec48e6134d")
    version("2.7", sha256="309884e82fb2a12c356f9a3f8fd7d5d62b927fb1b080228f10763a63540c3d5d")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")

    def autoreconf(self,spec,prefix):
        autoreconf("--install")

