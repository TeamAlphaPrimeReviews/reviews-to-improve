# [Review Improve](https://github.com/TeamAlphaPrimeReviews)
Building better online reviews to empower users.
# [![Build Status](https://travis-ci.org/TeamAlphaPrimeReviews/reviews-to-improve.svg?branch=master)](https://travis-ci.org/TeamAlphaPrimeReviews/reviews-to-improve)


**Authors:**
[Brendan Davis](https://github.com/Tsarcastic),
[Carson Newton](https://github.com/nosrac77), and
[Marco Zangari](https://github.com/marco-zangari)


We analyze online reviews to empower users. Online reviews are helpful except when they are not. We aim to make sure that before you read a site's reviews you receive a comprehensive review-score to know whether you should spend your time at the site's reviews or not.

## App Navigation


Point your browser at the site: [Review Improve](http://ec2-54-146-255-108.compute-1.amazonaws.com).


## Resources Used

#### AWS specific services:
[Hosting on AWS EC2](https://aws.amazon.com/ec2/?hp=tile&so-exp=below)
[Amazon Webservice - S3](https://aws.amazon.com/s3/?hp=tile&so-exp=below)
[RDS PostGres](https://aws.amazon.com/rds/postgresql/)

#### Other Services & Frameworks
Automate updating your EC2 instance:
[Ansible](https://www.ansible.com/integrations/cloud/amazon-web-services)

A dynamic Python webframework to manage all your modules:
[Django](https://www.djangoproject.com/)

Frontend web service with ready-to-use html and css:
[Bootstrap](https://startbootstrap.com/)

Favicon created with:
[favicongenerator](https://www.favicongenerator.com/)

#### Language & Data Processing

The main language used:
[Python3.6](https://www.python.org/downloads/)

Scraped the web with:
[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)

Analyzed the data with:
Used the natural language toolkit - [Nltk](http://www.nltk.org/data.html)
And also the scikit for handling our classification models - [scikit-learn](http://scikit-learn.org/stable/)


## Future goals

To add more categories beyond movies is a goal of ReviewImprove. We aim to be a clearing house for analyzing online reviews.

## Contributing

If you want to contribute, fork the repo: [Review Improve Repo](https://github.com/TeamAlphaPrimeReviews/reviews-to-improve).

## Testing

Make a directory to do your testing work. You can name it whatever you want, but here we name it review-improve. Once you've made your directory, enter the new directory:
```
mkdir reviewimprove-environment && cd reviewimprove-environment
```

Make your virtual environment for your testing suite and create its file system by activating it:
```
python -m venv ENV && source ENV/bin/activate
```

Install pytest:
```
pip install pytest
```
To read more: [Pytest](https://docs.pytest.org/en/latest/)

Install pytest coverage:
```
pip install pytest-cov
```
To read more: [Pytest-cov](https://pypi.python.org/pypi/pytest-cov)

You can deactivate your environment at any time by simply typing in your command line:
```
deactivate
```
