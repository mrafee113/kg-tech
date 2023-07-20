* resources
	* [beancount.io](https://beancount.io/)
	* [beancount.github.io](https://beancount.github.io/)
		* [getting started](https://beancount.github.io/docs/beancount_cheat_sheet.html)
		* [language syntax](https://beancount.github.io/docs/beancount_language_syntax.html)
		* [syntax cheatsheet](https://beancount.github.io/docs/beancount_cheat_sheet.html)
	* [furius.ca/beancount](https://furius.ca/beancount/)
	* [gdocs: Installing Beancount v2](https://docs.google.com/document/d/1FqyrTPwiHVLyncWTf3v5TcooCu9z5JRX8Nm41lVZi0U/edit)
	* [github/beancount](https://github.com/beancount/beancount/)

## Installation
> [google docs](https://docs.google.com/document/d/1FqyrTPwiHVLyncWTf3v5TcooCu9z5JRX8Nm41lVZi0U/edit)
* ubuntu
	```bash
	sudo apt install beancount
	```
* from sources (deprecated)
	```bash
	cd ~/.local
	git clone https://github.com/beancount/beancount
	sudo apt install python3-dev
	cd beancount
	
	# install dependencies
	deactivate
	sudo apt-get install python3-dateutil python3-bottle python3-ply python3-lxml python3-bs4
	sudo -H python3 -m pip install python-magic
	
	# make
	tsocks sudo python3 setup.py install
	
	# Apprently version 3 which is what resides on
	#  the master branch of the repo as of writing
	#  this at 21-June-2023, is **unstable**.
	```
* `vim-beancount`
```bash
mkdir -p ~/.vim/autoload ~/.vim/bundle
curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim
echo '" pathogen\n' >> ~/.vimrc
echo "execute pathogen#infect()" >> ~/.vimrc
echo '" vim-beancount\n'
echo "syntax enable\n" >> ~/.vimrc
echo "filetype plugin on" >> ~/.vimrc
```

## validating your file
The purpose of Beancount is to produce reports from your input file (either on the console or serve via its web interface). However, there is a tool that you can use to simply load its contents and make some validation checks on it, to ensure that your input does not contain errors. Beancount can be quite strict; this is a tool that you use while you’re entering your data to ensure that your input file is legal. The tool is called “bean-check” and you invoke it like this:

```
bean-check /path/to/your/file.beancount
```

Try it now on the file you just created from the previous section. It should exit with no output. If there are errors, they will be printed on the console.

## web interface
A convenient way to view reports is to bring up the “bean-web” tool on your input file. Try it:

```
bean-web /path/to/your/file.beancount
```

You can then point a web browser to [http://localhost:8080](http://localhost:8080/) and click your way around the various reports generated by Beancount. You can then modify the input file and reload the web page your browser is pointing to—bean-web will automatically reload the file contents.

