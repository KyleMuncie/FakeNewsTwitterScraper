# CSE472Project2
<b>make sure you run this in terminal while in the file directory:</b>
<ul>
  <li>pip install -r requirements.txt</li>
  <li>run main.py</li>
</ul>

## Summary of Code
<p> This code takes in a test.csv and then iterates through it to give each claim a category based off it's data from train.csv. <br>
For claims from a country/source/url that has a history of only outputting one category of claims, the score is automatically assigned <br>
Otherwise, we open the fact-checked url with selenium and get the html of the site. Then the html is formatted to regualr text and translated to english. <br>
From there we search the translated text looking for keywords to assign a category. If none are found we automatically assign the claim a 0.<br>
</p>

### Things to Know
<ul>
  <li> Selenium will need a chrome driver to run. </li>
  <li> The program takes about 45 to 50 minutes for the whole test.csv. </li>
  <li> Make sure main.py and test.csv are in the same folder if you're running it. </li>
  <li> The submission.csv the program outputs will have amn extra column that is the panda database index. It can be ignored </li>
</ul>

### Shortening the Code Run Time.
<p> <br> If you want to see how the code functions without waiting the full time, put the following code in at line 230. <br>
if( Id > X)
  break
<br> Where x is the amount of claims you want to see evaluated.
</p>
