:author: Charles Callaway
:date: 03-01-2020
:modified: 22-05-2020
:tags: getting, started, beginner, windows, settings
:lang: en-US
:translation: false
:status: final

.. include:: ../sphinx-roles.txt


.. _getting_started_example_settings:

******************************************************
Example:  Opening Windows Settings from the Start Menu
******************************************************

In the :ref:`previous example <getting_started_example_start>` we created an Alyvix
:iconlink:`gloss|test case|../glossary.html#glossary-test-case` consisting of a single test case
object.  Most of the time though, you'll need to chain together multiple test case objects to
synthesize more complex behavior in your apps.  So let's extend our previous example to run a
second action: opening the Windows Settings app.

.. rst-class:: bignums

#. Launch Alyvix Editor with the same file name from our previous example:

   .. code-block:: doscon
      :class: short-code-block

      C:\Alyvix\testcases> alyvix_editor -f start-test

   Editor will load the :file:`start-test.alyvix` test case created in the previous example.

#. We need to capture the screen once the Start menu has already opened, so change the delay
   number in :nobutton:`Delay [sec] 0` from ``0`` to something higher like ``5``, then click
   on :wbutton:`ADD`:

   .. image:: images/as_delay_five_seconds.png
      :class: image-with-border
      :alt: Setting up the 5 second delay before capturing the screen

#. Once you click :wbutton:`ADD`, you'll have 5 seconds to open the Windows Start Menu (you'll
   need to click on the Start button yourself in that time) before Alyvix captures the screen.

#. After the screen flashes white, press :kbd:`Escape` to return to screen capture mode, and then
   *right click* on the *Settings* icon at the left side of the Start Menu.  This will
   :iconlink:`gloss|autocontour|../glossary.html#glossary-autocontour` the icon.

   .. image:: images/ad_settings_selected.png
      :class: image-with-border
      :alt: Select Settings after the 5 second screen capture delay

#. Press :kbd:`Escape` again to return you to Editor with the new selection in the Designer
   panel at the right.  Assign a *left click* action as in the previous example by changing the
   value of the :guilabel:`Action` dropdown from ``None`` to ``Click``:

   .. image:: images/ad_settings_click.png
      :class: image-with-border
      :alt: Select Settings after the 5 second screen capture delay

#. In the Selector panel at the bottom left, change the name of our new test case object
   from :guilabel:`VisualObject1` to a new one like :guilabel:`PressSettingsIcon`:

   .. image:: images/as_rename_second_object.png
      :class: image-with-border
      :alt: The settings button test case in Alyvix Selector

#. Using its |4arrows-icon| icon seen above, drag the new test case object into the Scripting panel
   underneath the existing script element (similarly, clicking the |lineadd-icon| icon will add it
   to the end of the script):

   .. image:: images/ae_second_script_element.png
      :class: image-with-border
      :alt: The settings button script element in Alyvix Editor

#. Now call Alyvix Robot by pressing the |runblue| button at the top left.  You'll see the Start
   Menu open, and then a few seconds later a click on the Settings icon, at which point the Windows
   Settings app will open.

#. At the top of Editor, open the :nobutton:`Console` panel.  This contains the timing results
   for each script element.

   .. image:: images/ae_console_panel_result.png
      :class: image-with-border
      :alt: The results of running the script in Alyvix Editor

   |

   Finally, save and exit Alyvix Editor using the :nobutton:`SAVE` and :nobutton:`EXIT` buttons
   at the top.
