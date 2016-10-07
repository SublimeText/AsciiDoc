import sublime
import sublime_plugin


class AdocPasteAsLinkCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        sel = view.sel()[0]
        text = view.substr(sel)
        contents = sublime.get_clipboard()
        view.replace(edit, sel, "" + contents + "["+text+"]")

    def is_enabled(self):
        return bool(self.view.sel())
