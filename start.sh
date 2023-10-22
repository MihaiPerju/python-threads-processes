docker build -t threads .
docker run -v $(pwd):/opt/bin -it threads sh