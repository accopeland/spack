# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Coz(CMakePackage):
    """Coz is a new kind of profiler that unlocks optimization opportunities missed by traditional profilers. Coz employs a novel technique we call causal profiling that measures optimization potential. """

    # sudo apt-get install build-essential cmake docutils-common git python3 pkg-config
    #git clone https://github.com/antoyo/libelfin && cd libelfin && make && sudo make install && cd ..
    #git clone https://github.com/plasma-umass/coz && cd coz && cmake . && make && sudo make install && cd ..
    # Next, you need to change the "perf_event_paranoia" level so Coz can run.
    # sudo sh -c 'echo 1 >/proc/sys/kernel/perf_event_paranoid'

    homepage = "https://github.com/plasma-umass/coz"
    url = "https://github.com/plasma-umass/coz/archive/refs/tags/0.2.2.tar.gz"

    version("0.2.2", sha256="5e671c5b7e2920e295d2da793e5eb4d60b36889fd86c9dc40cacfe0d3ec24d0f")

    depends_on("python@3", when="run")
    depends_on("pkg-config", when="build")
    depends_on("libelfin", when="run")
    
    #def cmake_args(self):
    #    # FIXME: Add arguments other than
    #    # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
    #    # FIXME: If not needed delete this function
    #    args = []
    #    return args
