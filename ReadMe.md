AsciiDoc Package for Sublime Text
===================================

**Currently looking for a maintainer!**

This is an [AsciiDoc][] package for [Sublime Text][st]. It adds syntax highlighting and snippets for the AsciiDoc language to Sublime Text.

Sublime Text is compatible with the TextMate editor for OS X snippets, preferences and languages files. However, even though Sublime can recognize the Textmate snippets, some features such as tab completion and shortcut commands do not work out of the box. This package overcomes these limitations.


Installation
------------

### Package Control
Find the package on Package Control under the name [`AsciiDoc`][pkg].


### Manual
To install the package manually, follow these steps:

 - Download the zip containing src files.
 - Extract the files to an *AsciiDoc* folder (create this folder if not present already) under:
    - Windows: *%APPDATA%\Sublime Text\Packages*
    - OS X: *~/Library/Application Support/Sublime Text/Packages*
    - Linux: *~/.config/sublime-text/Packages*
    - Portable Installation: *Sublime Text/Data*
 - Close all instances of Sublime Text and relaunch the editor.

If successful, you should see an **AsciiDoc** entry under **View > Syntax** and under **Tools > Snippets**.

**Note**: Snippets may take few seconds to load under Windows.


Configure Variables: `TM_FULLNAME`, `TM_EMAIL`, etc.
------------------------------------------------
The Article snippet refers to certain variables that are styled after the TextMate standard for environment variables (as do other features of Sublime). These variables are configured via the Default.tmPreferences file.

1. Edit *Default.tmPreferences*
2. Replace "My Full Name", "My Email", and "My Company" with your actual name, email address, and company name.
3. Update the defintion of `TM_YEAR` (currently 2013) if necessary.
4. Test the Article snippet (create a new AsciiDoc file, type `ar` and hit Tab).


Configure the AsciiDoc Build System
-----------------------------------
Sublime has a build system for compiling source code like AsciiDoc source. A file called *asciidoc.sublime-build* is provided here to allow you to take advantage of the build system, but it needs to be told where you have installed Python and AsciiDoc:

1. Edit *asciidoc.sublime-build*
2. Change the `working_dir` from */path/to/asciidoc-8.6.8* to the actual location where you have AsciiDoc installed (e.g. *C:\prgs\asciidoc-8.6.8*)
3. Change the first parameter of `cmd` from */path/to/python* to the actual name and location of your Python engine (e.g. *C:\Python39\python.exe*)
4. Note: See below about <kbd>Ctrl</kbd>+<kbd>B</kbd> no longer being the shortcut key for the build system.


Usage
-----
 - Create a new file, save it as *\<filename\>.asc*
 - Start typing AsciiDoc!


Snippets
--------
Snippets can be inserted anywhere by using the menu command **Tools > Snippets > AsciiDoc** or by typing two initial characters and hitting tab to complete.
A few tab completion examples are:

 - Start a new article (type `ar TAB`)
 - Comments (type `// TAB`)
 - Headings (type `h1 TAB` to `h4 TAB` for one-liner versions)
 - Table generation (type `|= TAB`)
 - Tab expansion for blocks (type `== TAB`)
 - Sidebar block (type `** TAB`)
 - Add a definition to a glossary (type `:: TAB`)
 - Refer to a glossary definition elsewhere (type `<< TAB`)

### Article
When you first invoke the Article snippet, "Title" will be highlighted. Type over it with the actual title you want. (Notice that the new title will be automatically underlined to length.) Hit tab to move off the title, and the backend choices will be highlighted. These are only the 3 most popular backends. Either delete 2 of them, or type over the whole thing with a 4th choice (e.g. manpage). Hit tab to move to the end.

### Definition and Definition Link
Use these to create glossary definitions with anchors and corresponding references to them. Note how the anchor tags will be automatically composed as you type the name of the term being defined, and also how any non-alphanumeric characters are automatically left out of the tag.


Keyboard Shortcuts
------------------
Basic support for some handy shortcuts are now available:

 - **Bold** selection: Select some text and then press <kbd>Ctrl</kbd>+<kbd>B</kbd>
 - *Italic*ize selection: Select some text and then press <kbd>Ctrl</kbd>+<kbd>I</kbd>
 - Mark selection as Code literal: Select some text and then press <kbd>Ctrl</kbd>+<kbd>K</kbd>, <kbd>Ctrl</kbd>+<kbd>K</kbd>
 - Mark selection as filename: Select some text and then press <kbd>Ctrl</kbd>+<kbd>K</kbd>, <kbd>Ctrl</kbd>+<kbd>F</kbd>

**Note**: <kbd>Ctrl</kbd>+<kbd>B</kbd> overrides the standard key binding of `Tools > Build System`. If this bothers you, you can edit the `.sublime-keymap` files (based on your OS) under `Packages\AsciiDoc` folder.

Time permitting, I'll add more shortcuts but meanwhile if you come upon something useful, feel free to submit a patch!


Enhancements
------------

Following are planned enhancements for the package:

 - ~~Add keyboard shortcuts for various commands such bold text, italics, blocks etc.~~
 - ~~Adding Build system to preview as HTML or PDF.~~

Your suggestions are welcome.


Author & Credits
----------------
Created by Hrusikesh Panda. Copy left or right, as you wish.

Credit goes to Christian Zuckschwerdt for his original work on [AsciiDoc TextMate bundle][adoc-tm].

The Article, Definition, and Definition Link snippets were written by Craig Jones.

[asciidoc]: https://asciidoc.org
[st]: https://www.sublimetext.com
[pkg]: https://packagecontrol.io/packages/AsciiDoc
[adoc-tm]: https://github.com/zuckschwerdt/asciidoc.tmbundle
