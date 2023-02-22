from spack.package import *

class Fpart(AutotoolsPackage):
    """Fpart is a Filesystem partitioner. It helps you sort file trees and pack them into bags (called "partitions"). It is developed in C and available under the BSD license."""

    homepage = "http://www.fpart.org"
    url = "https://github.com/martymac/fpart/archive/refs/tags/fpart-1.5.1.tar.gz"
    version("1.5.1", sha256="c353a28f48e4c08f597304cb4ebb88b382f66b7fabfc8d0328ccbb0ceae9220c")

    # git
    #url = "https://github.com/martymac/fpart.git"
    #version('1.5.1', tag='fpart-1.5.1') #, submodules=True

    depends_on('autoconf', type='build', when='@1.5.1 build_system=autotools')
    depends_on('automake', type='build', when='@1.5.1 build_system=autotools')
    depends_on('libtool', type='build', when='@1.5.1 build_system=autotools')
