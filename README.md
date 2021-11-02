# HW_03 
In this file, I will answer the following:
<ol>
<li> What your ebay-dl.py file does

<li> How to run your ebay-dl.py file, using markdown code block(s) (and not inline code annotations) to show the exact commands that should be run to generate the 3 json files in your repo

<li> A link to the course project
</ol>


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
