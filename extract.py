import os
import shutil


def copy(from_, to, sources):
    print(f'Copy from \'{from_}\', to \'{to}\'.')
    for file in sources:
        source = os.path.join(from_, file)
        target = os.path.join(to, file)
        print(f'- \'{source}\' -> \'{target}\'.')
        if os.path.isfile(source):
            if os.path.exists(target):
                print(f'  ^ File \'{target}\' existed.')
                os.remove(target)
            shutil.copyfile(source, target)
        else:
            if os.path.exists(target):
                print(f'  ^ Directory \'{target}\' existed.')
                shutil.rmtree(target)
            shutil.copytree(source, target)


if __name__ == '__main__':
    copy(
        os.path.join('.', 'blivechat'),
        os.path.join('.'),
        [
            'data', 'frontend', 'log',
            'api', 'blivedm', 'models',
            'config.py', 'main.py', 'update.py'
        ]
    )
