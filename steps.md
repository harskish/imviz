* `git submodule update --init --recursive`
* install C++ compiler
  - Windows: Build Tools for Visual Studio 2022 (or full IDE install)
    - https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2022
    - In installer: select at least `MSVC` and `Windows 10/11 SDK`
  - Linux: g++
* install miniconda
* `conda env create --force --file environment.yml`
* `conda activate imviz_build`
* `./extern/vcpkg/bootstrap-vcpkg.sh -disableMetrics`
* `python setup.py bdist_wheel`