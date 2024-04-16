# Managing Python Projects with `pip` and `venv`

In this guide, we'll dive into how to efficiently manage your Python projects using `pip` for package management and `venv` for creating isolated environments. Think of `venv` as a safe or lockbox, keeping your project's dependencies (libraries) separate from those of other projects, ensuring compatibility and ease of management.

## Learning Objectives

By the end of this guide, you will be able to:
- Understand the importance of using virtual environments
- Create and manage virtual environments using `venv`
- Install, upgrade, and remove packages using `pip`
- Understand why and how to install external packages and libraries

___

## Virtual Environments with `venv`

### Why Use Virtual Environments?

Imagine you're a chef working on multiple dishes, each requiring different ingredients and cooking methods. Without organising your ingredients and utensils for each dish, you'd quickly run into chaos in the kitchen. Similarly, `venv` helps organise and segregate Python project dependencies, ensuring that each project has access to the right versions of libraries it needs, without interference from others.

We can infer, then, that a *non-virtual* environment, is simply the environment of the machine you are using - the global environment you can think of it as.

### What is a Dependency?

You may have seen the term dependency quite a few times so far, but what is it? Very simply, a dependency is a library that our program or code is *dependant* on in order to work.

So if your program *needs* the `pytest` library, or the `pandas` library in order to work, then those libraries are dependencies for your project. As you saw in the video, some libraries come with other libraries packaged with them (like `numpy` comes with `pandas`) because they need those dependant libraries in order to work. This is part and parcel of the modular nature of python, and is very common.

### Venv to the Rescue!

Imagine our chef is cooking multiple meals, for multiple tables at their restaurant. Some people might have allergies, some have asked for extras. Developers are similar, working on multiple projects and products.

Using `venv` is like our chef using separate tools and ingredients for each dish they prepare. This method prevents mixing up flavours or causing issues, similar to how `venv` keeps Python projects from interfering with each other. Here's why it's better than installing libraries globally:

- **Prevents Conflicts**: Like needing different versions of the same ingredient for various dishes, projects often require different versions of libraries. `venv` lets each project have its own set of libraries, avoiding clashes.
- **Keeps Projects Organised**: Just as a chef organises their kitchen, `venv` helps keep project dependencies tidy and separate, making projects easier to manage and share.
- **Ensures Consistency**: A chef aims for their dishes to taste the same every time. Similarly, `venv` ensures your project environment is the same everywhere it runs, making testing and deployment smoother.

In short, `venv` helps avoid mix-ups, keeps things tidy, and ensures projects work consistently, just as a well organised kitchen allows a chef to cook smoothly and efficiently.

### Creating Your First Virtual Environment

To create a virtual environment, select a directory where you want to place it, and run the `venv` module as follows:

```shell
python3 -m venv your_venv_name
```

This command creates a directory named `your_venv_name` which contains a complete Python environment. Think of it as crafting a lockbox where you'll store everything your project needs.

### Activating the Virtual Environment

Before using the virtual environment, you need to activate it:

- On Windows:
  ```cmd
  your_venv_name\Scripts\activate.bat
  ```
- On Unix or MacOS:
  ```shell
  source your_venv_name/bin/activate
  ```

Upon activation, you'll notice the environment's name appears in your shell prompt, indicating that any Python or pip commands will now operate within this isolated environment.

### Deactivating the Virtual Environment

To exit your virtual environment, or to "unlock" your lockbox, simply run:

```shell
deactivate
```

___


## Managing Packages with `pip`

`pip` is the tool for installing Python packages from the Python Package Index (PyPI). It's like an app store for Python, allowing you to install, upgrade, and remove libraries and tools.

### Installing Packages

To add a new tool to your lockbox, you can install a package using `pip`:

```shell
pip install pytest
```

This command fetches the `pytest` library from PyPI and installs it into your virtual environment (as long as your `venv` is activated!).

### Why Install Libraries and Packages?

Python comes with a rich standard library, which provides a wide range of functionality. However, there are times when you need capabilities that are not available in the standard library. This is where external libraries and packages come into play.

Think of Python's standard library as the basic ingredients in a chef's kitchen. While these ingredients allow you to cook a variety of dishes, sometimes you want to create something that requires exotic spices or specific tools not found in your kitchen. External packages and libraries are like these spices and tools, enabling you to enhance your projects with more specialised features and functionalities.

For instance, if you're working on a web scraping project, you might need `BeautifulSoup` or `Scrapy` to parse HTML and extract information. These powerful tools are not part of Python's standard offerings, so you'll need to install them using `pip`.

So, why would we use them in the first place? Imagine the chef, back in their kitchen, they need to blend some delicious ingredients. Should they build their own blender from scratch? Or should they borrow the really good one that everyone says is great, and is supported and upgraded often by lots of other great chefs?

### Where are these Libraries?

`PyPI`, or the Python Package Index, is like the phonebook for Python libraries and packages. It's a central repository where developers from around the world publish their Python projects, making them available for others to use. Just as you might search a phonebook to find a person's number, pip uses PyPI to find and download the libraries you want to add to your project. When you run a command like pip install pytest, pip looks up "pytest" in this vast "phonebook," finds the latest version, and then downloads it into your project's virtual environment. This seamless integration between pip and PyPI makes it incredibly easy to extend the capabilities of your Python projects by leveraging the work of thousands of developers worldwide.

### Upgrading Packages

If you find out a tool or library (like the `pytest` library in this example) you're using has a new version, you can upgrade it with:

```shell
pip install --upgrade pytest
```

This would of course work with any library you would like to upgrade.

### Listing Installed Packages

To see what's currently in your lockbox, use:

```shell
pip list
```

This command lists all packages installed in your virtual environment.

### Removing Packages

If you decide you no longer need a particular tool or library in your project, you can remove it:

```shell
pip uninstall pytest
```

___

## Practical Exercises

Now that you've learned how to manage your Python projects with `pip` and `venv`, try the following exercises to reinforce your understanding:

1. **Create a new virtual environment** for a project you're working on.
   - Navigate to your project's directory in the terminal and run:
     ```shell
     python3 -m venv myfunprojectenv
     ```
   - This creates a new virtual environment named `myfunprojectenv`.

2. **Activate your virtual environment** to start using it.
   - We use the source command to run the `activate` script in the venv.
     ```shell
     source myfunprojectenv/bin/activate
     ```
   - You'll see the name of your virtual environment (`myfunprojectenv`) in the prompt, indicating it's active.

3. **Install the fun library `pyjokes`** as an example external library for this project.
   - Install `pyjokes` by running:
     ```shell
     pip install pyjokes
     ```

4. **Verify the installation** by listing all installed packages.
   - Check which packages are installed in your virtual environment with:
     ```shell
     pip list
     ```
   - Ensure `pyjokes` is listed among the installed packages.

5. **Try using `pyjokes`** to see it in action.
   - Run a Python interactive repl session or create a small script:
     ```python
     import pyjokes

     joke = pyjokes.get_joke()
     print(joke)
     ```
   - Run your `example_pyjokes.py` file
     ```bash
     python3 example_pyjokes.py
     ```
   - Enjoy the output—a random programming joke!

6. **Experiment with installing an older version** of a package, then upgrading it.
   - First, find a package to downgrade (or install an older version), for example:
     ```shell
     pip install "pyjokes<0.6.0"
     ```
   - Then, upgrade to the latest version:
     ```shell
     pip install --upgrade pyjokes
     ```

7. **Introduce intentional errors** to learn about error messages.
   - Try installing a non-existent package:
     ```shell
     pip install nonexistpackagename
     ```
   - Observe and read the error message. Understanding these messages can be very helpful in troubleshooting.

8. **Deactivate your virtual environment** when you're finished with your session.
   - To exit your virtual environment, simply run:
     ```shell
     deactivate
     ```
   - Notice that the virtual environment's name disappears from the prompt, indicating it's no longer active.
9. **Try running the `pyjokes` script** again to see that it is no longer available.
   - After we have deactivated our venv, the `pyjokes` script will no longer run and we will get an error:
     ```bash
     python3 example_pyjokes.py
     ```
   - Notice that now we get an import error!


## Conclusion and Next Steps

Using `venv` and `pip` allows you to manage your Python projects efficiently, ensuring that each project has its own set of dependencies, undisturbed by the requirements of other projects. Like chefs organising their kitchen for each dish they're preparing, you can keep your Python projects clean, organised, and functional.

Now that you've got a handle on using `venv` and `pip`, [head back to the README to continue your journey with drills.](./README.md#installing-dependencies) 

You can return here any time in order to refresh your memory.


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2Fchallenges%2Fpackage_management.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2Fchallenges%2Fpackage_management.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2Fchallenges%2Fpackage_management.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2Fchallenges%2Fpackage_management.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2Fchallenges%2Fpackage_management.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
