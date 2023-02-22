# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
# ----------------------------------------------------------------------------

from spack import *

class Easel(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://github.com/EddyRivasLab/easel" 
    url      = "https://github.com/EddyRivasLab/easel/archive/refs/tags/Bio-Easel-0.15.tar.gz"
    # maintainers = ['github_user1', 'github_user2']

    version('0.15', sha256='716911858008fb107ae7855b19e1408a2b780bb7881cf9044f5c0e161a4a4bc9')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    def autoreconf(self, spec, prefix):
        # FIXME: Modify the autoreconf method as necessary
        autoreconf('--install', '--verbose', '--force')

    def configure_args(self):
        args = []
        return args
