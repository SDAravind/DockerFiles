# USAGE

1) Install Docker on your machine from **[here](https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe)**
2) Double click on `START` provided in the `repo` that builds and runs `webdev` container with below items
    -   Uses `node:lts-slim` from [here](https://hub.docker.com/_/node)  
    -   Sets `/usr/share/webdev` as `Work Directory`  
    -   Installs `git` and a npm package `docsify-cli` globally  
    -   Clone [Microsoft Web Development](https://github.com/microsoft/Web-Dev-For-Beginners) to `Work Directory`  
    -   Runs `docsify serve` on port `3000`  
    -   Creates a container with `webdev` tag  
    -   Opens http://127.0.0.1:3000 in the default browser
3) That's all !!!
4) Happy Learning!!!