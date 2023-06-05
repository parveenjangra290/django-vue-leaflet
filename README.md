# Display Farmer location on map


This is a test project that display farmers location on map using Django restframework, Vue JS and leaflet JS.

## Getting Started


These instructions will get you a copy of the project up and running on your local machine for testing purposes. See deployment notes for how to deploy the project on system.

### Prerequisites


What things you need to install the software and how to install them

```
Python Version = 3.9
Django Version = 4.1.5
```

## Development Installations

### Ubuntu 20.04 LTS

Ubuntu development build instructions using an isolated virtual environment (tested on Ubuntu 20.04 LTS):

Install Ubuntu dependencies

```
sudo apt-get update
sudo apt-get install python3-virtualenv python3-dev libxml2 libxml2-dev libxslt1-dev zlib1g-dev libjpeg-dev libpq-dev
```

Create and activate the virtualenv

```
python3 -m venv api_test_env
source api_test_env/bin/activate
```
git clone https://github.com/parveenjangra290/django-vue-leaflet.git

```
git clone https://github.com/parveenjangra290/django-vue-leaflet.git
cd django-vue-leaflet
cd web_mapping
```
Install pip dependencies and run migrations

```
pip install -r requirements.txt
pip install -e

python manage.py migrate
python manage.py runserver
```

Run test cases
```
python manage.py test
```

You can also interact with the API using command line tools such as curl.
```
# Farmer List
curl --location --request POST 'http://localhost:8000/api/v1/farmers/' \
--header 'Content-Type: application/json'
```

For frontend, Install VueJS
```
npm install -g @cli/vue
vue create projectname
npm run dev
```

Install npm dependancies
```
npm install --save leaflet
npm install --save vue2-leaflet
npm install webpack-cli
npm install axios
```

Upload Farmer demo data
```
python manage.py upload_farmer -n Dev.csv
```
## Authors

* **Parveen Kumar**
