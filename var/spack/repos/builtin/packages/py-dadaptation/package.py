
# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDadaptation(PythonPackage):
    """
    Learning rate free learning for SGD, AdaGrad and Adam!
    """

    homepage = "https://github.com/facebookresearch/dadaptation"
    pypi = "dadaptation/dadaptation-3.2.tar.gz"

    version("3.2", sha256="de8e8289d56bfdee0c8e3ca353143295d8a48363bcb02d6868a708354b47ccc0")
    version("3.1", sha256="aa4159c99f31b4103a530cf9e7a1b776912e61c317ff684b271751d4d1832df7")
    version("3.0", sha256="8081d076aa70b59672d202b0fa2d5f07e3744cff58a95b6d9eb86e3fd864e6fb")

    # build
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools@64.0:", type="build")
    #depends_on("py-setuptools-scm@8.0", type="build")
    #depends_on("py-pip@:23.0", type="build")
    #depends_on("py-cython@0.29.5", type="build")
    # run
    depends_on("py-torch", type="run")
    #depends_on("py-numpy@1.24.2", type="run")
    #depends_on("py-coverm@0.6.0", type="run")
    #depends_on("py-networkx@3.1", type="run")
    #depends_on("py-scikit-learn@1.2.2", type="run")
    #depends_on("py-pandas@2.0.0", type="run")
    #depends_on("py-dadaptation@3.0", type="run")
    #depends_on("py-loguru@0.7.2", type="run")
