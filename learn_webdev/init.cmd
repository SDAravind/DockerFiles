TITLE Learn Web Dev
CMD /c "cls & docker build -t webdev . & docker run -dit --name webdev -p 3000:3000 webdev & TIMEOUT /t 3 /nobreak & START http://127.0.0.1:3000"