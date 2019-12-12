:author: Charles Callaway
:date: 5-12-2019
:modified: 12-12-2019
:tags: designer
:lang: en-US
:translation: false
:status: draft


.. _alyvix_designer_top:

###############
Alyvix Designer
###############

Alyvix Designer lets you select patterns on a copy of the screen, whether they're images,
rectangles, or text.  You can then define triggers for actions when those patterns are recognized
later in a simulated interaction with an application.

Designer will then save the set of patterns as a single :ref:`testcase <glossary_testcase>`, which
you can then use as building blocks to compose more complicated objects and scripts, and to
measure performance with :ref:`Alyvix Robot <alyvix_robot_top>`.

The following documentation presents information on Alyvix Designer:

* The :ref:`Interface Overview <alyvix_designer_element_tree>` page provides a high-level overview
  and describes the general layout of the interface.

* To learn more about interacting with specific visual elements and what they can do, see the
  :ref:`Element Tree <alyvix_designer_element_tree>` page.

* You can find more detailed information about the available options for testcases and components on
  the :ref:`Interface Options <alyvix_designer_options>` page.

* The :ref:`Testcase Object <alyvix_designer_testcase>` page provides technical details on how
  Alyvix Designer files are organized and what they contain.


.. todo::

   * Need an overview/map of Alyvix Designer and its doc in the Designer intro page
   * Should we talk about "Groups" vs. "Components", or is it better to talk about
     a "Main" component as the head of a group, but otherwise the same?
   * Should we call the capture lines "guide lines", "crosshair", something else?
   * Link to the simple how-to for Designer when ready




.. toctree::
   :maxdepth: 2
   :name: toc_designer
   :hidden:

   alyvix_designer/designer_interface_overview.rst
   alyvix_designer/designer_options.rst
   alyvix_designer/designer_element_tree.rst
   alyvix_designer/designer_testcase.rst
