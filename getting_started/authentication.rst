:author: Charles Callaway
:date: 30-05-2023
:modified: 25-08-2023
:tags: getting, started, beginner, authentication
:lang: en-US
:translation: false
:status: final

.. include:: ../sphinx-roles.txt


.. _getting_started_authentication:

*****************************************
Example:  Authentication with Credentials
*****************************************

Often when monitoring applications and services via SaaS, whether in-house or in the cloud, you'll need
to log in to prove you're allowed to use that particular service.  And of course, logging in means that you'll
need private credentials like a user name and password.

When building a test case in Alyvix, where are you going to store those credentials, and how are you going
to retrieve them when you need them?

Remember that Alyvix stores its test cases in an open file format.  We even
:ref:`publish the full specification <test_case_data_format_top>`
right here on this very website.  But if anyone who gets their grubby little hands on your test case files is
able to just look at anything in it, that means they can also copy those credentials.  Not good.

Let's start at the beginning though so we don't miss anything.  Let's create a simple test case that logs
in to **www.dropbox.com** with our credentials and then logs out again, using the best practices described
:ref:`in this previous tutorial <getting_started_web_browser>`.


.. _getting_started_authentication_cipher:

========================
Alyix Cypher Preparation
========================

Before starting the test case build, let's encrypt our credentials so they're ready to use.
We'll make up a private key (remember to keep it securely locked away, even not on your computer),
and use it as one of the arguments to the :ref:`alyvix_cypher command <alyvix_robot_cipher_encryption>`:

.. code-block::

   C:\Alyvix\testcases> alyvix_cipher -e <text_string_to_encrypt> -k <private_key>

Suppose we make up a private key ``i_like_alyvix``, and your two credentials are ``my_user_name`` and
``my_password``.  Then we would run the cipher command twice as follows, producing two
ciphers that we'll copy later into the credential fields:

.. code-block::

   C:\Alyvix\testcases> alyvix_cipher -e my_user_name -k i_like_alyvix
   +HGl7XV2mdTFvWLpr9CtVQ==
   C:\Alyvix\testcases> alyvix_cipher -e my_password -k i_like_alyvix
   bS1boKctW64yZ1dG1iz2ZA==

The cipher command is deterministic, so if you give it the same credential and same private key, it will
produce the same cipher.  When it's time to build the relevant test case step, just use the cipher returned
as if it were the real credential, and Alyvix will decrypt it automatically, inserting the original value.

Note that the ``==`` at the end of the cipher is what tells Alyvix that it **is** a cipher.


.. _getting_started_authentication_build_start:

===================
Initial Build Steps
===================

Now that our ciphers are ready, let's start our build:

.. rst-class:: bignums

#. Repeat steps #1-4 :ref:`in the previous tutorial <getting_started_web_browser>` to launch the
   web browser, but using ``www.dropbox.com`` instead of ``www.visittrentino.it`` as the web app address.
   Once the page loads you should see this at the top:

   .. image:: images/gs_authentication_login.png
      :class: image-boxshadow
      :alt: The top of the initial web page for www.dropbox.com

#. Add a new step that clicks on the login button once the web page has loaded.  Highlight an anchor and
   the Login button, then add a Click action to the Login button:

   .. image:: images/gs_authentication_login_editor.png
      :class: image-boxshadow
      :alt: Highlighting the anchor and Login button in the web page

   .. image:: images/gs_authentication_login_click.png
      :class: image-boxshadow
      :alt: The click action added to the Login button

#. We now have the login page ready where we can enter our user name:

   .. image:: images/gs_authentication_field1.png
      :class: image-boxshadow
      :alt: The account field highlighted in a test case step

   where we show Alyvix how to click on the account field, type in the cipher, and click on the Continue button:

   .. image:: images/gs_authentication_login_username.png
      :class: image-boxshadow
      :alt: The click actions and user name insertion added in Alyvix Designer

#. After that a second page appears where we can enter the password, and we do the same thing with
   the password field:

   .. image:: images/gs_authentication_field2.png
      :class: image-boxshadow
      :alt: The password field highlighted in a test case step

   .. image:: images/gs_authentication_login_password.png
      :class: image-boxshadow
      :alt: The click actions and password insertion added in Alyvix Designer

#. You can now measure whatever task you would like within the web app (here, DropBox) and measure
   the results.  When you're done you'll need to log out so that the next time you run the test
   case, it will show the login page rather than launch the main app without asking for a login.

   At this point, the standard logout procedure is to click to open the Account menu, and then a
   second click to actually logout.  That's two whole steps.  But we can actually do it in one
   step if we note that all that button does is make a call to ``https://www.dropbox.com/logout``:

   .. image:: images/gs_authentication_logout.png
      :class: image-boxshadow
      :alt: The shortcut for logging out in multi-level windowing

   So instead just add a step to insert that URL into your browser's URL bar (locate it, click, and
   have Alyvix type in ``https://www.dropbox.com/logout{enter}`` where the ``{enter}`` string tells
   Alyvix to actually press the Enter key.

   That logs you out, so finally you can kill the browser as described in Step #6
   :ref:`in the previous tutorial <getting_started_web_browser>` and everything will be left in
   the same state that we started with, allowing you to repeatedly run the test case for a
   monitoring scenario.

That's it! You can follow the procedure above to create and insert ciphers no matter how many
encrypted strings you need, and you won't have to worry that someone will steal your stored
credentials just because they're kept in clear text in an open file structure.
