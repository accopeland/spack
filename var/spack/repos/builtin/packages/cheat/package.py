# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *

class Cheat(MakefilePackage): 
    """ 
    cheat allows you to create and view interactive
    cheatsheets on the command-line. It was designed to help remind *nix system
    administrators of options for commands that they use frequently, but not
    frequently enough to remember.  
    """

    homepage = "https://github.com/cheat/cheat"
    url = "https://github.com/cheat/cheat/archive/refs/tags/4.4.2.tar.gz"

    license("MIT")

    version("4.4.2", sha256="6968ffdebb7c2a8390dea45f97884af3c623cda6c2d36c4c04443ed2454da431")
    version("4.4.1", sha256="cca7f3d631de38ef1b4f36a5dc76d52d091611d38074ff2522a1a8b36f34a182")
    version("4.4.0", sha256="8694d75896dcb1dfb91ed95ec37f7fe409ad2bde76e66f80b20be24ee92ae3ec")
    version("4.3.3", sha256="6a1739b71d436f45dc7c028ec79863a34e30cc13da7159bf23604b77f43faaf2")
    version("4.3.2", sha256="ea40ebfef2d126c627e39a4e3c2aaf3a6b9bcf6489992430fb30fb42b13dab16")
    version("4.3.1", sha256="10011b4dd8e66976decd7f3252e3221cb2c5a290740648ac3a70f3b20bac3109")
    version("4.3.0", sha256="1e5bbaeca1bd3406afb03d696bd5e250189b4e11574c0077554150c2f054b8ce")
    version("4.2.7", sha256="124ddb6aeefdd954bbb8ab71c6da35a7c75cfabda55c437b0f00a10bfde50084")
    version("4.2.6", sha256="597b6fbfe09fa3db232ede9053dded7c3a0fca0bb7a32fbcdca956eb4c94ef46")
    version("4.2.5", sha256="727c19efb873e6ea29b922a480074da8e5b73a0d129c3277539484a736527033")

    depends_on("go@1.22:", type="build")
