# WagglyWalkers
Wagg.ly is a web app used for pairing dog walkers with dog owners and is a cloud based application. The setup for the protoype of this website can be found below. The prototype enables dog owners to register their dog and for dog walkers to register themselves within the web app, and this information will then be posted to a SQL database. To set up this prototype locally, please follow the steps below:

1. SET UP A SQL SERVER AND SQL DATABASE
   
Within the Azure portal, create a new SQL Server database by navigating to Create a resource > SQL Database. Complete the relevant information shown on screen, ensuring that 'Add Current Client IP Address' is set to yes.

Once the database is set up, open the Query Editor preview and sign in using the password you created in the previous step.

Create a new query and write a new script which creates a new table called dogs, and within this table you will need 4 columns: A primary key, name, email address, and dog's name. Next create another new query and write a script which creates a new table called walkers, and within this table you will need 4 columns: a primary key, name, email address and post code.

Within the database, navigate to 'Settings > Connection strings' and copy the connection string titled 'ADO.NET (SQL authentication)'. Replace {your_password} with the password you have created, removing the curly brackets {} and paste this string into a new temporary document for later use.

2. CREATE AZURE FUNCTIONS

Ensure that you have Visual Studio (VS) Code, Azure Extension for VS Code, Python, and Python Extension for VS Code installed on your machine before starting this section.

Open Visual Studio Code, open the Azure extension by navigating to the 'A' logo on the left hand pane and sign into your Azure account (using the same account that you used to create your database).

Navigate to 'Workspace > Create Function' and Create new project in a new folder.

In the Resources section of the Azure extension, navigate to 'Create a resource > Create Function App in Azure.

Right click on the new Function App and select 'Deploy to Function App'. Once complete right click on 'Application Settings' and select 'Add New Setting'. The setting should be named SqlConnectionString. Navigate to the temporary document you created earlier with the connection string and paste this into the SqlConnectionString.

Right click on 'register_dog' and 'register_walker' in turn, select 'Copy Function Url' and add both links to a temporary document for later use.

Open the Function App within the Azure Portal and navigate to 'API > CORS'. Add a single asterisk (*) to Allowed Origins and save. This is to prevent an error message when the web app tries to call the functions.

3. CREATE A STATIC WEB APP

Using the Index.html file and the images saved within this repository, create a GitHub repository that mirrors the structure of WagglyWalkers GitHub repository. The index file and the images must be saved within the main branch for it to work.

Within 'index.html', replace the API links for 'register_dog' and 'register_walker' with the function urls that you saved to a temporary document earlier. 

Within the Azure Portal, navigate to Create a resource > Static Web App to create a Static Web App using GitHub as the deployment source. Complete the set up information on screen and click create, it may take a few minutes for your app to become available. Once complete, click the blue 'visit your site' button on the static web app overview page to navigate to your new website.
