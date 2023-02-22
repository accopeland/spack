# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Bbtools(Package):
    """Brian Bushnell's bbtools package (java)"""

    homepage = "https://jgi.doe.gov/data-and-tools/software-tools/bbtools/"
    url      = "https://sourceforge.net/projects/bbmap/files/latest/download/BBMap_38.96.tar.gz"

    # notify when the package is updated.
    maintainers = ['bbushnell@lbl.gov']

    version('38.96', sha256='18d9c89b02c0ab044b2795a65f6236b2262a494ed83d27e31750437b350ef080')

    depends_on('openjdk')

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        mkdirp(prefix.libexec)
        mkdirp(prefix.share)

        install("*.sh", prefix.libexec)
        install("*.sh", prefix.bin)
        #install("*.doc", prefix.share)

    def setup_run_environment(self, env):
        env.prepend_path("bbtools", join_path(self.prefix.bin))
