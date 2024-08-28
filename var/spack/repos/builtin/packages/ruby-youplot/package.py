from spack.package import *

class RubyYouplot(RubyPackage):
    """A command line tool that draw plots on the terminal."""

    homepage = "https://github.com/red-data-tools/YouPlot"
    #url = "https://github.com/red-data-tools/YouPlot/archive/refs/tags/v0.4.5.tar.gz"
    url = "https://rubygems.org/downloads/youplot-0.4.5.gem"

    license("MIT")

    version("0.4.5", sha256="31b7a5d38a0924953e77a5cc8d463106c1282e457fddea1dbeb3bd297931be46", expand=False)
    version("0.4.4", sha256="71eff9e2d510d3d34bc0d660ed377a3476cab6d6d3e1a20e004c63972140861b")
    version("0.4.3", sha256="e68ba1b800bfe5b3f066e58e872761c118b556472eb537371b46d53f29fc6d30")
    version("0.4.2", sha256="379f72c2c2592b52d7ffe50c5f3dc7c4a18c630ce1cf8b74b80184627b014ab1")
    version("0.4.1", sha256="a7126edf92e615c3f099a58d709199a71ff2daa6292ee43b18f9a02b3783941a")
    version("0.4.0", sha256="28042bf099c7e97379265d0be350dc062322bba940c41e89acbb56e6b5f96c4f")
    version("0.3.5", sha256="5abfbdf75b5b72b83fd565d33de565759dd53a4ed0a480c2cc4d9d5d5df34db1")
    version("0.3.4", sha256="25a6df332321dcf32d6e28720e6316b48e40a25a83000c38135b0023fec407bd")


    depends_on("ruby-unicode-plot", type="run") # >=0.0.5
