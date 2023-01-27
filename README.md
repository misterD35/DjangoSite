# Very Simple Site on Django
[![Generic badge](https://img.shields.io/badge/Python-3.10-green.svg)](https://www.python.org/)  [![Docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://https://docker.com/)



Hello!:hand:

This is simple web service on ***Django*** which shows main features of this framework. Also based on ***Python*** and ***Docker***.
___


## Description
Simple site on ***Django*** contain some related sections with active ___links___, danger and warning ___buttons___ , ___images___ :evergreen_tree:, local ___data base___ with articles with ability to add new one. This functions client can use. But if you add to main ip adress and go to `127.0.0.1:8000/admin`, you can redact and delete added acticles.

*It has the following **structure:***
* Main
* About us
* Contacts
* News
    >* 1-st news
    >* ...
    >* last news
* Add article 
    * Name
    * Annotation
    * Text
___

## Installation
1. Create folder in your Docker and add this project there.
2. Go to this folder with command `cd`
3. Build image. Type in your terminal:
```
   docker build -t django_site .
```
4. Create container, run it and delete after working
```
   docker run --rm -it -dp 8000:80 --name DJ_Django django_site
```
5. Define your machine IP and go to browser adress `your_ip:8000`
___

## Technologies
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)   ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)   ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)   ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)   
- [x] [Python](https://www.python.org/) 3.10  :snake: 
- [x] [Django](https://www.djangoproject.com/) 4.1.5
- [x] [Docker](https://www.docker.com/) 20.10.22  :whale:
- [x] HTML
___

## License
Apache-2.0



<img src="https://cdn-icons-png.flaticon.com/512/919/919852.png?w=740&t=st=1674815666~exp=1674816266~hmac=d8675dffadfc01e1bb6ec97b220b11c5e004da72099526ebc7569461b3b0ce53" width="150" height="150" >   <img src="https://cdn.pixabay.com/photo/2014/05/07/15/19/django-339744_960_720.png" width="250" height="150" >
