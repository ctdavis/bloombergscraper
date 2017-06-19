This is a Scrapy webcrawler that I built to scrape articles from Bloomberg.com. It's deployed using Docker and is linked to a MongoDB container. Assuming you have docker, you can try it out with the following code:

    docker pull tsaed/bloombergscraper
    docker-compose run web scrapy crawl bloomberg -a section=stocks -a depth=10

    # if you want to check out what's in the database, execute this:

    docker exec -it bloomberg_db_1 mongo --shell

    # ...and once you're inside the shell, you can do something like this:

    show articles;
    db.bloomberg.find({text:/Trump/});

Otherwise, visit this page to install docker and then you can try it out.

The point of this project was simply to familiarize myself with Docker, which I really like due to the fact that I can now put projects like this online and not have to worry so much about people have difficulty with peripheral stuff (like installing a database server) if they want to try out some code.