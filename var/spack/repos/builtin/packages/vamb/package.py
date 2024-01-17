# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Vamb(PythonPackage):
    """Variational autoencoder for metagenomic binning"""

    homepage = "https://github.com/RasmussenLab/vamb"
    #url = "https://github.com/RasmussenLab/vamb/archive/refs/tags/v4.1.3.tar.gz"
    pypi = "vamb/vamb-4.1.3.tar.gz"

    version("4.1.3", sha256="b559853c32bb56490049fb8a85bf574bce16a356045407f8c28973ea98878786")
    version("4.1.2", sha256="5c107ea01ab2bc22924658241875d749558e5707376d69919f4ed6d35c68707b")
    version("4.1.1", sha256="e5374ac411ae66f052a8924626cc988060b7d09258c287a7ce455696717f9d86")
    version("4.1.0", sha256="e412bd75a42fce9f18fd6f37e594460b8da5498c540d153246b63b95fcd7175c")
    version("4.0.1", sha256="7696178e34203d1f3080e200c4c27b0cff6afba84de47188af5ba23c094350c9")
    version("4.0.0", sha256="9a2603296fc590d409129b6d2a4498c63ddac0eacaf94b010ec6ece681c0e6c4")
    version("3.0.9", sha256="20de5eb619931c02c8ed47d96bb09585405696347956feb0861c4fc97d97ef1d")
    version("3.0.8", sha256="fe75e3ba080f23bbf52bb06e7029f7cf2311b2945482c61a317be5c7577e9a0b")

    # Currently pycoverm does not have binaries for Python > 3.11.
    # The dependency resolver, will not error on Python 3.11, but attempt
    # to build pycoverm from source, but will not get the deps required for that.
    #requires-python = "<3.12,>=3.9.0"

    # build
    depends_on("python@3.9:3.11", type=("build", "run"))
    depends_on("py-cython@0.29.5", type="build")
    depends_on("py-setuptools@64.0", type="build")
    depends_on("py-setuptools-scm@8.0", type="build")
    depends_on("py-pip@:23.0", type="build")
    depends_on("py-cython@0.29.5", type="build")

    # run
    #depends_on("py-numpy@1.24.2", type="run")
    #depends_on("py-torch@1.13.1", type="run")
    #depends_on("py-pycoverm@0.6.0", type="run")
    #depends_on("py-networkx@3.1", type="run")
    #depends_on("py-scikit-learn@1.2.2", type="run")
    #depends_on("py-pandas@2.0.0", type="run")
    #depends_on("py-dadaptation@3.0", type="run")
    #depends_on("py-loguru@0.7.2", type="run")
