<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">Weather App</h3>

  <p align="center">
    A Django Application that consumes DarkSky weather API to show weather condition in Nairobi
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [License](#license)
* [Contact](#contact)


## About The Project

A Django Application that consumes DarkSky weather API to show weather condition in Nairobi.



### Built With

* []()Python
* []()Django



## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Python 3.7+

### Installation
 
1. Clone the repo
```sh
git clone https://timobure@bitbucket.org/timobure/weatherapp.git
```
2. Make a virtual environment
```sh
mkvirtualenv --python=python3.7 weatherapp
```
3. Install pip packages in the virtual env
```sh
pip install -r requirements.txt
```
4. Go to weatherapp -> settings.py and fill the empty 'DARK_SKY_API_KEY' variable with your key

5. CD into weatherapp dir and Fire up the django server
```sh
./manage.py runserver
```
 and view the result in 127.0.0.1:8000
6. To run test, 
```sh
./manage.py test
```

## License

Distributed under the MIT License. See `LICENSE` for more information.


## Contact

Timon Obure - timobure@gmail.com

Project Link: https://timobure@bitbucket.org/timobure/weatherapp.git