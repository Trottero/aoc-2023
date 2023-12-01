
import argparse


if __name__ == '__main__':
    # Check the day that was passed in using argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--day', type=str, required=True)
    args = parser.parse_args()

    # Check if the directory already exists
    import os.path
    if os.path.exists(f'{args.day}'):
        print(f'Day {args.day} already exists!')
        exit(1)

    # Copy the template folder to the new day
    import shutil
    shutil.copytree('template', f'{args.day}')

    # Replace the {day} placeholder in the new files
    import os

    for root, dirs, files in os.walk(f'{args.day}'):
        for file in files:
            if file.endswith('.py') or file.endswith('.txt'):
                with open(os.path.join(root, file), 'r+') as f:
                    content = f.read()
                    f.seek(0)
                    f.write(content.replace('{day}', args.day))
                    f.truncate()
