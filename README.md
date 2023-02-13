<h1 align="left">Restaurant Orders</h1>

###

<p align="left">System that generates reports with information about orders and customers who attend a restaurant. This data will help the work of a marketing agency in order to leverage sales and the number of customers.<br>In addition, it is also possible to control the stock of ingredients to ensure that the restaurant's digital menu always offers products that are available in stock.</p>

###

<h2 align="left">Technologies used</h2>

###

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="50" width="62" alt="python logo"  />
</div>

###

<h2 align="left">How to use the application</h2>

###

Clone the application using the git clone command. After that, enter the project folder using the command `cd restaurant-orders`.

###

<h2 align="left">How to run the application</h2>

###

1. Create the virtual environment for the project
 - `python3 -m venv .venv && source .venv/bin/activate`
 
2. Install the dependencies
- `python3 -m pip install -r dev-requirements.txt`

###

> <h2 align="left">Publicity campaign</h2>

#### The system generates a txt file in `data/mkt_campaign.txt` with the following information:

- What is the most requested dish by 'maria'?
- How many times did 'arnaldo' ask for 'hamburger'?
- Which dishes did 'joao' never order?
- What days did 'joao' never go to the snack bar?

To run it, use the command `python3 -m src.analyze_log`.

###

> <h2 align="left">Continuous analyzes</h2>

#### System that allows, at any time, the extraction of information:

- Favorite dish per customer
- Dishes never ordered by each customer
- Days never visited by each customer
- Busiest day
- Less busy day

To run it, use the command `python3 -m src.track_orders`.

###

> <h2 align="left">Inventory control</h2>

#### Controls the restaurant's inventory, showing quantities of products to be purchased and availability of dishes.

To run it, use the command `python3 -m src.inventory_control`.
