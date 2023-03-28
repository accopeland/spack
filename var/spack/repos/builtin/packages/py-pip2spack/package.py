# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPip2spack(PythonPackage):
    """Automatically create and update a spack package base on the pypi.org information"""

    homepage = "https://github.com/NexSabre/pip2spack"
    #url = "https://files.pythonhosted.org/packages/38/4f/8b17084af5419ddcf801d035896b48481d9aa6b3ff844a10f3b8ec55276d/pip2spack-1.4.1.tar.gz"
    pypi = "pip2spack/pip2spack-1.4.1.tar.gz"
    version("1.4.1", sha256="38a9c6e04c9344be6d308214d99c57e3586e3b482037cc7d4a692280c1543dbe")

    depends_on("py-setuptools", type="build")
    #depends_on("python@3.6:", type=("build", "run"))
