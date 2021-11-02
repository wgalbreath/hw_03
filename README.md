# HW_03 
In this file, I will answer the following:
<ol>
<li> What your <code>ebay-dl.py</code> file does

<li> How to run your <code>ebay-dl.py</code> file, using markdown code block(s) (and not inline code annotations) to show the exact commands that should be run to generate the 3 json files in your repo
    
<li> A link to the course project
</ol>

Overall, my `ebay-dl.py` file converts ebay's html files into json files. The file is scraping ebay for selected keywords that I specified (i.e. laptop, pants, spanish textbooks). The file called on a variety of old and new skills, including using doctests to find certain variables. At first, the program reads the html files and then my program ends by writing json files for each of the keywords. By using CSS selectors, the program searches for certain categories, such as price, status, and shipping details, and extracts that information by calling on the first ten pages of search results.

To generate the 3 json files, I had this code at the end of my `ebay-dl.py` file:
```

    filename = args.search_term+'.json'
    with open(filename, 'w', encoding='ascii') as f:
        f.write(json.dumps(items))

```


Then, I typed the following in my VS Code Terminal:
```

python3 ebay-dl.py "laptop"
python3 ebay-dl.py "pants"
python3 ebay-dl.py "spanish textbooks"

```



Here is a link to the [course project](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_03).
