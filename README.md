# https://docs.scrapy.org/en/latest/
# https://thepythonscrapyplaybook.com/videos/

# Create A Python Virtual Environment

-> The commands are valid only for a Windows environment; USE CMD to run the commands

* Create Virtual Environment
RUN `python -m venv env`

* Activate Virtual Environment
RUN `env\Scripts\activate.bat`

* Deactivate Virtual Environment
RUN `deactivate`


# Create a Scrapy Spider Project

-> Instal the scrapy module first
RUN `pip install scrapy`

-> Create a scrapy project
RUN `scrapy startproject project-name`

-> Start the first spider with
RUN `cd project-name`
RUN `scrapy genspider spider-name url-for-spider-to-scrape`

-> Find items from the page
RUN `scrapy shell`

-> Fetch the data
RUN `fetch('https://www.chocolate.co.uk/collections/all')`

-> Running the spider
RUN `scrapy crawl chocolatespider`

-> Running the spider and save the output in a file
/* The capital -O will overwrite the previous data */
RUN `scrapy crawl chocolatespider -o mydata.json`
RUN `scrapy crawl chocolatespider -O mydata.json`

-> Running the spider and upload the data to AWS S3 bucket
RUN `scrapy crawl chocolatespider -O s3://aws_key:aws_secret@mybucket/path/to/myscrapeddata.csv:csv`

