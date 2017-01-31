# Encyclopedia

## Description

This project proudly presents a uniue collection of articles written by @ilebedev.
It is a [static site](https://sbkubric.github.io/19_site_generator/site/) that
represent a [Encyclopedia of Devman](https://devman.org/encyclopedia/).

The source files are written in Markdown and are separated by topics in different folders.
The structure of the static site is generated from JSON file `config.json`.
For simplicity of usage a pre-commit hook is provided to regenerate the sources of the site when
trying to commit updated content.

## Installation
```
git clone git@github.com:SBKubric/19_site_generator.git
```

To initiate git hooks, run `./init_hooks`.

### Configuration

To add new articles you should update the config.file structure and place them in appropriate folder
at `./articles`.

If you want to add extra hooks, just place them into
`./hooks/` directory and run the `./init_hooks`.

If you want to know more about git-hook technique you could use this [link](http://githooks.com/).

Also you can define extra scripts in the `makefile` and `./hooks/*`.



# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
