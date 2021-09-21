# CustomerService-Bot

This repository contains a chatbot made with RiveScript, Flask and MySQL

The frontend of the chatbot build assisted by [this]( https://github.com/hlaahmed/Skin_care-chatbot/blob/master/README.md) repository 

## Installation and usage

### 1. Install Rivescript


```bash
pip install rivescript
```

### 2. Install flask


```bash
pip install Flask
```
### 3. Install sql


```bash
pip install mysql
```
```bash
pip install mysql-connector
```

### 4. Start MySQL server

On your local machine, make sure to start MySQL server and have an IDE for managing the server, like XAMPP or MAMP .

### 5. creat database 
open phpmyadmin creat database 'customer service' and database tables 
user (user_id,	name,	email, password, complain, phone)
order(order_num,	deliver,	quality,	additinalcomplain)


## to run code

```bash
python main.py  
```


