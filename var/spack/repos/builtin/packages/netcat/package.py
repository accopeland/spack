from spack.package import *

class Netcat(AutotoolsPackage):
    """ Rewrite of the well-known networking tool, but more portable, with new features and fully GNU compliant."""

    homepage = "https://www.example.co://netcat.sourceforge.net/download.php"
    url = "https://sourceforge.net/projects/netcat/files/latest/download/netcat-0.7.1.tar.gz"

    version("0.7.1", sha256="b55af0bbdf5acc02d1eb6ab18da2acd77a400bafd074489003f3df09676332bb")
