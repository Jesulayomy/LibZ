<div align="center">

  <img src="https://readme-typing-svg.herokuapp.com?font=comic+sans+ms&size=32&duration=2000&pause=100000&color=FC440F&width=435&lines=LibZ+-+The+Public+Library" alt="LibZ - The Public Library" />

</div>


## Installation

#### Dependencies
> Python 3.10.11

> MySQL 8.0.32

> Node 16.20.2

> npm 8.19.4

#### Requirements
All requirements are stored in the `requirements.txt` [file](test/requirements.txt). To install them, run the following command:
```bash
pip install -r requirements.txt
```

##### Running the API server
For production environment, use the `gunicorn` module to run the server. For development environment, use the `flask` module to run the server. To run the server, run the following command:

```bash
cd api/
flask run
```

```bash
gunicorn --workers=3 --access-logfile access.log --error-logfile error.log --bind 0.0.0.0:5000 api.app:app
```

##### Running the React app
First, install all the dependencies using the following command:
```bash
cd libz
npm install
```

Then, run the following command to start the React app:
```bash
npm start
```

## Contributors
<table>
  <tr>
  <td align="center"><a href="https://github.com/Jesulayomy"><img src="https://avatars.githubusercontent.com/u/113533393?s=96&v=4" width="80px;" alt=""/><br /><sub><b>Jesulayomy</b></sub></a></td>

  <td align="center"><a href="https://github.com/micoliser"><img src="https://avatars.githubusercontent.com/u/108087255?v=4" width="80px;" alt=""/><br /><sub><b>micoliser</b></sub></a></td>
  </tr>
</table>
