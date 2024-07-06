# Data Narrative


<p align="center">
<a href="https://pypi.python.org/pypi/data_narrative">
    <img src="https://img.shields.io/pypi/v/data_narrative.svg"
        alt = "Release Status">
</a>

<a href="https://github.com/fccoelho/data_narrative/actions">
    <img src="https://github.com/fccoelho/data_narrative/actions/workflows/main.yml/badge.svg?branch=release" alt="CI Status">
</a>

<a href="https://fccoelho.github.io/data_narrative/">
    <img src="https://img.shields.io/website/https/fccoelho.github.io/data_narrative/index.html.svg?label=docs&down_message=unavailable&up_message=available" alt="Documentation Status">
</a>

</p>


This is a tool to generate natural language narrative for a database table. These narratives can have multiple applications, such as simply describing datasets, or generating reports. The narratives are generated using a template-based approach, where the user can define the structure of the narrative using a simple template based on the [Jinja2](https://jinja.palletsprojects.com) templating engine.


* Free software: MIT
* Documentation: <https://fccoelho.github.io/data_narrative/>


## Features

* Support for different types of narratives
  * Structural narrative: Just gives the name of table and enumerates the columns in the table, as well as the number of rows.

## Credits

This package was created with the [ppw](https://zillionare.github.io/python-project-wizard) tool. For more information, please visit the [project page](https://zillionare.github.io/python-project-wizard/).
