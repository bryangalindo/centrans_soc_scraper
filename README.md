# Centrans Shipper Owned Container Tracker

Our Centrans SOC Tracker guarantees your container ends up in the correct depot, to be resold to other vendors. 
Auto updates status of your container from the following websites:
* Textainer
* Caru Containers
* Conglobal Industries
* Interport: Container Solutions
* UES International (HK) Holdings

Future versions will include auto-email options based on number of days after the posted last free day.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installing

Start by having [Postgres10](https://www.postgresql.org/download/) downloaded, along with PgAdmin4 for ease of restoring the SOCtracking.tar file. 

Deploy PgAmin4, and a window will open on your local host through your default browser:

![alt text](https://drive.google.com/open?id=12woL_x_WRPglyY5YKwx65ueBA4ivWqjt)

Expand on Servers > PostgreSQL 10 > Databases
Create a new database.
Expand on newdatabase > Schemas > public
Right-click on public and click on Restore, like so:

![alt text](https://drive.google.com/open?id=1HWKdRitCpN7SEFOxB-deL1O55FDkT_CB)

**Warning:** When restoring, leave role name empty, otherwise the restore job will fail with a "object of type 'bool' has no len()"

Once you have successfully loaded the .tar file, you should be rewarded with a green popup in the bottom right corner and all the tables should show up in your database:

![alt text](https://drive.google.com/open?id=1-b1OkzX_W1UYk_GtPrN8ml4JoTZ_TVWL)

### Prerequisites

Required libraries can be extracted from the requirements.txt file

```
pip freeze requirements.txt
```

## Built With

* [Python3.7](https://docs.python.org/3/) - Language
* [PostgreSQL](https://www.postgresql.org/docs/10/index.html) - Database

## Authors

* **Bryan Galindo** - *Initial work* - (https://github.com/bryangalindo)

See also the list of [contributors](https://github.com/bryangalindo/centrans_soc_tracker/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Good buddy Steven Dao who introduced me to the world of python and scraping
