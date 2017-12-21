# [ReviewImprove](http://ec2-54-146-255-108.compute-1.amazonaws.com)
Analyzing better online reviews to empower users


**Authors:**
[Brendan Davis](https://github.com/Tsarcastic),
[Carson Newton](https://github.com/nosrac77), and
[Marco Zangari](https://github.com/marco-zangari)


We analyze online reviews to empower users. Online reviews are helpful except when they are not. We aim to make sure that before you read a site's reviews you receive a comprehensive review-score to know whether you should spend your time at the site's reviews or not.

## App Navigation

Point your browser at the site: [ReviewImprove](http://ec2-54-146-255-108.compute-1.amazonaws.com).


## Resources Used

#### AWS specific services:
[Hosting on AWS EC2](https://aws.amazon.com/ec2/?hp=tile&so-exp=below)
[Amazon Webservice - S3](https://aws.amazon.com/s3/?hp=tile&so-exp=below)
[RDS PostGres](https://aws.amazon.com/rds/postgresql/)

#### Other Services & Frameworks
[Ansible](https://www.ansible.com/integrations/cloud/amazon-web-services)
[Django](https://www.djangoproject.com/)

## Future goals

To add more categories beyond movies is a goal of ReviewImprove. We aim to be a clearing house for analyzing online reviews.

## Contributing

If you want to contribute, fork the repo: (https://github.com/TeamAlphaPrimeReviews/reviews-to-improve).

## Testing

To set up a virtual environment for your testing suite, follow these instructions:
```
pip install virtualenv
```

Make a directory to do your testing work. You can name it whatever you want, but here we name it review-improve. Once you've made your directory, enter the new directory:
```
mkdir reviewimprove-environment && cd reviewimprove-environment
```

Make your virtual environment and create its file system by activating it:
```
pyvenv ENV && source ENV/bin/activate
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
