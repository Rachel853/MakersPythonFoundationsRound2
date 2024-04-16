# Chapter 1 Challenges

Well done for reaching the chapter 1 challenges! Here, you'll find two types of
exercise: drills and a programming challenge. Do the drills first and then move
onto the programming challenge. You must complete both before going
[back](../11_putting_chapter_1_into_practice.md) to reflect on your progress.

## Initial Setup

### Getting the Code

To get the exercises onto your machine, you'll need to fork and then clone this
repo.

<!-- OMITTED -->

### Installing Dependencies

Before starting either the drills or the programming challenge, you need to
install some dependencies — programs upon which these exercises depend.

One of these libraries (or dependencies we sometimes call them if they are a library that our code is *dependant* on to work) we will need is called `pytest`, a testing library for python. More on that to follow.

In Python, dependencies are managed using tools called package managers. Python has a few, but we are going to use the one that is the most popular, and comes prepackaged with your python installation - `pip`. 

We will also want to create a virtual environment (`venv`) - a kind of lockbox to store our libraries in. 

[Head over to this page for more guidance on virtual environments and packages](./package_management.md)

We're going to create a `venv` and use `pip`. Make sure you are at the top level of your directory.

*Whilst you can change `your_venv_name` to anything you like, it's generally a good practice to name it descriptively, like your project name and then "_venv", for example `foundations_venv`.

Here's how to do it:

```shell
python3 -m ensurepip --upgrade

# This will create a venv - change your_venv_name to anything
python3 -m venv your_venv_name

# This will activate the virtual environment
source your_venv_name/bin/activate
```
- After this you will see your `venv` name pop up in parenthesis in your terminal.
- Activating a `venv` simply means the `venv` is accessible in that terminal session - so we can install things into it, and use libraries inside it when running files.

``` shell
# This will install pytest
(your_venv_name)pip install pytest

# This will list out the libraries 
(your_venv_name)pip list

# Looks like this: 
Package   Version
--------- -------
pip       24.0
pytest    8.0.1
```
- You will see `pytest` has installed 

If you have trouble with this, contact your coach.

## Setting up the tests

[Pytest](https://docs.pytest.org/) is a tool used to run tests that ensure
your program does what it needs to do. In the near future you'll be writing your
own tests but, for now, you'll use the tests that we wrote for you.

Your goal is to make all the tests pass.

To run the tests, make sure you're in either the `drills` or `program` directory
and then run `pytest`. This will execute all the tests inside the `tests`
directory.

**Remember** if you have installed `pytest` into your `venv` i

Here's how to start:

```shell
cd path/to/python_foundations

# Make sure your venv is activated
source your_venv_name/bin/activate

# Navigate to the drills folder
(your_venv_name)cd chapter1/challenges/drills

# This will run all of the tests
(your_venv_name)pytest
# Very noisy right! Lots of stuff to read.

# BUT, there is a better way.
# This will run all of the tests until one fails, then show you the error
(your_venv_name)pytest -x
# You should probably run this one!
```

<details>
  <summary>:confused: I see an error about `ModuleNotFoundError: No module named 'lib.password_manager'`?</summary>

  ---

  You are most likely running `pytest` in the folder above or below where you ought to run it.

  ```shell
  # Check you are in the folder above the tests & lib folders
  ls -a
  .     .pytest_cache conftest.py   tests
  ..    __pycache__   lib
  

  ```
  
  ---
</details>

## Drills

Drills are short, tightly focused exercises which get harder as you progress.
Leave alone any files with `test` at the start of them.

Open `drills/lib/_1_calling_methods.py` in VS Code to begin! Remember to run
`pytest -x` often when you're in the `drills` folder! 

You will notice an `IMPORT ERROR` if you try and run `pytest -x` in
the wrong directory.

### Getting Started

1. Find the first set of drills
    * For chapter 1, that's `drills/lib/_1_calling_methods.py`
    * You'll find further instructions there
2. Work on the first challenge
3. Run `pytest -x` to check your answer
4. Keep going until all the tests for that set of drills are passing
5. Move on to the next set
6. Keep going until all the tests for all the sets are passing
7. :warning: [Zip up](../../pills/creating_zipfiles.md) your code so that you're
   ready to share it later
8. Move on to the programming challenge

## Programming Challenge

In this exercise you'll bring together several different concepts to build a
password validator.

:warning: Please do a [screen recording](../../pills/screen_recordings.md) of
yourself working on this exercise so that your coach can see how you're getting
on. You can upload it, along with your code, using the form at the end of this
file.

### Getting Started

1. [Start recording.](../../pills/screen_recordings.md) 🎥
2. Open up `program/lib/password_validator.py` and read the instructions.
3. Ensure your virtual environment is activated.
4. Navigate to the `program` directory in your terminal and run `pip install -r requirements.txt` 
to install dependencies.
5. Run `pytest -x` to show you the first failing test.
6. Work in small steps to complete the `is_valid()` method.
7. Run `pytest -x` regularly to check your progress.
8. Keep going until all the tests pass.

If you get stuck, consult the [Breaking Down
Problems](../../pills/breaking_down_problems.md) guide.

## Submitting Your Work

Use [this form](https://airtable.com/shrvo9ePjlwnaiLv5?prefill_Item=pyf_ch1) to
submit your code and screen recording

## What Next?

Go back [here](../11_putting_chapter_1_into_practice.md#reflect-and-review)
to reflect on your progress before moving on.


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2Fchallenges%2FREADME.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2Fchallenges%2FREADME.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2Fchallenges%2FREADME.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2Fchallenges%2FREADME.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fpython_foundations&prefill_File=chapter1%2Fchallenges%2FREADME.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
