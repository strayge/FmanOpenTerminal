import platform
from subprocess import call
from fman import DirectoryPaneCommand
from fman.url import splitscheme, as_human_readable


class OpenTerminal(DirectoryPaneCommand):
    def start_first_existed(self, commands, cwd):
        for command in commands:
            try:
                res = call(command, cwd=cwd)
                if res == 0:
                    return
            except FileNotFoundError:
                pass
        show_alert('No terminal found.')

    def __call__(self):
        url = self.pane.get_path()
        scheme, path = splitscheme(url)
        if scheme != 'file://':
            show_alert('No such path supported.')
            return
        local_path = as_human_readable(url)
        system = platform.system()

        if platform.system() == 'Windows':
            self.start_first_existed(
                (['wt'], ['cmd', '/c start cmd']),
                local_path,
            )
        elif system == 'Darwin':
            self.start_first_existed(
                (['open', '-a', 'iterm', '.'], ['open', '-a', 'terminal', '.']),
                local_path,
            )
        elif system == 'Linux':
            self.start_first_existed(
                (['gnome-terminal'], ['xfce4-terminal'], ['konsole'], ['x-terminal-emulator']),
                local_path,
            )
        else:
            show_alert('Unknown platform.')
