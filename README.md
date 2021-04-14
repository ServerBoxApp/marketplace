# Marketplace
The marketplace to store the templates.

# Usage
```shell
vim new_template.yml # Create a new template
python3 generate.py # Grab all the YAML files and generate a data.json.
```

# Template
A template is a YAML file that describes the necessary information to create a application in ServerBox.
A tipycal template consists of the following parts:
- info: Describes the genral information about the template.
- env: The available environmental variables to configure an application.
- data: The data storage configuration for a stateful application.
- network: The port mapping configuration for an application.

More details can be found in this repository.


# Contribute new templates
1. Create the template following the template format defined above.
2. Test the template by running `verify.py`.
3. Create a pull request and wait for approval.