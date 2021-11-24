# python_packaging_examples
Example projects on how to create python packages of different complexity

The different configurations are implemented in different branches of this repository.
* **setuptool_helloworld**: Very basic python library that offers a `ppe.main.hello()` function


## Examples
## setuptool_helloworld
This is the minimal skeleton for any kind of single python library. It contains
a single module `ppe` that the user can import and use.

## setuptool_simple_clitool
Extens **setuptool_helloworld** to expose a cli tool named `ppe-hello` that executes
ppe.main.main().