:author: Charles Callaway
:date: 5-12-2019
:modified: 11-12-2019
:tags: designer
:lang: en-US
:translation: false
:status: draft


.. _alyvix_designer_options:

****************************
Testcase and Element Options
****************************

Parameters and settings for Alyvix Designer are separated into those that affect an entire
testcase, and those that affect a specific element type for a group or component.



.. _alyvix_designer_options_testcase:

================
Testcase Options
================

At the top of the Alyvix Designer panel (see Figure 1) are the options for the testcase as a whole.

.. figure:: images/ad_testcase_options_sized.png
   :alt: To fill in
   :figwidth: 80%
   :target: ../../alyvix_designer/images/ad_testcase_options_sized.png

   **Fig. 1:  ad_testcase_options_sized.png.**

The **Object name** is the reference name (not the file name) of the testcase object allowing the
testcase to be used in testcase scripts.

There are also three **testcase parameters** that affect how the
:ref:`screen capture elements <alyvix_designer_element_tree_types>` in its element tree
are detected, regardless of their type, and what happens if they fail to be detected.

* **Detection condition:**  One of the following conditions will be checked at a default
  interval of every ``0.5`` seconds

   * **Appear:**  Alyvix will continuously try to detect any of the main group elements (*image*
     or *rect*) on screen if it was not already there when the testcase started
   * **AppearDisappear:**  Alyvix will see whether any of the main group elements appears,
     and then disappears
   * **Disappear:**  If any of the main group elements was present when the testcase started,
     Alyvix will detect when one is no longer visible

* **Timeout:**  The chosen detection condition will be continuously checked until this number
  of seconds is reached
* **Break:**  If this option is ticked, then a timeout will cause the testcase to fail, and
  if it is part of a series of testcases, then the entire series will fail.  If not ticked,
  it will report failure but let the series of testcases continue.



.. _alyvix_designer_options_elements:

===============
Element Options
===============

General text.



.. _alyvix_designer_options_elements_root:

--------------
Parent is root
--------------

When parent is the root node

.. figure:: images/ad_root_options_sized.png
   :align: center
   :alt: To fill in
   :figwidth: 80%
   :target: ../../alyvix_designer/images/ad_root_options_sized.png

   **Fig. 2:  ad_root_options_sized.png.**

* **Call**

  * **Run**
  * **Kill**

* **Path** (SELECT)
* **Arguments**



.. _alyvix_designer_options_elements_image:

---------------
Parent is image
---------------

When the parent is *image*

.. figure:: images/ad_type_submenu_image_sized.png
   :align: center
   :alt: To fill in
   :figwidth: 80%
   :target: ../../alyvix_designer/images/ad_type_submenu_image_sized.png

   **Fig. 3:  ad_type_submenu_image_sized.png.**

**Recognition options**

* **MATCH**
* **COLOR**
* **SHAPE**



.. _alyvix_designer_options_elements_rect:

--------------
Parent is rect
--------------

When the parent is *rect*

.. figure:: images/ad_type_submenu_rect_sized.png
   :align: center
   :alt: To fill in
   :figwidth: 80%
   :target: ../../alyvix_designer/images/ad_type_submenu_rect_sized.png

   **Fig. 4:  ad_type_submenu_rect_sized.png.**

**Recognition options**

* **BUTTON**
* **BOX**
* **WINDOW**



.. _alyvix_designer_options_elements_text:

--------------
Parent is text
--------------

When the parent is *text*

**Recognition options**

**DETECT**

.. figure:: images/ad_type_submenu_text_detect_sized.png
   :align: center
   :alt: To fill in
   :figwidth: 80%
   :target: ../../alyvix_designer/images/ad_type_submenu_text_detect_sized.png

   **Fig. 5:  ad_type_submenu_text_detect_sized.png.**

* **Mode**

   * **Regex**  (Regex string)
   * **Number**  (More than 0)
   * **Date**  (last hour, last day, last week, last month)

* **Scrap**  (the text detected by OCR in the selected region)


**MAP**

.. figure:: images/ad_type_submenu_text_map_sized.png
   :align: center
   :alt: To fill in
   :figwidth: 80%
   :target: ../../alyvix_designer/images/ad_type_submenu_text_map_sized.png

   **Fig. 6:  ad_type_submenu_text_map_sized.png.**



.. _alyvix_designer_options_elements_all:

------------------
Parent is any type
------------------

For all object types

.. figure:: images/ad_action_string_sized.png
   :align: center
   :alt: To fill in
   :figwidth: 80%
   :target: ../../alyvix_designer/images/ad_action_string_sized.png

   **Fig. 7:  ad_action_string_sized.png.**

* **Action**

   * **None** (default)
   * **Move**
   * **Click**
   * **Scroll**
   * **Hold**
   * **Release**

* **String**




.. todo::

   * Timeout(s) implies more than one?  How?
   * The Timeout value can be set as a command line parameter, but not "Appear" and "Break"?
   * Need a clear explanation of `break`
   * Is the detection interval still set at 0.5 seconds as described in the 2.7.5 doc?  Is
     it still configurable?
