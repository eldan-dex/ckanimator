# ckAnimator

This [Python 3] script enables you to quickly and easily create seamless color transitions in A4Tech Bloody RGB mouse .ckAnimation files. Such option is not, to my knowledge, currently available in supplied [Bloody6] software suite.

The script is pre-set to generate an example .ckAnimation file out-of-the-box.

## Usage

1. Create and save a custom still frame animation using the [Bloody6] editor
2. Locate Bloody6' resource directory and open your custom .ckAnimation file in a text editor
3. Copy the contents of its `<ColorPicture>` tags into ckanimator.py file's `COLOR_LIST` as instructed (overwrite example)
4. Further customize the script's variables to your liking
5. Run the script using [Python 3]
6. Import the output file into the Bloody6 suite

## Notes

**Bloody mouses officially support up to 99-frame animations. The Bloody6 animation editor does NOT support larger files and crashes on the attempt. Exceeding the frame limit may lead to memory access violation!**

Likely location of the Bloody6 resource directory:
```
C:\Program Files (x86)\Bloody6\Bloody6\Data\RES\English\SLED\Standard8
```
Tested on Bloody P85 only. Sorry for messy code, I honestly don't expect anyone to use this ever.

## License

MIT

[Python 3]: <https://www.python.org/>
[Bloody6]: <http://software.bloody.com>
