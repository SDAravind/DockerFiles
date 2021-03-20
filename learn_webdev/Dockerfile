FROM node:lts-slim
WORKDIR /usr/share/webdev
RUN apt update && apt install git -y \
&& npm i docsify-cli -g \
&& git clone https://github.com/microsoft/Web-Dev-For-Beginners.git .\
&& rm -rf /var/lib/apt/lists/*

CMD ["docsify", "serve"]

# ######### COMMANDS TO RUN #########
# docker build --no-cache -t webdev .
# docker run -dit --name webdev -p 3000:3000 webdev
# open http://127.0.0.1:3000 in the browser