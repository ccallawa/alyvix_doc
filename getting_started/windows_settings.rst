:author: Charles Callaway
:date: 03-01-2020
:modified: 09-01-2020
:tags: getting, started, beginner, windows, settings
:lang: en-US
:translation: false
:status: draft

.. include:: ../sphinx-roles.txt


.. _getting_started_example_settings:

**********************************************
An Extended Example:  Opening Windows Settings
**********************************************

The real value of Alyvix lies in chaining together sequences of detections and actions.  So let's
extend the :ref:`previous example <getting_started_example_start>` so that in addition to
recognizing when the Start Menu is available and clicking on it, we'll also do something with
that menu.

The problem however is that we can't detect anything within the opened Start Menu, because it's
closed in the screenshot we used in the previous example.  We'll need to create a second test case
with a new screenshot.  But how can we detect the Start Menu when running Alyvix Designer will
cause the opened Start Menu to disappear?

The answer is to use the :ref:`delay parameter <test_case_building_designer>` when starting
Alyvix Designer.  This will insert a delay of however many seconds you request before the screen
is captured.



.. _getting_started_example_settings_build:

======================
Building the Test Case
======================

So let's build the second test case.  Add the ``-d`` delay parameter as follows, where the number
for *delay* is in seconds.  Remember to give the new test case a different object name (it should
have the same file name, however):

.. code-block:: doscon

   C:\Users\[username]\Desktop\Alyvix\Testcases\> alyvix_designer -f start-test -o settings -d 3

Once you see the line "Counting down" in the console, you'll have 3 seconds to open the Start
Menu and then wait for Alyvix Designer to capture the screen.  If that's not enough time for you,
just change it to 5, 10, or any other number you like.

.. sidebar:: Fig. 4:  Setting up the Settings button

   .. image:: images/ad_comptree_autodetect.png
      :alt: Setting up the Windows Settings button in Alyvix Designer
      :target: ../../getting_started/images/ad_comptree_autodetect.png
      :name: label_edit_settings_button

When you've done that, select the *Settings* icon on the left side of the Start Menu.  Try using
the right mouse button to autodetect the icon if you didn't in the
:ref:`previous tutorial <getting_started_example_start>`).  It creates minimized rectangles, which
can speed up test execution, especially when it has to look for lots of rectangles.  Your new test
case should look like Figure 4.

As in our previous example, we can now assign a left-click action by selecting our new *Settings*
region in the component tree, and then changing the action from ``None`` to ``Click``.  We can
then save everything with the :guilabel:`OK` button.

Where's the trick, though?  Now we just have two, independent test cases (even though they are in
the same file).  If you run the ``alyvix_robot`` script as before with the object name ``settings``,
it doesn't detect anything because the Start Menu is not open.  How do we chain them together using
the Command Prompt to open the Start Menu, and then open the Settings app?
:hint:`(Hint:  see the next section).`



.. _getting_started_example_settings_exec:

=======================
Executing the Test Case
=======================

The answer lies in how we call the execution script.  Since we have both test cases in the same
file, we can join the object names together as follows:

.. code-block:: doscon

   C:\Users\[username]\Desktop\Alyvix\Testcases\> alyvix_robot -f start-test -o "start settings"

This will chain the end of one test case to the beginning of the next.

When you run the command, you'll see the Start Menu open, and then a few seconds later a click
on the Settings icon, at which point the Windows Settings app will open.  Meanwhile, in the
console, Alyvix Robot reports the combined time (3 of the 3.219 seconds comes from the delay we
specified above):

.. code-block:: md

   2020/01/03 12:06:51.166: start-test starts
   2020/01/03 12:06:52.710: start DETECTED in 0.0s (+/-0.049)
   2020/01/03 12:06:54.381: settings DETECTED in 0.0s (+/-0.061)
   2020/01/03 12:06:54.385: start-test ends OK, it takes 3.219s.
