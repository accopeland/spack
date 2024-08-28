# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Nushell(CargoPackage):
    """
    A new type of shell built w rust
    """

    homepage = "https://github.com/nushell/nushell"
    url = "https://github.com/nushell/nushell/archive/refs/tags/0.88.1.tar.gz"

    license("MIT")

    version("0.88.1", sha256="19f5a46799142117f61989a76f85fdd24361fe9e5068565d7fff36b91a7a7a39")

    depends_on("rust@1.72:")

    # see https://github.com/nushell/nushell/blob/main/scripts/install-all.sh in nushell/scripts/install-all.sh
    def install(self, spec, prefix):
        #cargo = which("cargo")
        #  default = ["plugin", "which-support", "trash-support", "sqlite", "mimalloc"]:  stable wasi extra dataframe
        cargo("install", "--root", prefix, "--features", "dataframe,extra,wasi", "--locked", "--path",".")

    def install_plugins(self, spec, prefix):
        #cargo("install", "--force", "--path", prefix/crates/$plugin)
        #buildpath.glob("crates/nu_plugin_*").each do |plugindir|
          #next unless (plugindir/"Cargo.toml").exist?
          #system "cargo", "install", *std_cargo_args(path: plugindir)
        with working_dir(self.build_directory):
            mkdirp(prefix.crates)
            plugins_to_find = []
            plugins_to_find.append("nu_plugin_*")
            for plugin in plugins_to_find:
                plugins_to_install = glob.glob(os.path.join(self.build_directory, "**", plugin), recursive=True)
                for plugin_to_install in plugins_to_install:
                    install(plugin_to_install, prefix.crates)
