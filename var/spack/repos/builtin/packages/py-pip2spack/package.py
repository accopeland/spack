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

    """
    FIXME

     '/clusterfs/jgi/groups/gentech/genome_analysis/spack-fork/spack/opt/spack/linux-rocky8-zen2/gcc-14.2.0/python-venv-1.0-hns6p2ximsigvcfxsnrp4xtzoxu6iz4n/bin/p
ython3' '-m' 'pip' '-vvv' '--no-input' '--no-cache-dir' '--disable-pip-version-check' 'install' '--no-deps' '--ignore-installed' '--no-build-isolation' '--no-war
n-script-location' '--no-index' '--prefix=/clusterfs/jgi/groups/gentech/genome_analysis/spack-fork/spack/opt/spack/linux-rocky8-zen2/gcc-14.2.0/py-pip2spack-1.4.
1-mjpkl34b4rm2cf6sqg4uroz7lrzbgryf' '.'

1 error found in build log:
     64          setup_py_code = "from setuptools import setup; setup()"
     65
     66      exec(compile(setup_py_code, filename, "exec"))
     67      '"'"''"'"''"'"' % ('"'"'/tmp/accopeland/spack-stage/spack-stage-py-pip2spack-1.4.1-mjpkl34b4rm2cf6sqg4uroz7lrzbgryf/spack-src/setup.py'"'"',), "<pi
           p-setuptools-caller>", "exec"))' egg_info --egg-base /tmp/pip-pip-egg-info-t4gc7eed
     68      cwd: /tmp/accopeland/spack-stage/spack-stage-py-pip2spack-1.4.1-mjpkl34b4rm2cf6sqg4uroz7lrzbgryf/spack-src/
     69      Preparing metadata (setup.py): finished with status 'error'
  >> 70    error: metadata-generation-failed
     71
     72    × Encountered error while generating package metadata.
     73    ╰─> See above for output.
     74
     75    note: This is an issue with the package mentioned above, not pip.
     76    hint: See above for details.

     """
