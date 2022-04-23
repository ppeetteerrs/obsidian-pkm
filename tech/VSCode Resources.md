## Settings
- C++ Formatter Settings: [Clang format style options](https://clang.llvm.org/docs/ClangFormatStyleOptions.html)(for `.clang-format` or VSCode settings)
- Favourite mono font with font ligatures: [Microsoft Cascadia Code](https://github.com/microsoft/cascadia-code)

## Note
- Command substitution does not work in `devcontainer.json`, which is pretty sad ([reference](https://github.com/microsoft/vscode-remote-release/issues/1050))

## Weird Issues
1. When using (WSL2) + remote host + devcontainer ==> `localEnv` need to be set in `.bash_profile` not `.bashrc` because VSCode runs  a login shell (?) through ssh everytime