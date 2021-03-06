# Serverless Playground :building_construction:

____

![serverless](https://user-images.githubusercontent.com/11817331/116174930-c5221980-a6e5-11eb-9bb6-c3f38ded1f16.gif)

### What is Serverless ?

*The phrase “serverless” doesn’t mean servers are no longer involved. It simply means that developers no longer have to
think "that much" about them. Computing resources get used as services without having to manage around physical
capacities or limits.*

### Configuration

It is necessary to create user called *serverless-admin* in your AWS account

You need to create your profile at `/.aws/credentials` called `serverless-admin`

```
[serverless-admin]
aws_access_key_id = your access key
aws_secret_access_key = your secret key 
```


**How to create**

In your AWS Console access IAM > Users > Add Users


### Running locally

To run application locally execute the code below:

```
 make start-serverless-offline:
```

### Deploy

To deploy application, just run the code below:

```
 make deploy 
```

### Pros & Cons

**Pros**

- You do not need to manager servers, only serverless functions
- Run on-demand
- Scaling is automated (Limited by your available functions)
- Easy Pricing

**Cons**

- Be careful about timeout & memory
- Limited by time
- Cold start can be a problem
- Have a lot o lambdas working can be a pricing problem

## Application

This application provides a CRUD for books management 

### application Design

The application was designed using `package by feature`, basically we create package for which feature we have in the
application, in this case we have `books` as package and all division of classes inside it, if it was necessary we
create a new package of feature needed.

Example:

![Screen Shot 2021-05-20 at 21 52 29](https://user-images.githubusercontent.com/11817331/119066230-b9103b80-b9b5-11eb-9363-edcf76fbeaac.png)

## application Architecture Draw

:construction:

### Built With

- [Python](https://www.python.org/) - Programming language
- [Pycharm](https://www.jetbrains.com/pycharm/) - IDE
- [Poetry](https://python-poetry.org/) - Dependency Management
