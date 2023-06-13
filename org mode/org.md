#+TITLE: Org
#+DESCRIPTION: Useful key bindings and hacks to use org-mode.
#+COLUMNS: %25ITEM %TODO %3PRIORITY %2PRIORITY(something){max;some}
#+CATEGORY: cheatsheet
#+FILETAGS: :cheatsheet:org:doc_summary:

* read org-mode manual with M-x org-info
* Attention
Weirdly, org-mode cannot work without headlines. Meaning that
if you create a headline and try to come out of that headline without a new
headline, org-mode will not allow you to do that; unless of course you create
another headline. Although by toggling org-indent-mode you are able to do that
but org-mode features (e.g. folding) will not work correctly at all. So just
keep in mind to always use headlines with org-indent-mode turned on.

* org activation (from manual)
activate org from anywhere in emacs
** org-agenda: C-c a OR SPC-o-a-a
** org-store-link: C-c l OR SPC-n-l
** org-capture: C-c c OR SPC-n-n
** org-attach: C-c C-a

* structure
** org files
org files are succeeded with a .org file.
alternatively you can make a file use org mode by insert the below line at the
beginning.
org-insert-mode-line-in-empty-file: "MY PROJECTSS    -*- mode: org; -*-"

** headings :: aka headlines aka entries
*** org-toggle-heading: SPC-m-h
*** examples
**** This is level 3
***** This is level 4
****** This is level 5
******* This is level 6
text goes here

** items
*** org-toggle-item: SPC-m-i
*** examples
+ unordered list item one
+ unordered list item two
  - you can use dash instead of +
    1. ordered list item
    2. 2nd ordered list item

** drawers :: this is a headline
still outside the drawer
:some-drawer-name:
and this is inside the drawer
:end:
*** you can also insert drawers with: C-c C-x
*** completion over drawer's keywords: M-TAB

** blocks
They are used for various purposes including source code examples.
*** basic syntax
#+BEGIN_EXAMPLE
this is *the* example block
#+END_EXAMPLE
*** line numbers
Line numbers only affect org export. For further information read the
manual.
#+BEGIN_SRC -n
this is exported as a numbered line.
#+END_SRC
*** source code
#+BEGIN_SRC python
# this code will be rendered as a python code.
print("Hello from python.")
#+END_SRC

** properties
These are key-value pairs that need to be associated with an entry or a tree.
The association should be done using drawers. Basically put, properties are
a drawer with a special name. And that is "PROPERTIES".
Also note that the properties drawer should be located right below the
headline.
*** this entry has properties set.
:PROPERTIES:
:Title: The Properties Exntry
:Author: Mehdi Rafee
:END:

** column view :: FUCKING AMAZING
*** TODO entry status :: access org doc
**** TODO column syntax
**** TODO column view inheritance
**** TODO column view features
*** Example column view :: turn on using C-c C-x C-c and off using 'q'
   :PROPERTIES:
   :COLUMNS:  %20ITEM %9Approved(Approved?){X} %Owner %11Status %10Time_Spent{:}
   :Owner_ALL:    Tammy Mark Karl Lisa Don
   :Status_ALL:   "In progress" "Not started yet" "Finished" ""
   :Approved_ALL: "[ ]" "[X]"
   :END:

**** Item 1
    :PROPERTIES:
    :Owner:    Tammy
    :Time_spent:   1:45
    :Status:   Finished
    :END:

**** Item 2
    :PROPERTIES:
    :Owner:    Tammy
    :Status:   In progress
    :Time_spent:   0:15
    :END:

**** Item 3
    :PROPERTIES:
    :Owner:    Lisa
    :Status:   Not started yet
    :Approved: [X]
    :END:

** folding trees and sub-trees
Much like other powerful text editors or IDEs, you can fold/unfold sub-trees
in org-mode.
*** rotate current sub-tree between states: TAB
*** rotate the entire buffer between states: S-TAB
*** fold (close) the sub-tree: zc
*** unfold (open) the sub-tree: zo
*** fold everything: zM
*** unfold everything: zR

** motion (normal mode)
*** move left/down/up/right: h/j/k/l
*** move to next/prev heading: gj/gk
*** move to parent/child element: gh/gl

** tree structure editing
*** indent/un-indent heading: M-h/M-l
*** indent/un-indent sub-tree: M-S-h/M-S-l
*** move sub-tree/item up/down: M-j/M-k
*** move item up/down but not sub-tree: M-S-j/M-S-k

** advanced vim structure editing
*** select an element: vae
*** delete an element: dae
*** select a sub-tree: vaR
*** delete sub-tree: daR
*** yank sub-tree (without heading): yiR

* tables
** creating a table: surround column names with pipes(|)
** add row to table: C-RET
** move to next/prev cell: TAB/S-TAB
** insert row separator: SPC-m-b--
** duplicate value in the cell below: S-RET
** example
 | column1   | column2 | etc   |
 | v1        | v2      | v3    |
 |           | v3      | v4    |
 |-----------+---------+-------|
 |           |         |       |
 | above row | is      | empty |
 |-----------+---------+-------|
 |           |         |       |
** table motions
*** move row up/down: M-k/M-j
*** move row left/right: M-h/M-l
*** insert column: M-S-l
*** delete column: M-S-h
*** insert row: M-S-j
*** delete row: M-S-k

* links
** general link format
#+BEGIN_SRC
[[link][description]]
#+END_SRC
** internal links
If the link does not look like a url, it is considered a link to the current
file.
This syntax leads to a text search in file: [[tables][table entry search]].
If a property "CUSTOM_ID" has a unique value links can be written as
[#CUSTOM_ID][description].
** external links
id, [[mailto:mrafee113@gmail.com]], [[help:org-store-link]],
[[info:org#External links]], [[shell:ls *.org]],
*** file links
[[file:~/.doom.d/init.el]]
[[../../.doom.d/init.el]] # If path starts with '/' or './', "file:" can be
omitted.
[[file:local-file.org]] # If path does not start with "/" or "./", link will
refer to file in the file's directory.
** handling links
*** org-store-link
shortcut: M-x org-store-link OR SPC-n-l
function: It stores a link to the current location.
The stored link is in a history list specially defined for org.
*** org-insert-link
shortcut: C-c C-l
function: Prompts to insert a new link. The links stored from
org-store-link are presented too.
**** insert file links
shortcut: [C-u] C-u C-c C-l
By default the function prefers relative path; To force an absolute
path use two C-u prefixes.
*** edit existing links: C-c C-l
*** record positions
org-mark-ring-push: C-c %
org-mark-ring-goto: C-c &

* task state management :: TODOs
** configure states using the org-todo-keywords variable.
** toggle state buffer: SPC-m-t
** iterate states backwards/forwards: S-LEFT/S-RIGHT
** PENDING view todo items in a sparse tree: M-x org-show-todo-tree
** "todo" dependencies
This functionality, when activated, acts as a validator when the state is
being marked as done.
A parent cannot be marked as done when any of its children are in a non-done
state.
If an entry has a property "ORDERED", each of its todo children is blocked
until all earlier siblings are marked as done.
You can prevent an entry from being blocked by using the "NOBLOCKING"
property.
** checkbox-es
*** create checkbox: - [ ]
*** iterate checkbox state: C-c C-c OR RET
*** example [1/3] [33%] (hint: this (/ and %) will keep track of item-done count)
- [ ] checkbox 1
- [-] checkbox 2
- [X] checkbox 3

* tags
Each entry in a file can contain tags. :this_is_a_tag: :these:are:multiple:tags:
Each file can have a default tag for all children using the #+FILETAGS property.
Every tree in org files, uses tag inheritance by default.
Pressing C-c C-c on a headline presents you with tags.
** inheritance :: sample parent heading :parent_tag:
*** sample child heading :child_tag:
This heading will contain, the parent_tag along with the child_tag.
** grouping tags
#+TAGS: { @work(w) @home(h) @tennisclub(t) } laptop(l) pc(p)
This indicates that at most one of @work, @home and @tennisclub should be selected.
** tag hierarchies
refer to org documentation for this. very useful but tldw.

* Properties and Columns :: read org-doc tldw
* Dates and Times
** different timestamps
*** plain timestamps
The simple one.
**** example description or sth
<2006-11-01 Wed 19:15>
**** example with time range
<2006-11-01 Wed 19:15-20:00>
*** timestamp with repeating interval
Although timestamps can be used when reading a tree, they are also used for org-agenda. (I think all of them...)
Entry timestamps can be scheduled to repeat with a repeater_interval.
**** example timestamp with repeater
<2007-05-16 Wed 12:30 +1w>
This repeats every wednesday.
You can also use "d=days", "m=months" or "y=years" instead of "w=weeks".
*** Time/Date range
Two timestamps connected by '--' denote a range.
**** example range
<2004-08-23 Mon>--<2004-08-26 Thu>
*** inactive timestamps
In contrast to other timestamps that are shown in org-agenda, these timestamps don't.
**** example inactive timestamp
[2006-11-01 Wed 10:20-11:32]--[2007-12-01 10:20]

** creation/modification
*** insert timestamp with prompt: C-c .
*** insert inactive timestamp: C-c !
*** normalize timestamp: C-c C-c
*** input timestamp from calendar: C-c <
*** goto calendar from timestamp: C-c >
*** access agenda on date: C-c C-o
*** timestamp day down/up: S-LEFT/S-RIGHT
*** evaluate time range(diff): C-c C-y

** deadlines/scheduling
*** deadline :: C-c C-d
This is better if a task is a todo item, but it's not necessary.
On the given day the task is listed in the agenda.
**** TODO example
DEADLINE: <2004-02-29 Sun>
**** TODO specific example about warning days
DEADLINE: <2004-02-29 Sun -5d>
*** scheduled :: C-c C-s
This is for when you're planning to work on a task on the given date.
SCHEDULED: <2004-12-25 Sat>
*** org-check-deadlines :: C-c / d

** Clocking Work Time (record time)
Refer to org docs. tldw
*** example
:LOGBOOK:
CLOCK: [2021-09-18 Sat 20:48]--[2021-09-18 Sat 20:49] =>  0:01
CLOCK: [2021-09-18 Sat 20:46]--[2021-09-18 Sat 20:47] =>  0:01
:END:
i'm trying this out.

* Refiling and Archiving
** refile
*** org-refile :: C-c C-w
This will cut and paste the selected entry under another entry within the file.
*** org-copy :: C-c M-w
This functions like org-refile except it copy and pastes.
*** org-archive-subtree-default :: C-c C-x C-a
This moves the selected subtree to another file named [this_file].org_archive.
*** org-toggle-archive-tag :: C-c C-x a
Entries can be marked archived for invisibility in agenda view without being moved.

* org agenda
** views :: org-agenda
Each view is shown through a read-only buffer with special commands available.
*** agenda :: a
Looks like a calendar that provides information for specific dates.
*** todo list :: t OR T
Covers all unfinished action items.
*** Match View :: m OR M
Shows headlines based on the tags, properties, and todo state associated with them.
*** Text Search View :: s OR /
Shows all entries from multiple files that contain specific keywords.
*** Custom Views
These are special searches and combinations of different views.
** filtering agenda views
*** org-agenda-filter-by-tag :: \
*** org-agenda-filter-by-category :: <
*** org-agenda-filter-by-regexp :: =
*** org-agenda-filter-by-effort :: _
*** org-agenda-filter :: /
*** org-agenda-filter-remove-all :: |
** agenda commands
*** buffer
**** Motion
***** org-agenda-next-line :: n OR DOWN OR C-n
***** org-agenda-previous-line :: p OR UP OR C-p
**** View/Go to org file
***** org-agenda-show-and-scroll-up :: SPC OR mouse-3
Display the original location of the item in another window.
***** org-agenda-recenter :: L
Display original location of the item in another window.
***** recommended: org-agenda-goto :: TAB OR mouse-2
Go to the original location of the item in another window.
***** org-agenda-switch-to :: RET
Go to the original location of the item and delete other windows.
***** org-agenda-follow-mode :: F
Toggle Follow mode. In Follow mode, as you move point through the
 agenda buffer, the other window always shows the corresponding
 location in the Org file.
***** org-agenda-open-link :: C-c C-o
Follow a link in the entry. This offers a selection of any links
 in the text belonging to the referenced Org node.
**** Change display
***** A
Interactively select another agenda view and append it to the current view.
***** O
Delete other windows.
***** org-agenda-day-view :: v d OR d
Switch to day view.  When switching to day view, this setting
 becomes the default for subsequent agenda refreshes.  A numeric
 prefix argument may be used to jump directly to a specific day of
 the year.  For example, ‘32 d’ jumps to February 1st.  When setting
 day view, a year may be encoded in the prefix argument as well.
 For example, ‘200712 d’ jumps to January 12, 2007.
***** org-agenda-week-view :: v w OR w
Switch to week view.  When switching week view, this setting
 becomes the default for subsequent agenda refreshes.  A numeric
 prefix argument may be used to jump directly to a specific day of
 the ISO week.  For example ‘9 w’ to ISO week number 9.  When
 setting week view, a year may be encoded in the prefix argument as
 well.  For example, ‘200712 w’ jumps to week 12 in 2007.
***** org-agenda-month-view :: v m
Switch to month view.  Because month views are slow to create, they
 do not become the default for subsequent agenda refreshes.  A
 numeric prefix argument may be used to jump directly to a specific
 day of the month.  When setting month view, a year may be encoded
 in the prefix argument as well.  For example, ‘200712 m’ jumps to
 December, 2007.
***** org-agenda-year-view :: v y
Switch to year view.  Because year views are slow to create, they
 do not become the default for subsequent agenda refreshes.  A
 numeric prefix argument may be used to jump directly to a specific
 day of the year.
***** org-agenda-reset-view :: v SPC
Reset the current view to 'org-agenda-span'
***** org-agenda-later :: f
Go forward in time to display the span following the current one.
 For example, if the display covers a week, switch to the following
 week.  With a prefix argument, repeat that many times.
***** org-agenda-earlier :: b
***** org-agenda-goto-today :: .
***** org-agenda-goto-date :: j
***** org-agenda-redo :: r OR g
Recreate the agenda buffer, for example to reflect the changes
 after modification of the timestamps of items with ‘S-<LEFT>’ and
 ‘S-<RIGHT>’.  When the buffer is the global TODO list, a prefix
 argument is interpreted to create a selective list for a specific
 TODO keyword.
***** org-agenda-columns :: C-c C-x C-c
Invoke column view (see *note Column View::) in the agenda buffer.
 The column view format is taken from the entry at point, or, if
 there is no entry at point, from the first entry in the agenda
 view.  So whatever the format for that entry would be in the
 original buffer (taken from a property, from a ‘COLUMNS’ keyword,
 or from the default variable ‘org-columns-default-format’) is used
 in the agenda.
**** Remote Editing
***** org-agenda-undo :: C-_
***** org-agenda-todo :: t
***** org-agenda-kill :: C-k
Delete the current agenda item along with the entire subtree
 belonging to it in the original Org file.  If the text to be
 deleted remotely is longer than one line, the kill needs to be
 confirmed by the user.  See variable ‘org-agenda-confirm-kill’.
***** org-agenda-refile :: C-c C-w
***** org-agenda-archive-default-with-confirmation :: a
***** org-agenda-toggle-archive-tag :: C-c C-x a
***** org-agenda-show-tags :: T
Show all tags associated with the current item.  This is useful if
 you have turned off ‘org-agenda-show-inherited-tags’, but still
 want to see all tags of a headline occasionally.
***** org-agenda-set-tags :: :
***** org-agenda-priority :: ,
***** org-agenda-show-priority :: P
***** org-agenda-priority-up :: +
***** org-agenda-priority-down :: -
***** org-agenda-add-note :: C-c C-z OR z
***** org-agenda-attach :: C-c C-a
***** org-agenda-schedule :: C-c C-s
***** org-agenda-deadline :: C-c C-d
***** org-agenda-do-date-later :: S-RIGHT
Change the timestamp associated with the current line by one day
 into the future.  If the date is in the past, the first call to
 this command moves it to today.  With a numeric prefix argument,
 change it by that many days.  For example, ‘3 6 5 S-<RIGHT>’
 changes it by a year.  With a ‘C-u’ prefix, change the time by one
 hour.  If you immediately repeat the command, it will continue to
 change hours even without the prefix argument.  With a double ‘C-u
 C-u’ prefix, do the same for changing minutes.  The stamp is
 changed in the original Org file, but the change is not directly
 reflected in the agenda buffer.  Use ‘r’ or ‘g’ to update the
 buffer.
***** org-agenda-do-date-earlier :: S-LEFT
***** org-agenda-date-prompt :: >
***** org-agenda-clock-in :: I
***** org-agenda-clock-out :: O
***** org-agenda-clock-cancel :: X
***** org-agenda-capture :: k
**** Bulk remote editing selected entries
***** org-agenda-bulk-mark :: m
***** org-agenda-bulk-mark-all :: *
***** org-agenda-bulk-unmark :: u
***** org-agenda-bulk-remove-all-marks :: U
***** org-agenda-bulk-toggle :: M-m
***** org-agenda-bulk-toggle-all :: M-*
***** org-agenda-bulk-mark-regexp :: %
***** org-agenda-bulk-action :: B
****** p: Toggle persistent marks.
****** $: Archive all selected entries.
****** A: Archive entries by moving them to their respective archive siblings.
****** t
Change TODO state.  This prompts for a single TODO keyword and
 changes the state of all selected entries, bypassing blocking
 and suppressing logging notes—but not timestamps.
****** +: Add a tag to all selected entries.
****** -: Remove a tag from all selected entries.
****** s
Schedule all items to a new date.  To shift existing schedule
 dates by a fixed number of days, use something starting with
 double plus at the prompt, for example ‘++8d’ or ‘++2w’.
****** d: Set deadline to a specific date.
****** S
Reschedule randomly into the coming N days.  N is prompted
 for.  With a prefix argument (‘C-u B S’), scatter only across
 weekdays.
**** Calendar Commands
***** org-agenda-goto-calendar :: c
***** org-calendar-goto-agenda :: c
***** org-agenda-sunrise-sunset :: S
***** org-agenda-holidays :: H
**** Quit and exit
***** org-agenda-quit :: q
***** org-agenda-exit :: x

* TODO Markup
* TODO Exporting
* TODO Publishing
* TODO Working with Source code
* TODO Miscellaneous
* TODO Hacking
