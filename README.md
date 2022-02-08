####################################################################
# Openclassroom Scraping 
<h2>Openclassroom - Web scraping project</h2>

<h3>Informations:</h3>

First Python App Dev course project from Openclassroom based on web scraping.<br>
The app connects to https://books.toscrape.com/ and scrap the data related
to each books.<br>
The data is classified into the following variables:
<li>product_page_url</li>
<li>universal_ product_code (upc)</li>
<li>title</li>
<li>price_including_tax</li>
<li>price_excluding_tax</li>
<li>number_available</li>
<li>product_description</li>
<li>category</li>
<li>review_rating</li>
<li>image_url</li>
<br>
Finally the app will create one CSV file for each book category and also save every book pictures.
They'll be organized within separated folders as per following:
<li>CSV files :"/category_X/"</li>
<li>Pictures :"/category_X/Book_Picture/"</li>


<h3>Gettings started:</h3>
In order to launch the app, you'll need to:<br><br>
<li>Create a virtual environnement</li>
To install the package, open the Terminal and type the following:<br>
<code class="language-bash" data-lang="bash">pip install virtualenv</code><br>
Create the virtual environnement<br>
<code class="language-bash" data-lang="bash">virtualenv mypython</code><br>
Once done, you can close it typing:<br>
<code class="language-bash" data-lang="bash">deactivate</code><br><br>



<li>Install the Python libraries</li>
<code class="language-bash" data-lang="bash">pip install -r requirements.txt</code><br><br>
Versions :
python ==3.7.4
beautifulsoup4 ==4.10.0           
requests ==2.27.1        
python-csv == 0.0.13 
<h3>Author:</h3>
Arnaud ROUDIERE
<br><br>
####################################################################
