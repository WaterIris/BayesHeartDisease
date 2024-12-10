{
  description = "Pytorch with cuda";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-24.05";
  };
  outputs = { self, nixpkgs }:
  
  let 
   pkgs = import nixpkgs { system = "x86_64-linux"; config.allowUnfree = true; };
  in
  { 
    devShells."x86_64-linux".default = pkgs.mkShell {
      LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
        pkgs.stdenv.cc.cc
        "/run/opengl-driver"
      ];
        
      venvDir = ".venv";
      packages = with pkgs; [
        python312    
        python312Packages.venvShellHook
        python312Packages.pip
        python312Packages.numpy
        python312Packages.pyqt6
      ];
        
    };
  };
}
